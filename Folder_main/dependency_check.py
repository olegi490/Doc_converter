import shutil
import sys
import os

LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
WINRAR_PATH = r"C:\Program Files\WinRAR\Rar.exe"

def check_dependency(path, friendly_name, install_url=None):
    if not os.path.isfile(path):
        print(f"[ERROR] {friendly_name} is not installed or not found at:")
        print(f"  {path}")
        print(f"Please install {friendly_name} before running this program.")
        if install_url:
            print(f"Download: {install_url}")
        sys.exit(1)

def check_all_dependencies():
    # LibreOffice check
    check_dependency(
        LIBREOFFICE_PATH,
        'LibreOffice',
        'https://www.libreoffice.org/download/download-libreoffice/'
    )

    # wkhtmltopdf check
    check_dependency(
        WKHTMLTOPDF_PATH,
        'wkhtmltopdf',
        'https://wkhtmltopdf.org/downloads.html'
    )

    # WinRAR check
    check_dependency(
        WINRAR_PATH,
        'WinRAR',
        'https://www.win-rar.com/download.html'
    )
