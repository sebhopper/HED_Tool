"""HED tool"""

#Standard Imports
import argparse
import pathlib

#Project imports
from HED_tool.utils.read import read
from HED_tool.utils.build_alignments import build_alignments
from HED_tool.core.calculate import calculate

def main():
    """Main"""

    args = get_args()

    patient_data = read(args.input_file)

    for patient in patient_data:
        results = []
        results.append({'patient_id': patient.get('patient_id'),
                        })
        allele_seqs = build_alignments(patient, args.alignments)
        for allele in allele_seqs:
            gene = list(allele.keys())[0].split('*')[0]
            hed = calculate(allele)
            results.append({'gene': gene,
                            'HED': hed
                            })
        print(results)

def get_args():
    """Create the Argument Parser"""

    #Construct the argument parser
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('input_file',
                        type=pathlib.Path,
                        help="Input file containg typings")

    parser.add_argument('alignments',
                        type=pathlib.Path,
                        help="Directory containing all alignment files")

    return parser.parse_args()

if __name__ == '__main__':
    main()
