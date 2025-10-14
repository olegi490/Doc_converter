import os
import os
import zipfile
import py7zr
import subprocess

from Folder_main.dependency_check import WINRAR_PATH

def convert_f_zip_to_7z(input_path, output_path, temp_dir):
    with zipfile.ZipFile(input_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    with py7zr.SevenZipFile(output_path, "w") as archive:
        archive.writeall(temp_dir, ".")

def convert_f_zip_to_rar(input_path, output_path, temp_dir):
    with zipfile.ZipFile(input_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    subprocess.run([WINRAR_PATH, "a", "-r", output_path, temp_dir], check=True)
