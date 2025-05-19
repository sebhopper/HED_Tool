# HED Tool

## Overview
- The HED Tool calculates the HLA Evolutionary Divergence (HED) between alleles that have been provided for a patient.
- It does this by parsing the IPD-IMGT/HLA alignment files and calculating the Grantham Matrix distance between two alleles at the same loci.


---

## Features
- **HED Calculation**: Computes HED for individual patients based on their HLA typings.
- **Support for ARD and Full CDS**: Allows analysis of the antigen recognition domain (ARD) or the full coding sequence (CDS).
- **Customizable Typings**: Supports patient-specific HLA typings for analysis.
- **Extensible Design**: Modular structure for easy integration and extension.

---

## Requirements
- Python version required: 
	- Python 3.8 or higher
- Libraries used
	- `re` 
	- `pathlib`
	- `Biopython`
	
- Please install any requirements through the requirements.txt file that is provided.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HED_tool.git
   cd HED_tool
   ```

2. Set up a virtual environment
	```bash
	python3 -m venv HED_ENV
	source HED_ENV/bin/activate
	```
3. Install dependencies
	```bash
	pip install -r requirements.txt
	```

---

## Usage through the Command-Line Interface (CLI)
Run the tool using the CLI:
 
 	```bash
 	python3 -m HED_tool -h
 	```
This will bring up the help prompts for the tool.

### Example command

	```bash
	python -m HED_tool example_file.txt True resources/alignments
	```
	
- Input File: A file containing patient typings (e.g, example_file.txt).
- ARD Status: True for ARD analysis, False for full CDS analysis.
- Alignments Directory: Path to the directory containing alignment files.

---

## Example Input and Output
### Input:
The input file should contain patient typings in the following format:

	`P001 A*01:01 B*07:02 DRB1*15:01 DRB3*02:02 MICA*001 TAP1*02:01`

	`P002 A*03:01 B*08:01 C*07:02 DRB1*13:01 DQB1*05:01 TAP2*01:01`

Where:
- Each line represents a patient.
- The first column includes the individual identifier.
- All subsequent columns are the HLA typings.
	
I have included example_file.txt within this repository as an example input file.

### Output:
The tool produces a dictionary with the following structure:
```
	{
    	'patient_id': 'P001',
    	'batch_results': {
    	    'class_i': 0.875,
    	    'class_ii': 0.775,
    	    'other_non_hla': 0.65
    	},
    	'individual_results': [
    	    {'gene': 'A', 'HED': 0.85},
    	    {'gene': 'B', 'HED': 0.90},
    	    {'gene': 'DRB1', 'HED': 0.75},
    	    {'gene': 'DRB3', 'HED': 0.80},
    	    {'gene': 'MICA', 'HED': 0.65}
    	]
	}
```

---

## Contact
For questions or feedback, please contact Sebastian Hopper.

---

## Disclaimer
The code for this project is a work in progress and is absolutely not intended for clinical use.
The code is provided as is and I take no responsibility for any errors or omissions in the code or the results produced by the code.
The code is provided for educational purposes only and should not be used for any other purpose.

---

## References
1. Chowell, D., Krishna, C., Pierini, F., Makarov, V., Rizvi, N. A., Kuo, F., … Chan, T. A. (2019). Evolutionary divergence of HLA class I genotype impacts efficacy of cancer immunotherapy. Nature Medicine, 25(11), 1715–1720. https://doi.org/10.1038/s41591-019-0639-4
2. Pierini, F., & Lenz, T. L. (2018). Divergent Allele Advantage at Human MHC Genes: Signatures of Past and Ongoing Selection. Molecular Biology and Evolution, 35(9), 2145–2158. Retrieved from http://dx.doi.org/10.1093/molbev/msy116
