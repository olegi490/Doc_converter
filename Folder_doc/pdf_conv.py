import os
import subprocess
import glob
import fitz  # PyMuPDF
import pdfplumber
import pandas as pd
from pdf2docx import Converter

LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_pdf_to_docx(input_pdf, output_docx):
    if not os.path.exists(input_pdf):
        print("PDF file not found.")
        return
    try:
        cv = Converter(input_pdf)
        cv.convert(output_docx, start=0, end=None)
        cv.close()
        print(f"Converted PDF to DOCX: {output_docx}")
    except Exception as e:
        print(f"PDF → DOCX conversion failed: {e}")

def convert_pdf_to_doc(input_pdf, output_doc):
    # Convert to DOCX then to DOC
    temp_docx = os.path.splitext(output_doc)[0] + "_temp.docx"
    convert_pdf_to_docx(input_pdf, temp_docx)
    if os.path.exists(temp_docx):
        convert_with_libreoffice(temp_docx, output_doc, "doc")
        os.remove(temp_docx)

def convert_with_libreoffice(input_file, output_file, output_format):
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return
    try:
        subprocess.run([
            LIBREOFFICE_PATH,
            "--headless",
            "--convert-to", output_format,
            "--outdir", os.path.dirname(output_file),
            input_file
        ], check=True)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        matches = glob.glob(os.path.join(os.path.dirname(output_file), base_name + ".*"))
        if matches:
            actual_file = matches[0]
            if actual_file != output_file:
                os.replace(actual_file, output_file)
            print(f"Converted {input_file} → {output_file}")
        else:
            print(f"LibreOffice did not produce output for {input_file}")
    except FileNotFoundError:
        print("LibreOffice not found. Please check LIBREOFFICE_PATH.")
    except subprocess.CalledProcessError as e:
        print(f"LibreOffice conversion failed: {e}")

# -------------------- PDF → TXT --------------------
def convert_pdf_to_txt(input_pdf, output_txt):
    if not os.path.exists(input_pdf):
        print("PDF file not found.")
        return
    doc = fitz.open(input_pdf)
    text = "\n".join(page.get_text() for page in doc)
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Converted PDF to TXT: {output_txt}")

# -------------------- PDF → HTML --------------------
def convert_pdf_to_html(input_pdf, output_html):
    convert_with_libreoffice(input_pdf, output_html, "html")

# -------------------- PDF → CSV --------------------
def convert_pdf_to_csv(input_pdf, output_csv):
    if not os.path.exists(input_pdf):
        print("PDF file not found.")
        return
    try:
        with pdfplumber.open(input_pdf) as pdf:
            rows = [row for page in pdf.pages for table in page.extract_tables() for row in table]
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return
    if not rows:
        pd.DataFrame([["No tables found"]]).to_csv(output_csv, index=False)
        print(f"No tables found. Created CSV with notice: {output_csv}")
    else:
        pd.DataFrame(rows).to_csv(output_csv, index=False)
        print(f"Converted PDF to CSV: {output_csv}")
