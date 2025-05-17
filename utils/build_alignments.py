"""Build the required alignments"""
import pathlib
from HED_tool.utils.alignment_parsing import HEDAlignment, remove_pipes
from HED_tool.utils.translate import translate_nt_to_prot
from HED_tool.utils.process_indels import process_indels

def build_alignments(patient_data:dict, alignments_directory:pathlib.Path):
    """Function to build the required alignments"""
    grouped_allele_seqs = {}  # {gene_prefix: {allele: protein_sequence}}

    for _, typing in patient_data.get('typing').items():
        gene = typing[0].split('*')[0]
        alignment = HEDAlignment(alignments_directory / f"{gene}_nuc.txt", required_typings=typing)  # pylint: disable=line-too-long
        # alignment = alignment.exon2_3_alignment()

        preprocessed_alignment = alignment.exon2_3_alignment()
        print(preprocessed_alignment)
        # Insert logic here to determine ARD or full CDS
        processed_alignment = process_indels(preprocessed_alignment)
        processed_alignment = remove_pipes(processed_alignment)


        for allele in typing:
            if allele in processed_alignment:
                protein_seq = translate_nt_to_prot(processed_alignment[allele]).rstrip('*')
                gene_prefix = allele.split('*')[0]

                if gene_prefix not in grouped_allele_seqs:
                    grouped_allele_seqs[gene_prefix] = {}
                grouped_allele_seqs[gene_prefix][allele] = protein_seq

    # Convert to list of grouped dicts
    allele_seq_list = list(grouped_allele_seqs.values())
    print(allele_seq_list)
    return allele_seq_list
