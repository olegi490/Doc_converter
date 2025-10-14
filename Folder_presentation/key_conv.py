import os
import os

import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

def convert_p_key_to_pptx(input_path, output_path):
    logging.info(f"Converting KEY → PPTX: {input_path} → {output_path}")
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(f_in.read())
    return True

def convert_p_key_to_odp(input_path, output_path):
    logging.info(f"Converting KEY → ODP: {input_path} → {output_path}")
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(f_in.read())
    return True
