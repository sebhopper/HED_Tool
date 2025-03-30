"""
Functions to read in the data and make it parsable for calculations.
"""

#Standard Imports
import re

HLA_CLASS_I = ['A', 'B', 'C', 'E', 'F', 'G']
HLA_CLASS_I_PSEUDO = ['H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
HLA_CLASS_II = ['DRA', 'DRB1',	'DRB2',	'DRB3',	'DRB4',	'DRB5',
                'DRB6',	'DRB7',	'DRB8',	'DRB9', 'DQA1', 'DQA2', 
                'DQB1', 'DQB2', 'DPA1', 'DPA2', 'DPB1', 'DPB2', 
                'DMA', 'DMB', 'DOA', 'DOB']
OTHER_NON_HLA = ['HFE', 'MICA', 'MICB', 'TAP1', 'TAP2']

VALID_TYPING = ['A', 'B', 'C', 'E', 'F', 'G', 'H',
                'DRA', 'DRB1', 'DRB2', 'DRB3', 'DRB4', 'DRB5','DRB6', 'DRB7', 'DRB8', 'DRB9', 
                'DQA1', 'DQA2', 'DQB1', 'DQB2', 'DPA1', 'DPA2', 'DPB1', 'DPB2', 'DMA', 'DMB', 
                'DOA', 'DOB', 'MICA', 'MICB', 'TAP1', 'TAP2']

def read(input_filepath):
    """Script for reading in the data and making it parsable for further use"""

    patient_dict = read_patient_data(input_filepath)

    return patient_dict

def read_patient_data(patient_data_filepath):
    """Read and Process Patient Data into a dict format"""
    patients = []

    with open(patient_data_filepath, 'r', encoding='utf-8') as file:
        for line in file:
            patients.append(process_patient_data(line))

    return patients


def process_patient_data(line: str):
    """Process the patient data line into a dict"""

    #Define possible separators that could have been included in the file
    separators = r'[\s\t,;]'

    #Use re.split() to split on the first occurrence of any separator
    line_parts = re.split(separators, line, maxsplit=1)

    #Unpack the list results into the different parts
    patient_id = line_parts[0]
    remainder_of_line = line_parts[1] if len(line_parts) > 1 else ''

    #Initialise the line_dict with patient_id and an empty typing dictionary
    line_dict = {'patient_id': patient_id,
                 'typing': {}
                }

    #Define a mapping of HLA categories to their respective keys
    hla_categories = {'class_i': HLA_CLASS_I,
                         'class_i_pseudo': HLA_CLASS_I_PSEUDO,
                         'class_ii': HLA_CLASS_II,
                         'other_non_hla': OTHER_NON_HLA}

    #Populate the typing dictionary with non-empty values
    for key, hla_type in hla_categories.items():
        extracted_typing = extract_typing(remainder_of_line, hla_type)
        if extracted_typing:
            line_dict['typing'][key] = extracted_typing

    return line_dict

def extract_typing(typing_string: str, typing_to_extract: list):
    """ Function to use a regex to extract the typing information from the string """

    pattern = r'(?:' + '|'.join(re.escape(gene) for gene in typing_to_extract) + r')\*\d+(?::\d+)*'

    matches =  re.findall(pattern, typing_string)

    return matches
