"""HED tool"""

#Standard Imports
import argparse
import pathlib

#Project imports
from utils.read import read

def main():
    """Main"""

    args = get_args()

    patient_data = read(args.input_file)
    print(patient_data)




def get_args():
    """Create the Argument Parser"""

    #Construct the argument parser
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('input_file',
                        type=pathlib.Path,
                        help="Input file containg typings")

    return parser.parse_args()

if __name__ == '__main__':
    main()
