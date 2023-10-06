# VA PDF Claim Scrapper

This project aims to extract medical conditions from a collection of PDF files containing medical records.

## Features

- Scan a specified folder for PDF files
- Extract text content from PDF files
- Identify a list of medical conditions from the text content
- Log the conditions found and their occurrences in the PDF files
- Generate a report table listing each condition found, the file it was found in, and the line it was found on

## Prerequisites

- **Python**: Ensure you have Python installed on your Windows system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

## Usage

1. Run the script.
2. When prompted, select the text file containing the list of medical conditions.
3. When prompted, select the folder containing the PDF files.
4. The script will process the PDF files and generate a log file `log.txt` and print a report table to the console.

## Running the Script

1. **Clone or Download the Repository**: If you haven't already, clone or download the project repository from GitHub to your local machine.

   ```
   git clone https://github.com/kaspaeve/VA_PDF_Claim_Scrapper.git
   ```
   This will create a local copy of the project in your current directory.

2. **Open Command Prompt**: Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

3. **Navigate to the Project Folder**: Use the `cd` command to navigate to the folder where the project is located.

4. **Install Dependencies**: Install the required dependencies for the project using `pip`:

   ```
   pip install -r requirements.txt
   ```

5. **Run the Script**: To run your script, use the `python` command followed by the script's filename. For example, if your script is named `pdf_scanner.py`, run:

   ```
   python pdf_scanner.py
   ```

6. **Follow the Prompts**:
   - Select the text file containing the list of medical conditions.
   - Select the folder containing the PDF files.
   - The script will process the PDF files and generate a log file `log.txt` and print a report table to the console.

7. **View the Results**: After the script completes, you can view the results in the console, as well as in the `log.txt` file.

## Dependencies

- pdfplumber
- tqdm
- tkinter
- prettytable

## License

MIT

## Contributing

Please feel free to submit issues and pull requests.
