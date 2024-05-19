# Genome Inspector 1.0
**Genome Inspector 1.0** is a graphical user interface (GUI) application for performing various DNA sequence analyses. It is designed to be user-friendly and accessible for researchers, students, and anyone interested in molecular biology. The application leverages the Tkinter library for the GUI and Biopython for powerful sequence analysis capabilities.

## Features

- **DNA to RNA Conversion:** Convert a DNA sequence to its RNA counterpart.
- **DNA Complement:** Generate the complementary DNA sequence.
- **DNA to Amino Acid:** Translate a DNA sequence to its corresponding amino acid sequence (one-letter and three-letter codes).
- **Translate Reading Frame:** Translate the DNA sequence starting from a specified reading frame.
- **Reverse Complement:** Generate the reverse complement of the DNA sequence.
- **Find Restriction Sites:** Identify the locations of specified restriction enzyme sites within the DNA sequence.
- **Find ORFs:** Detect open reading frames (ORFs) within the DNA sequence.
- **Count Nucleotide Frequencies:** Count occurrences of each nucleotide (A, T, G, C) in the DNA sequence.
- **GC Content:** Calculate the GC content percentage in the DNA sequence.
- **Melting Temperature:** Compute the melting temperature of the DNA sequence.
- **Annealing Temperature:** Estimate the annealing temperature, typically 5°C lower than the melting temperature.
- **Quick Analysis:** Perform a quick summary analysis, including base count, GC content, melting temperature, annealing temperature, and nucleotide frequencies.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AtharvaTilewale/genome-inspector.git
   cd genome-inspector

2. **Install required dependencies:**
   - Ensure you have Python installed (version 3.6 or higher).
   - Install the required Python packages using pip:
   ```sh
   pip install biopython

3. **Installation**
   ```sh
   chmod +x 777 setup
   ./setup

4. **Run the program**
   ```sh
   geneinspect

## Usage
1) Launch the application:
Run the Python script to start the Genome Inspector GUI.

2) Input DNA Sequence:

- You can manually enter a DNA sequence in the input field.
- Alternatively, use the "Browse File" button to upload a sequence file (FASTA, FASTQ, or plain text).

3) Select Analysis Option:

- Choose from various analysis options by clicking the respective buttons on the home screen.
- For restriction site analysis, you will be prompted to enter the enzyme site.

4) View Results:

- The results of the selected analysis will be displayed in the text area within the application.
- You can save the results to a text file using the "Save Results" button.

## Screenshots

![Home Screen](path/to/home_screen.png)
![Analysis Result](path/to/analysis_result.png)


## Contributing
Contributions are welcome! Please follow these steps:

1) Fork the repository.
2) Create a new branch for your feature or bugfix.
3) Commit your changes with a descriptive message.
4) Push your branch to your fork.
5) Open a pull request detailing your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions, suggestions, or feedback, feel free to open an issue or contact the project maintainers.


---

**Genome Inspector 1.0** © 2024 Atharva Tilewale
