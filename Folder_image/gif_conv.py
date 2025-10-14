import os
from PIL import Image, ImageSequence
from Folder_image.image_utils import convert_image, _ensure_dir

def convert_i_gif(input_path: str, output_path: str) -> str:
 
    if os.path.isdir(output_path) or output_path.endswith("_frames"):
        _ensure_dir(output_path)
        with Image.open(input_path) as im:
            for i, frame in enumerate(ImageSequence.Iterator(im)):
                frame_path = os.path.join(output_path, f"frame_{i:03d}.png")
                frame.convert("RGBA").save(frame_path, "PNG")
        return output_path

    if os.path.isdir(output_path):
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(output_path, f"{base_name}.gif")

    ext = os.path.splitext(output_path)[1][1:].lower()
    if not ext:
        output_path = f"{output_path}.gif"
        ext = "gif"

    folder = os.path.dirname(output_path) or "outputs"
    _ensure_dir(folder)

    return convert_image(input_path, ext, folder)
