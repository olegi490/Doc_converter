import os
import logging
from flask import request, send_file
from Folder_audio.audio_conv import convert_audio as base_convert_audio
from Folder_audio.yt_conv import download_youtube 


SUPPORTED_AUDIO = {"mp3", "wav", "mp4"}  # mp4 is audio only

conversion_options = {
    ".mp3": [".wav", ".mp4"],
    ".wav": [".mp3", ".mp4"],
    ".mp4": [".mp3", ".wav"],
}

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

def detect_format(path):
    return os.path.splitext(path)[1].lower().strip(".")

def validate_format(inp, out):
    if inp not in SUPPORTED_AUDIO:
        raise ValueError(f"Unsupported input format: {inp}")
    if out not in SUPPORTED_AUDIO:
        raise ValueError(f"Unsupported output format: {out}")
    if f".{out}" not in conversion_options.get(f".{inp}", []):
        raise ValueError(f"Conversion {inp} → {out} is not allowed")

def convert_file(input_path, output_path):
    inp = detect_format(input_path)
    out = detect_format(output_path)

    logging.info(f"Starting conversion: {input_path} -> {output_path}")
    validate_format(inp, out)

    base_convert_audio(input_path, output_path)

    logging.info(f"Conversion successful: {input_path} -> {output_path}")
    return output_path

def download_youtube_file(url, output_format="mp3", output_dir="outputs"):
    logging.info(f"Downloading from YouTube: {url} as {output_format}")
    os.makedirs(output_dir, exist_ok=True)
    filepath = download_youtube(url, output_dir=output_dir, output_format=output_format)
    logging.info(f"YouTube download complete: {filepath}")
    return filepath


def handle_audio_request():
    file = request.files.get("file")
    output_format = request.form.get("output_format")

    if not file or not output_format:
        return "Missing file or format", 400

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    input_path = os.path.join("uploads", file.filename)
    file.save(input_path)

    output_path = os.path.join(
        "outputs",
        f"{os.path.splitext(file.filename)[0]}.{output_format}"
    )

    try:
        convert_file(input_path, output_path)
    except Exception as e:
        return f"Conversion failed: {e}", 500

    return send_file(output_path, as_attachment=True)

def handle_youtube_request():
    url = request.form.get("youtube_url") 
    output_format = request.form.get("output_format")

    if not url or not output_format:
        return "Missing URL or format", 400

    try:
        downloaded_file = download_youtube_file(url, output_format=output_format)
    except Exception as e:
        return f"YouTube download/conversion failed: {e}", 500

    inp = detect_format(downloaded_file)
    if inp != output_format:
        output_path = os.path.join(
            "outputs",
            f"{os.path.splitext(os.path.basename(downloaded_file))[0]}.{output_format}"
        )
        try:
            convert_file(downloaded_file, output_path)
        except Exception as e:
            return f"YouTube conversion failed: {e}", 500
    else:
        output_path = downloaded_file

    return send_file(output_path, as_attachment=True)
