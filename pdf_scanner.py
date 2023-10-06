import os
import logging
import pdfplumber
from tqdm import tqdm
from tkinter import filedialog
from tkinter import Tk
from prettytable import PrettyTable

# Set up logging to file
logging.basicConfig(filename='log.txt', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_folder_for_pdfs(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

def read_pdf(file_path):
    try:
        text_content = ''
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text_content += page.extract_text()
        return text_content
    except Exception as e:
        logging.error(f"Failed to read {file_path}: {e}")
        return ''

def load_medical_conditions(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file if line.strip())

def identify_medical_conditions(text_content, medical_conditions_list):
    found_conditions = set()
    for condition in medical_conditions_list:
        if condition.lower() in text_content.lower():
            found_conditions.add(condition)
    return found_conditions

def report_conditions_to_table(conditions_dict):
    table = PrettyTable()
    table.field_names = ["Medical Condition", "File", "Line"]
    for condition, files in conditions_dict.items():
        for file, line in files:
            table.add_row([condition, file, line])
    print(table)
    # Log the table to log.txt
    with open('log.txt', 'a') as f:
        f.write(table.get_string() + '\n')

def main():
    root = Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select the medical list text file
    conditions_file_path = filedialog.askopenfilename(title="Select the Medical List Text File")
    if not conditions_file_path:
        logging.info("No medical list text file selected. Exiting.")
        return

    # Prompt user to select the folder containing PDF files
    folder_path = filedialog.askdirectory(title="Select Folder with PDFs")
    if not folder_path:
        logging.info("No folder selected. Exiting.")
        return

    logging.info(f"Scanning folder: {folder_path}")
    pdf_files = scan_folder_for_pdfs(folder_path)
    logging.info(f"Found {len(pdf_files)} PDF files.")

    # Load medical conditions from the selected file
    medical_conditions_list = load_medical_conditions(conditions_file_path)

    conditions_dict = {}

    for pdf_file in tqdm(pdf_files, desc="Processing PDF files", unit="file"):
        text_content = read_pdf(pdf_file)
        found_conditions = identify_medical_conditions(text_content, medical_conditions_list)
        for condition in found_conditions:
            conditions_dict.setdefault(condition, []).append((pdf_file, ''))  # Line info not available yet

    # Report conditions to table
    report_conditions_to_table(conditions_dict)

if __name__ == "__main__":
    main()
