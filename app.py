import os
from flask import Flask, request, send_file, render_template_string
from Folder_main.dependency_check import check_all_dependencies
from Folder_main.converter_doc import convert 
from Folder_main.converter_audio import handle_audio_request, handle_youtube_request
from Folder_main.converter_video import convert_v
from Folder_main.converter_file import convert_f
from Folder_main.converter_presentation import convert_p
from Folder_main.converter_image import convert_i

check_all_dependencies()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

INDEX_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multi Converter</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; }
        .btn { display: block; width: 250px; margin: 20px auto; padding: 15px; font-size: 18px; background: #4CAF50; color: white; text-decoration: none; border-radius: 8px; }
        .btn:hover { background: #45a049; }
    </style>
</head>
<body>
    <h1>Welcome to Multi Converter</h1>
    <a class="btn" href="/doc">📄 Document Converter</a>
    <a class="btn" href="/audio">🎵 Audio & YouTube Converter</a>
    <a class="btn" href="/video">🎬 Video Converter</a>
    <a class="btn" href="/archive">🗜️ Archive Converter</a>
    <a class="btn" href="/presentation">📊 Presentation Converter</a>
    <a class="btn" href="/image">🖼️ Image Converter</a>
</body>
</html>
'''

DOC_HTML = '''
<h2>Document Converter</h2>
<form method="post" enctype="multipart/form-data">
    <input type="hidden" name="converter" value="doc">
    <p><input type="file" name="file" required></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="pdf">PDF</option>
            <option value="doc">DOC</option>
            <option value="docx">DOCX</option>
            <option value="odt">ODT</option>
            <option value="html">HTML</option>
            <option value="xlsx">XLSX</option>
            <option value="txt">TXT</option>
            <option value="csv">CSV</option>
        </select>
    </p>
    <input type="submit" value="Convert Document">
</form>
<a href="/">⬅ Back</a>
'''

AUDIO_HTML = '''
<h2>Audio & YouTube Converter</h2>
<form method="post" enctype="multipart/form-data">
    <p><label>Upload an audio file:</label><br>
    <input type="file" name="file"></p>
    <p><label>Or paste YouTube URL:</label><br>
    <input type="text" name="youtube_url" style="width: 300px;"></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="mp3">MP3</option>
            <option value="wav">WAV</option>
            <option value="mp4">MP4</option>
        </select>
    </p>
    <input type="submit" value="Convert">
</form>
<a href="/">⬅ Back</a>
'''

VIDEO_HTML = '''
<h2>Video Converter</h2>
<form method="post" enctype="multipart/form-data">
    <input type="hidden" name="converter" value="video">
    <p><input type="file" name="file" required></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="mp4">MP4</option>
            <option value="mov">MOV</option>
            <option value="mkv">MKV</option>
            <option value="avi">AVI</option>
            <option value="flv">FLV</option>
            <option value="webm">WebM</option>
        </select>
    </p>
    <input type="submit" value="Convert Video">
</form>
<a href="/">⬅ Back</a>
'''

ARCHIVE_HTML = '''
<h2>Archive Converter (ZIP, RAR, 7Z)</h2>
<form method="post" enctype="multipart/form-data">
    <p><input type="file" name="file" required></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="zip">ZIP</option>
            <option value="rar">RAR</option>
            <option value="7z">7Z</option>
        </select>
    </p>
    <input type="submit" value="Convert Archive">
</form>
<a href="/">⬅ Back</a>
'''

PRESENTATION_HTML = '''
<h2>Presentation Converter</h2>
<form method="post" enctype="multipart/form-data">
    <p><input type="file" name="file" required></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="pptx">PPT / PPTX</option>
            <option value="odp">ODP</option>
            <option value="key">KEY</option>
        </select>
    </p>
    <input type="submit" value="Convert Presentation">
</form>
<a href="/">⬅ Back</a>
'''

IMAGE_HTML = '''
<h2>Image Converter</h2>
<form method="post" enctype="multipart/form-data">
    <p><input type="file" name="file" required></p>
    <p>Convert to:
        <select name="output_format" required>
            <option value="jpeg">JPEG / JPG</option>
            <option value="png">PNG</option>
            <option value="gif">GIF</option>
            <option value="tiff">TIFF / TIF</option>
            <option value="webp">WebP</option>
            <option value="bmp">BMP</option>
        </select>
    </p>
    <input type="submit" value="Convert Image">
</form>
<a href="/">⬅ Back</a>
'''


@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/doc', methods=['GET', 'POST'])
def doc_page():
    if request.method == 'POST':
        file = request.files.get('file')
        output_format = request.form.get('output_format')
        if not file or not output_format:
            return "Missing file or output format", 400
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        base_name = os.path.splitext(file.filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.{output_format}")
        try:
            convert(input_path, output_path)
        except Exception as e:
            return f"Conversion failed: {e}", 500
        return send_file(output_path, as_attachment=True)
    return render_template_string(DOC_HTML)

@app.route('/audio', methods=['GET', 'POST'])
def audio_page():
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        file = request.files.get('file')
        if youtube_url:
            return handle_youtube_request()
        elif file:
            return handle_audio_request()
        else:
            return "Please upload a file or paste a YouTube URL", 400
    return render_template_string(AUDIO_HTML)

@app.route('/video', methods=['GET', 'POST'])
def video_page():
    if request.method == 'POST':
        file = request.files.get('file')
        output_format = request.form.get('output_format')
        if not file or not output_format:
            return "Missing file or output format", 400
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        base_name = os.path.splitext(file.filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.{output_format}")
        try:
            convert_v(input_path, output_path)
        except Exception as e:
            return f"Video conversion failed: {e}", 500
        return send_file(output_path, as_attachment=True)
    return render_template_string(VIDEO_HTML)

@app.route('/archive', methods=['GET', 'POST'])
def file_page():
    if request.method == 'POST':
        file = request.files.get('file')
        output_format = request.form.get('output_format')
        if not file or not output_format:
            return "Missing file or output format", 400
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        base_name = os.path.splitext(file.filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.{output_format}")
        try:
            convert_f(input_path, output_path)
        except Exception as e:
            return f"Archive conversion failed: {e}", 500
        return send_file(output_path, as_attachment=True)
    return render_template_string(ARCHIVE_HTML)

@app.route('/presentation', methods=['GET', 'POST'])
def presentation_page():
    if request.method == 'POST':
        file = request.files.get('file')
        output_format = request.form.get('output_format')
        if not file or not output_format:
            return "Missing file or output format", 400
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        base_name = os.path.splitext(file.filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.{output_format}")
        try:
            convert_p(input_path, output_path)
        except Exception as e:
            return f"Presentation conversion failed: {e}", 500
        return send_file(output_path, as_attachment=True)
    return render_template_string(PRESENTATION_HTML)

@app.route('/image', methods=['GET', 'POST'])
def image_page():
    if request.method == 'POST':
        file = request.files.get('file')
        output_format = request.form.get('output_format')
        if not file or not output_format:
            return "Missing file or output format", 400
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        base_name = os.path.splitext(file.filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.{output_format}")
        try:
            convert_i(input_path, output_path)
        except Exception as e:
            return f"Image conversion failed: {e}", 500
        return send_file(output_path, as_attachment=True)
    return render_template_string(IMAGE_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
