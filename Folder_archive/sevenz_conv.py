import py7zr
import zipfile
import subprocess
import os
from Folder_main.dependency_check import WINRAR_PATH 

def convert_f_7z_to_zip(input_path, output_path, temp_dir):
    with py7zr.SevenZipFile(input_path, "r") as archive:
        archive.extractall(temp_dir)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, temp_dir)
                zipf.write(abs_path, rel_path)

def convert_f_7z_to_rar(input_path, output_path, temp_dir):
    with py7zr.SevenZipFile(input_path, "r") as archive:
        archive.extractall(temp_dir)

    subprocess.run([WINRAR_PATH, "a", "-r", output_path, temp_dir], check=True)
