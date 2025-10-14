import os
from PIL import Image

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def convert_image(input_path: str, output_format: str, output_dir: str) -> str:
    
    _ensure_dir(output_dir)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    out_ext = output_format.lower()
    output_path = os.path.join(output_dir, f"{base_name}.{out_ext}")

    img = Image.open(input_path)

    if out_ext in ["jpg", "jpeg"] and img.mode in ("RGBA", "LA"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    else:
        if img.mode not in ("RGB", "RGBA", "L"):
            img = img.convert("RGB")

    save_format = out_ext.upper()
    if save_format == "JPG":
        save_format = "JPEG"
    elif save_format == "TIF":
        save_format = "TIFF"

    img.save(output_path, save_format)
    return output_path
