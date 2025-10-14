ReadMe instruction for Convertor.

# Code review

## 🏠 1. Main Entry Point (main.py / app.py)
This is the core controller of the application.
It:
- Detects uploaded file type (by extension or content signature).
- Dynamically loads the appropriate converter (e.g., document, audio, image).
- Runs the correct conversion function.
- Returns or saves the converted file.
- Connects directly to all converter branches.
 ------------------------------------------------------------------------------------------- 
## 📄 2. Document Converter Branch
Handles conversions between text-based and structured document formats:
- PDF ↔ DOCX / TXT / HTML / ODT
- DOCX ↔ PDF / TXT / HTML / ODT
- ODT ↔ PDF / DOCX / TXT
- HTML ↔ PDF / DOCX / TXT
- TXT ↔ PDF / DOCX / CSV
- CSV ↔ XLSX / TXT / PDF
Uses libraries like python-docx, pdfkit, pdfplumber, docx2pdf, openpyxl, and pandas.
 ------------------------------------------------------------------------------------------- 
## 🎵 3. Audio & YouTube Converter Branch
Allows uploading audio files or providing a YouTube URL.
Converts between:
- MP3 ↔ WAV ↔ MP4 (audio track)
- YouTube URL → MP3 / WAV / MP4
- Uses yt-dlp for downloading and pydub for conversion.
- Communicates with the main controller through form submission.
---------------------------------------------------------------------------------------------
Communicates with the main controller through form submission.
## 🎬 4. Video Converter Branch
Handles direct video file uploads or YouTube video URLs.
Converts between major formats:
- MP4, MOV, MKV, AVI, FLV, WEBM
- Uses opencv-python-headless or ffmpeg (if available) for format transformations.
- Shares download logic with the audio converter.
---------------------------------------------------------------------------------------------
## 🗜️ 5. Archive Converter Branch
Manages compressed file formats:
- ZIP ↔ RAR ↔ 7Z
Uses py7zr, rarfile, and Python’s built-in zipfile for extraction and repackaging.
Ensures integrity and prevents nested archive corruption.
Connected to main UI through /archive route.
---------------------------------------------------------------------------------------------
## 📊 6. Presentation Converter Branch
Converts between presentation formats:
- PPTX ↔ ODP ↔ KEY
Uses python-pptx or CairoSVG (for slides to images/PDF).
Integrated in /presentation route.
---------------------------------------------------------------------------------------------
## 🖼️ 7. Image Converter Branch
Converts between image formats:
- JPG / JPEG ↔ PNG ↔ GIF ↔ TIFF ↔ WEBP ↔ BMP
Uses Pillow, imageio, tifffile, and CairoSVG for rendering and format conversion.
Linked with /image route in the Flask app.
---------------------------------------------------------------------------------------------
## 💡 8. HTML Interface Templates
Each converter type has a dedicated HTML page:
- /doc, /audio, /video, /archive, /presentation, /image
Each form allows file upload and target format selection.
All templates are connected to the Flask routes in the main file.
---------------------------------------------------------------------------------------------
## ⚙️ 9. Utility Modules
Common helper scripts:
- file_detector.py → Determines file type.
- helpers.py → Handles naming, pathing, and saving outputs.
- converter_map.py → Stores valid conversion routes.
Shared across all branches.
---------------------------------------------------------------------------------------------
## 🔗 10. Interconnection Summary
Main.py / app.py acts as the central brain.
Each branch (document, audio, image, etc.) is a specialized module.
They’re connected via:
Flask routing (for web app) or
Direct function calls (for local desktop mode).
All results are unified under a consistent output manager that saves converted files and returns status messages.
---------------------------------------------------------------------------------------------
# Convertation list:

## 📄 Document Conversions
From .pdf
→ .docx
→ .txt
→ .html
→ .csv
→ .odt

From .doc / .docx
→ .pdf
→ .txt
→ .html
→ .odt

From .odt
→ .pdf
→ .docx
→ .txt

From .html / .htm
→ .pdf
→ .docx
→ .txt

From .xls / .xlsx
→ .csv
→ .txt
→ .pdf

From .txt
→ .pdf
→ .docx
→ .csv

From .csv
→ .xlsx
→ .txt
→ .pdf
---------------------------------------------------------------------------------------------
## 🎵 Audio Conversions
From .mp3
→ .wav
→ .mp4

