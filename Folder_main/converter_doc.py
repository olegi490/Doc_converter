import os
import logging
import pandas as pd
from pdfminer.high_level import extract_text

LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

# PDF
from Folder_doc.pdf_conv import (
    convert_pdf_to_doc, 
    convert_pdf_to_docx, 
    convert_pdf_to_txt, 
    convert_pdf_to_html, 
    convert_pdf_to_csv
)

# DOCX
from Folder_doc.docx_conv import (
    convert_docx_to_pdf,
    convert_docx_to_txt,
    convert_docx_to_html,
    convert_docx_to_odt,
    convert_docx_to_doc,
    convert_docx_to_csv
)

# DOC
from Folder_doc.doc_conv import (
    convert_doc_to_docx,
    convert_doc_to_pdf,
    convert_doc_to_txt,
    convert_doc_to_html,
    convert_doc_to_odt,
    convert_doc_to_csv
)

# ODT
from Folder_doc.odt_conv import (
    convert_odt_to_pdf,
    convert_odt_to_docx,
    convert_odt_to_txt,
    convert_odt_to_html,
    convert_odt_to_doc
)

# HTML
from Folder_doc.html_conv import (
    convert_html_to_docx, 
    convert_html_to_pdf, 
    convert_html_to_odt, 
    convert_html_to_txt
)

# XLS
from Folder_doc.xls_conv import (
    convert_xls_to_csv, 
    convert_xls_to_pdf, 
    convert_xls_to_html
)
from Folder_doc.xlsx_conv import (
    convert_xlsx_to_csv, 
    convert_xlsx_to_pdf, 
    convert_xlsx_to_html
)

# TXT
from Folder_doc.txt_conv import (
    convert_txt_to_csv,
    convert_txt_to_pdf,
    convert_txt_to_docx
)

# CSV
from Folder_doc.csv_conv import (
    convert_csv_to_txt,
    convert_csv_to_xlsx, 
    convert_csv_to_xls,
    convert_csv_to_pdf
)

SUPPORTED = {
    'pdf', 'doc', 'docx', 'odt', 'html', 'xls', 'xlsx', 'txt', 'csv'
}

conversion_options = {
    '.pdf': ['.doc', '.docx', '.txt', '.html', '.csv'], #yes
    '.docx': ['.pdf', '.txt', '.html', '.odt', '.doc', '.csv'], #pdf , doc
    '.doc': ['.pdf', '.txt', '.html', '.odt', '.docx', '.csv'], # yes
    '.odt': ['.pdf', '.docx', '.doc', '.txt', '.html'], # pdf, doc,
    '.html': ['.pdf', '.docx', '.odt', '.txt'], # pdf
    '.htm': ['.pdf', '.docx', '.odt', '.txt'],
    '.xls': ['.csv', '.pdf', '.html'],  
    '.xlsx': ['.csv', '.pdf', '.html'], # csv pdf
    '.txt': ['.pdf', '.docx', '.csv'], #pdf
    '.csv': ['.xlsx', '.xls', '.pdf', '.txt'], # xls, pdf
}

ext_to_name = {
    '.pdf': 'PDF',
    '.docx': 'DOCX',
    '.doc': 'DOC',
    '.odt': 'ODT',
    '.html': 'HTML',
    '.htm': 'HTML',
    '.xls': 'XLS',
    '.xlsx': 'XLSX',
    '.txt': 'TXT',
    '.csv': 'CSV',
}

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

def detect_format(path):
    ext = os.path.splitext(path)[1].lower().strip('.')
    if ext == 'htm':
        ext = 'html'
    return ext

def validate_format(fmt):
    if fmt not in SUPPORTED:
        raise ValueError(f"Unsupported file format: '{fmt}'")

def convert(input_path, output_path):
    logging.info(f"Starting conversion: {input_path} -> {output_path}")
    inp = detect_format(input_path)
    out = detect_format(output_path)

    validate_format(inp)
    validate_format(out)

    if inp == out:
        raise ValueError("Input and output formats are identical.")

    mapping = {
        # PDF
        ('pdf', 'doc'): convert_pdf_to_doc,
        ('pdf', 'docx'): convert_pdf_to_docx,
        ('pdf', 'txt'): convert_pdf_to_txt,
        ('pdf', 'html'): convert_pdf_to_html,
        ('pdf', 'csv'): convert_pdf_to_csv,

        # DOC
        ('doc', 'docx'): convert_doc_to_docx,
        ('doc', 'pdf'): convert_doc_to_pdf,
        ('doc', 'txt'): convert_doc_to_txt,
        ('doc', 'html'): convert_doc_to_html,
        ('doc', 'odt'): convert_doc_to_odt,
        ('doc', 'csv'): convert_doc_to_csv,

        # DOCX
        ('docx', 'doc'): convert_docx_to_doc,
        ('docx', 'pdf'): convert_docx_to_pdf,
        ('docx', 'txt'): convert_docx_to_txt,
        ('docx', 'html'): convert_docx_to_html,
        ('docx', 'odt'): convert_docx_to_odt,
        ('docx', 'csv'): convert_docx_to_csv,

        # ODT
        ('odt', 'pdf'): convert_odt_to_pdf,
        ('odt', 'docx'): convert_odt_to_docx,
        ('odt', 'doc'): convert_odt_to_doc,
        ('odt', 'txt'): convert_odt_to_txt,
        ('odt', 'html'): convert_odt_to_html,

        # HTML
        ('html', 'pdf'): convert_html_to_pdf,
        ('html', 'docx'): convert_html_to_docx,
        ('html', 'odt'): convert_html_to_odt,
        ('html', 'txt'): convert_html_to_txt,

        # Excel
        ('xls', 'csv'): convert_xls_to_csv,
        ('xls', 'pdf'): convert_xls_to_pdf,
        ('xls', 'html'): convert_xls_to_html,

        ('xlsx', 'csv'): convert_xlsx_to_csv,
        ('xlsx', 'pdf'): convert_xlsx_to_pdf,
        ('xlsx', 'html'): convert_xlsx_to_html,

        # TXT
        ('txt', 'pdf'): convert_txt_to_pdf, 
        ('txt', 'docx'): convert_txt_to_docx,
        ('txt', 'csv'): convert_txt_to_csv,

        # CSV
        ('csv', 'xls'): convert_csv_to_xls,
        ('csv', 'xlsx'): convert_csv_to_xlsx,
        ('csv', 'pdf'): lambda i, o: (convert_csv_to_xlsx(i, '_tmp.xlsx') or convert_xlsx_to_pdf('_tmp.xlsx', o)),
        ('csv', 'txt'): convert_csv_to_txt,
    }

    func = mapping.get((inp, out))
    if not func:
        raise NotImplementedError(f"Conversion {inp} → {out} not supported yet.")

    try:
        func(input_path, output_path)
        logging.info(f"Conversion successful: {input_path} → {output_path}")
    except Exception as e:
        logging.error(f"Conversion failed: {e}")
        raise
