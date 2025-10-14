import os
from Folder_image.jpeg_conv import convert_i_jpeg
from Folder_image.jpg_conv import convert_i_jpg
from Folder_image.png_conv import convert_i_png
from Folder_image.gif_conv import convert_i_gif
from Folder_image.tiff_conv import convert_i_tiff
from Folder_image.webp_conv import convert_i_webp
from Folder_image.bmp_conv import convert_i_bmp

def convert_i(input_path: str, output_path: str) -> str:
   
    ext = os.path.splitext(input_path)[1].lower()
    out_ext = os.path.splitext(output_path)[1][1:].lower()
    out_dir = os.path.dirname(output_path) or "outputs"

    if ext in ['.jpg']:
        return convert_i_jpg(input_path, output_format=out_ext, output_folder=out_dir)
    elif ext in ['.jpeg']:
        return convert_i_jpeg(input_path, output_format=out_ext, output_folder=out_dir)
    elif ext == '.png':
        return convert_i_png(input_path, output_format=out_ext, output_folder=out_dir)
    elif ext == '.gif':
        return convert_i_gif(input_path, output_path)
    elif ext in ['.tif', '.tiff']:
        return convert_i_tiff(input_path, output_format=out_ext, output_folder=out_dir)
    elif ext == '.webp':
        return convert_i_webp(input_path, output_format=out_ext, output_folder=out_dir)
    elif ext == '.bmp':
        return convert_i_bmp(input_path, output_format=out_ext, output_folder=out_dir)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