From .wav
→ .mp3
→ .mp4

From YouTube URL
→ .mp3
→ .wav
→ .mp4
---------------------------------------------------------------------------------------------
## 🎬 Video Conversions
From .mp4
→ .mov
→ .mkv
→ .avi
→ .flv
→ .webm

From .mov
→ .mp4
→ .mkv
→ .avi
→ .flv
→ .webm

From .mkv
→ .mp4
→ .mov
→ .avi
→ .flv
→ .webm

From .avi
→ .mp4
→ .mov
→ .mkv
→ .flv
→ .webm

From .flv
→ .mp4
→ .mov
→ .mkv
→ .avi
→ .webm

From .webm
→ .mp4
→ .mov
→ .mkv
→ .avi
→ .flv

From YouTube URL
→ .mp4
→ .mov
→ .mkv
→ .avi
→ .flv
→ .webm
---------------------------------------------------------------------------------------------
## 🖼️ Image Conversions
From .jpg / .jpeg
→ .png
→ .gif
→ .tiff
→ .bmp
→ .webp

From .png
→ .jpg / .jpeg
→ .gif
→ .tiff
→ .bmp
→ .webp

From .gif
→ .jpg / .jpeg
→ .png
→ .tiff
→ .bmp
→ .webp

From .tiff / .tif
→ .jpg / .jpeg
→ .png
→ .gif
→ .bmp
→ .webp

From .bmp
→ .jpg / .jpeg
→ .png
→ .gif
→ .tiff
→ .webp

From .webp
→ .jpg / .jpeg
→ .png
→ .gif
→ .tiff
→ .bmp
---------------------------------------------------------------------------------------------
## 📊 Presentation Conversions
From .ppt / .pptx
→ .odp
→ .key
→ .pdf

From .odp
→ .pptx
→ .key
→ .pdf

From .key
→ .pptx
→ .odp
→ .pdf
---------------------------------------------------------------------------------------------
## 🗜️ Archive Conversions
From .zip
→ .rar
→ .7z

From .rar
→ .zip
→ .7z

From .7z
→ .zip
→ .rar
---------------------------------------------------------------------------------------------
## 🧷 Special Conversions (Cross-Type / Mixed)
Input    Output    Description
.pdf    .jpg / .png    Converts PDF pages to images (optional extension)
.jpg / .png    .pdf    Converts image to a single-page PDF
.mp4    .mp3 / .wav    Extracts audio from video
YouTube URL    .mp3, .wav, .mp4, .webm    Direct download and conversion


# Running guidance (via terminal) by steps:

## 1) Write "venv\Scripts\activate"
![13 10 2025_17 34 52_REC](https://github.com/user-attachments/assets/bb9c10b8-c4ff-4d78-ac3f-6c22e7db3545)

## 2) Write "python app.py"
![13 10 2025_17 35 34_REC](https://github.com/user-attachments/assets/26831339-cb15-48aa-a969-d7344de7aedb)

## 3) Choose one of the proposed hosts. Copy that link and paste it into address bar (URL)
![13 10 2025_17 36 15_REC](https://github.com/user-attachments/assets/f480b7c2-3a2a-4c9f-8ffc-aa627e8a44b8)

## 4) Choose prefered convertor and make convertations!
![13 10 2025_17 37 07_REC](https://github.com/user-attachments/assets/8a0dfb07-f0d7-4809-b7c2-ed87d41a39a3)

## (Optional) 5) Enjpy the programme!


# 📦 Total List of required Python libraries: 41

- blinker
- click
- colorama
- docx2pdf
- et_xmlfile
- fire
- Flask
- fonttools
- itsdangerous
- Jinja2
- lxml
- MarkupSafe
- numpy
- opencv-python-headless
- openpyxl
- pandas
- pdfkit
- PyMuPDF
- python-dateutil
- python-docx
- pytz
- pywin32
- six
- termcolor
- tqdm
- typing_extensions
- tzdata
- Werkzeug
- xlrd
- pdf2docx
- pdfplumber
- beautifulsoup4
- pydub
- yt-dlp
- pdfminer.six
- py7zr
- rarfile
- Pillow
- CairoSVG
- imageio
- tifffile
  
---

# This code required for Python 3.10+ version
