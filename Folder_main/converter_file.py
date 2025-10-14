import os
import logging
import shutil

WINRAR_PATH = r"C:\Program Files\WinRAR\Rar.exe"


from Folder_archive.zip_conv import (
    convert_f_zip_to_7z, 
    convert_f_zip_to_rar 
)
from Folder_archive.sevenz_conv import (
    convert_f_7z_to_zip, 
    convert_f_7z_to_rar
)
from Folder_archive.rar_conv import ( 
    convert_f_rar_to_zip, 
    convert_f_rar_to_7z
)

SUPPORTED_ARCHIVE = {"zip", "rar", "7z"}

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

# Mapping: (input_format, output_format) - conversation function
mapping = {
    ("zip", "7z"): convert_f_zip_to_7z,
    ("zip", "rar"): convert_f_zip_to_rar,
    ("7z", "zip"): convert_f_7z_to_zip,
    ("7z", "rar"): convert_f_7z_to_rar,
    ("rar", "zip"): convert_f_rar_to_zip,
    ("rar", "7z"): convert_f_rar_to_7z,
}

def _detect_format(path):
    return os.path.splitext(path)[1].lower().strip(".")

def _validate_format(fmt):
    if fmt not in SUPPORTED_ARCHIVE:
        raise ValueError(f"Unsupported archive format: '{fmt}'")

def convert_f(input_path, output_path):
    """Convert between archive formats using the mapping."""
    inp = _detect_format(input_path)
    out = _detect_format(output_path)

    _validate_format(inp)
    _validate_format(out)

    if inp == out:
        raise ValueError("Input and output formats are identical.")

    temp_dir = os.path.splitext(input_path)[0] + "_temp"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        func = mapping.get((inp, out))
        if not func:
            raise NotImplementedError(f"Conversion {inp} → {out} not supported yet.")
        func(input_path, output_path, temp_dir)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    logging.info(f"Converted {inp.upper()} → {out.upper()} successfully: {output_path}")
    return output_path
