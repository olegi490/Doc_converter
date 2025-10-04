import os
import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

def convert_p_odp_to_pptx(input_path, output_path):
    logging.info(f"Converting ODP → PPTX: {input_path} → {output_path}")
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(f_in.read())
    return True

def convert_p_odp_to_key(input_path, output_path):
    logging.info(f"Converting ODP → KEY: {input_path} → {output_path}")
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(f_in.read())
    return True
