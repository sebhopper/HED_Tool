"""HED tool"""

#Standard Imports
import argparse
import pathlib

#Project imports
from utils.read import read
from bio_utils.alignment_functions import parse_alignments, retrieve_required_alignments

def main():
    """Main"""

    args = get_args()

    patient_data = read(args.input_file)
    print(patient_data)

    # alignments = parse_alignments('A', args.alignments)
    retrieve_required_alignments(patient_data, args.alignments)



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
