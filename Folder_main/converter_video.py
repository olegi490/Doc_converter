import os
import logging

from Folder_video.mp4_conv import (
    convert_v_mp4_to_mkv, 
    convert_v_mp4_to_avi, 
    convert_v_mp4_to_flv, 
    convert_v_mp4_to_webm
)
from Folder_video.mov_conv import (
    convert_v_mov_to_mkv, 
    convert_v_mov_to_avi, 
    convert_v_mov_to_flv, 
    convert_v_mov_to_webm
)
from Folder_video.mkv_conv import (
    convert_v_mkv_to_mp4, 
    convert_v_mkv_to_avi, 
    convert_v_mkv_to_flv, 
    convert_v_mkv_to_webm
)

from Folder_video.avi_conv import (
    convert_v_avi_to_mp4, 
    convert_v_avi_to_mov,
    convert_v_avi_to_mkv, 
    convert_v_avi_to_flv, 
    convert_v_avi_to_webm
)
from Folder_video.flv_conv import (
    convert_v_flv_to_mp4, 
    convert_v_flv_to_mov,
    convert_v_flv_to_mkv, 
    convert_v_flv_to_avi, 
    convert_v_flv_to_webm
)
from Folder_video.webm_conv import (
    convert_v_webm_to_mp4, 
    convert_v_webm_to_mov,
    convert_v_webm_to_mkv, 
    convert_v_webm_to_avi, 
    convert_v_webm_to_flv
)

# Path to FFmpeg
FFMPEG_PATH = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"

SUPPORTED_VIDEO = {"mp4", "mov", "mkv", "avi", "flv", "webm"}

mapping = {
    ("mp4", "mkv"): convert_v_mp4_to_mkv,
    ("mp4", "avi"): convert_v_mp4_to_avi,
    ("mp4", "flv"): convert_v_mp4_to_flv,
    ("mp4", "webm"): convert_v_mp4_to_webm,

    ("mov", "mkv"): convert_v_mov_to_mkv,
    ("mov", "avi"): convert_v_mov_to_avi,
    ("mov", "flv"): convert_v_mov_to_flv,
    ("mov", "webm"): convert_v_mov_to_webm,

    ("mkv", "mp4"): convert_v_mkv_to_mp4,
    ("mkv", "avi"): convert_v_mkv_to_avi,
    ("mkv", "flv"): convert_v_mkv_to_flv,
    ("mkv", "webm"): convert_v_mkv_to_webm,

    ("avi", "mp4"): convert_v_avi_to_mp4,
    ("avi", "mov"): convert_v_avi_to_mov,
    ("avi", "mkv"): convert_v_avi_to_mkv,
    ("avi", "flv"): convert_v_avi_to_flv,
    ("avi", "webm"): convert_v_avi_to_webm,

    ("flv", "mp4"): convert_v_flv_to_mp4,
    ("flv", "mov"): convert_v_flv_to_mov,
    ("flv", "mkv"): convert_v_flv_to_mkv,
    ("flv", "avi"): convert_v_flv_to_avi,
    ("flv", "webm"): convert_v_flv_to_webm,

    ("webm", "mp4"): convert_v_webm_to_mp4,
    ("webm", "mov"): convert_v_webm_to_mov,
    ("webm", "mkv"): convert_v_webm_to_mkv,
    ("webm", "avi"): convert_v_webm_to_avi,
    ("webm", "flv"): convert_v_webm_to_flv,
}

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

def _detect_format(path):
    return os.path.splitext(path)[1].lower().strip(".")

def _validate_format(fmt):
    if fmt not in SUPPORTED_VIDEO:
        raise ValueError(f"Unsupported video format: '{fmt}'")

def convert_v(input_path, output_path):
    """Main entry point: convert between video formats."""
    inp = _detect_format(input_path)
    out = _detect_format(output_path)

    _validate_format(inp)
    _validate_format(out)

    if inp == out:
        raise ValueError("Input and output formats are identical.")

    func = mapping.get((inp, out))
    if not func:
        raise NotImplementedError(f"Conversion {inp} → {out} not supported yet.")

    return func(input_path, output_path, ffmpeg_path=FFMPEG_PATH)