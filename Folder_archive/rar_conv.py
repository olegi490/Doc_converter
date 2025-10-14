import rarfile
import zipfile
import py7zr
import os

def convert_f_rar_to_zip(input_path, output_path, temp_dir):
    with rarfile.RarFile(input_path) as rar_ref:
        rar_ref.extractall(temp_dir)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, temp_dir)
                zipf.write(abs_path, rel_path)

def convert_f_rar_to_7z(input_path, output_path, temp_dir):
    with rarfile.RarFile(input_path) as rar_ref:
        rar_ref.extractall(temp_dir)

    with py7zr.SevenZipFile(output_path, "w") as archive:
        archive.writeall(temp_dir, ".")
