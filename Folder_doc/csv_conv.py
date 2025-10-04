import os
import pandas as pd
from fpdf import FPDF

def convert_csv_to_xlsx(input_csv, output_xlsx):
    if not os.path.exists(input_csv):
        print("CSV file not found.")
        return

    try:
        df = pd.read_csv(input_csv)
        df.to_excel(output_xlsx, index=False, engine='openpyxl')
        print(f"Converted CSV to XLSX: {output_xlsx}")
    except Exception as e:
        print(f"Error converting CSV to XLSX: {e}")

def convert_csv_to_xls(input_csv, output_xls):
    if not os.path.exists(input_csv):
        print("CSV file not found.")
        return

    try:
        df = pd.read_csv(input_csv)
        df.to_excel(output_xls, index=False, engine='xlwt')  # xlwt supports XLS
        print(f"Converted CSV to XLS: {output_xls}")
    except Exception as e:
        print(f"Error converting CSV to XLS: {e}")

def convert_csv_to_pdf(input_csv, output_pdf):
    if not os.path.exists(input_csv):
        print("CSV file not found.")
        return

    try:
        df = pd.read_csv(input_csv)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_width = pdf.w / (len(df.columns) + 1)
        row_height = pdf.font_size * 1.5

        # Header
        for col in df.columns:
            pdf.cell(col_width, row_height, str(col), border=1)
        pdf.ln(row_height)

        # Rows
        for i in range(len(df)):
            for col in df.columns:
                text = str(df.at[i, col])
                pdf.cell(col_width, row_height, text, border=1)
            pdf.ln(row_height)

        pdf.output(output_pdf)
        print(f"Converted CSV to PDF: {output_pdf}")

    except Exception as e:
        print(f"Error converting CSV to PDF: {e}")

def convert_csv_to_txt(input_csv, output_txt, delimiter=','):
    if not os.path.exists(input_csv):
        print("CSV file not found.")
        return

    try:
        with open(input_csv, 'r', encoding='utf-8') as f_in, open(output_txt, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                f_out.write(line)
        print(f"Converted CSV to TXT: {output_txt}")
    except Exception as e:
        print(f"Error converting CSV to TXT: {e}")
