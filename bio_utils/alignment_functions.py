#Standard imports
import pathlib
import re

ALLELE_NAME_REGEX = re.compile(r'([A-Za-z1-9]+\*(?:\d+:?)+\d+[NSQL]?)')

def parse_alignments(gene, library_directory):
    """Parse alignments"""
    alignment_file = read_alignment_file(library_directory, gene)

    alignment = {}
    for line in alignment_file:
        #If the line doesn't begin with an allele name, skip over it
        if not ALLELE_NAME_REGEX.search(line):
            continue
        

        line = re.split(r'[\t ]+', line.strip())

        allele_name = line[0]

        if allele_name not in alignment:
            alignment[allele_name] = ''

        alignment[allele_name] += ''.join(line[1:])

        for allele_name, sequence in alignment.items():
            if '-' not in sequence:
                reference = allele_name
                break

    return reformat_alignment(reference, alignment)


def read_alignment_file(library_directory, gene):
    """Read Filepath of alignments"""

    filepath = pathlib.Path(f"{library_directory}/{gene}_prot.txt")
    with open(filepath, 'r', encoding='utf-8') as file:
        alignments = file.readlines()

    return alignments

def reformat_alignment(reference, alignment):
    """Reformat the alignments to turn any '-' into the sequence"""

    for allele_name, sequence in alignment.items():
        if allele_name == reference:
            continue

        alignment[allele_name] = ''.join(
            ref if seq == '-' else seq
            for ref, seq in zip(alignment[reference], sequence)
        )

    return alignment

def retrieve_required_alignments(patient_dict, library_directory):

    for patient in patient_dict:
        for key, values in patient.items():


    # alignment_file = read_alignment_file(library_directory, gene)

    # alignment = {}
    # for line in alignment_file:
    #     #If the line doesn't begin with an allele name, skip over it
    #     if not ALLELE_NAME_REGEX.search(line):
    #         continue
