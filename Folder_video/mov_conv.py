import subprocess
import logging

def _run_ffmpeg(input_path, output_path, ffmpeg_path):
    cmd = [ffmpeg_path, "-y", "-i", input_path, output_path]
    logging.info(f"Running command: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        logging.info(f"Conversion successful: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg failed: {e}")
        raise

def convert_v_mov_to_mkv(input_path, output_path, ffmpeg_path):
    return _run_ffmpeg(input_path, output_path, ffmpeg_path)

def convert_v_mov_to_avchd(input_path, output_path, ffmpeg_path):
    return _run_ffmpeg(input_path, output_path, ffmpeg_path)

def convert_v_mov_to_avi(input_path, output_path, ffmpeg_path):
    return _run_ffmpeg(input_path, output_path, ffmpeg_path)

def convert_v_mov_to_flv(input_path, output_path, ffmpeg_path):
    return _run_ffmpeg(input_path, output_path, ffmpeg_path)

def convert_v_mov_to_webm(input_path, output_path, ffmpeg_path):
    return _run_ffmpeg(input_path, output_path, ffmpeg_path)
