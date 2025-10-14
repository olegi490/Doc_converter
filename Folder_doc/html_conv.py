import os
import subprocess

LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_with_libreoffice(input_file, output_dir, output_format, filter_name=None):

    os.makedirs(output_dir, exist_ok=True)

    try:
        conv_target = output_format
        if filter_name:
            conv_target += f":{filter_name}"

        subprocess.run([
            LIBREOFFICE_PATH,
            "--headless",
            "--convert-to", conv_target,
            "--outdir", output_dir,
            input_file
        ], check=True)

        print(f"Converted {input_file} to {output_format.upper()} in {output_dir}")

    except FileNotFoundError:
        print("LibreOffice not found. Please install or update LIBREOFFICE_PATH.")
    except subprocess.CalledProcessError as e:
        print(f"LibreOffice conversion failed: {e}")

def convert_html_to_pdf(input_html, output_pdf):
    if not os.path.exists(input_html):
        print("HTML file not found.")
        return
    convert_with_libreoffice(input_html, os.path.dirname(output_pdf), "pdf", "writer_pdf_Export")

def convert_html_to_docx(input_html, output_docx):
    if not os.path.exists(input_html):
        print("HTML file not found.")
        return
    convert_with_libreoffice(input_html, os.path.dirname(output_docx), "docx")

def convert_html_to_odt(input_html, output_odt):
    if not os.path.exists(input_html):
        print("HTML file not found.")
        return
    convert_with_libreoffice(input_html, os.path.dirname(output_odt), "odt")

def convert_html_to_txt(input_html, output_txt):
    if not os.path.exists(input_html):
        print("HTML file not found.")
        return
    convert_with_libreoffice(input_html, os.path.dirname(output_txt), "txt")
