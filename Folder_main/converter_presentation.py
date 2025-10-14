import os
import logging

from Folder_presentation.ppt_conv import (
    convert_p_ppt_to_odp, 
    convert_p_ppt_to_key
)

from Folder_presentation.odp_conv import (
    convert_p_odp_to_pptx, 
    convert_p_odp_to_key
)
from Folder_presentation.key_conv import (
    convert_p_key_to_pptx, 
    convert_p_key_to_odp
)

SUPPORTED_PRESENTATIONS = {"ppt", "pptx", "odp", "key"}

mapping = {
    ("ppt", "odp"): convert_p_ppt_to_odp,
    ("ppt", "key"): convert_p_ppt_to_key,
    ("pptx", "odp"): convert_p_ppt_to_odp,
    ("pptx", "key"): convert_p_ppt_to_key,
    ("odp", "pptx"): convert_p_odp_to_pptx,
    ("odp", "key"): convert_p_odp_to_key,
    ("key", "pptx"): convert_p_key_to_pptx,
    ("key", "odp"): convert_p_key_to_odp,
}

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

def _detect_format(path):
    return os.path.splitext(path)[1].lower().strip(".")

def _validate_format(fmt):
    if fmt not in SUPPORTED_PRESENTATIONS:
        raise ValueError(f"Unsupported presentation format: '{fmt}'")

def convert_p(input_path, output_path):
    """Main entry point for converting presentations."""
    inp = _detect_format(input_path)
    out = _detect_format(output_path)

    _validate_format(inp)
    _validate_format(out)

    if inp == out:
        raise ValueError("Input and output formats are identical.")

    func = mapping.get((inp, out))
    if not func:
        raise NotImplementedError(f"Conversion {inp} → {out} not supported yet.")

    return func(input_path, output_path)
