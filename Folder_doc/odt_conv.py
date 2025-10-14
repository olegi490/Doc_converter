import os
import subprocess
import glob

LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_with_libreoffice(input_file, output_file, output_format, filter_name=None):
    
    if not os.path.exists(input_file):
        print(f"[Error] File not found: {input_file}")
        return False

    output_dir = os.path.dirname(output_file) or "."
    os.makedirs(output_dir, exist_ok=True)

    try:
        conv_target = output_format
        if filter_name:
            conv_target += f":{filter_name}"

        cmd = f'"{LIBREOFFICE_PATH}" --headless --convert-to "{conv_target}" --outdir "{output_dir}" "{input_file}"'

        # Run LibreOffice
        subprocess.run(cmd, shell=True, check=True)

        generated_file = None
        for f in glob.glob(os.path.join(output_dir, "*.*")):
            if f.lower().endswith(output_format.lower()):
                generated_file = f
                break

        if generated_file:
            if os.path.abspath(generated_file) != os.path.abspath(output_file):
                os.replace(generated_file, output_file)
            print(f"[Success] Converted {input_file} → {output_file}")
            return True
        else:
            print(f"[Error] Conversion failed: No {output_format} file produced.")
            return False

    except subprocess.CalledProcessError as e:
        print(f"[Error] LibreOffice failed: {e}")
        return False
    except Exception as e:
        print(f"[Error] Conversion exception: {e}")
        return False

def convert_odt_to_doc(input_odt, output_doc):
    return convert_with_libreoffice(input_odt, output_doc, "doc", "MS Word 97")

def convert_odt_to_docx(input_odt, output_docx):
    return convert_with_libreoffice(input_odt, output_docx, "docx")

def convert_odt_to_pdf(input_odt, output_pdf):
    return convert_with_libreoffice(input_odt, output_pdf, "pdf")

def convert_odt_to_txt(input_odt, output_txt):
    return convert_with_libreoffice(input_odt, output_txt, "txt")

def convert_odt_to_html(input_odt, output_html):
    return convert_with_libreoffice(input_odt, output_html, "html")
