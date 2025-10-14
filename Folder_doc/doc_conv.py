import os
import subprocess
import glob
import tempfile
from Folder_doc.txt_conv import convert_txt_to_csv

# Path to your LibreOffice executable
LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

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
def convert_doc_to_txt(input_doc, output_txt):
    convert_with_libreoffice(input_doc, output_txt, "txt")

def convert_doc_to_csv(input_doc, output_csv):
    # DOC to TXT then to CSV
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp:
        temp_txt = temp.name
    try:
        convert_doc_to_txt(input_doc, temp_txt)
        convert_txt_to_csv(temp_txt, output_csv)
        print(f"Converted {input_doc} → {output_csv}")
    finally:
        if os.path.exists(temp_txt):
            os.remove(temp_txt)

def convert_doc_to_pdf(input_doc, output_pdf):
    convert_with_libreoffice(input_doc, output_pdf, "pdf")

def convert_doc_to_html(input_doc, output_html):
    convert_with_libreoffice(input_doc, output_html, "html")

def convert_doc_to_odt(input_doc, output_odt):
    convert_with_libreoffice(input_doc, output_odt, "odt")

def convert_doc_to_docx(input_doc, output_docx):
    convert_with_libreoffice(input_doc, output_docx, "docx")
