import os
import pandas as pd
from fpdf import FPDF

def convert_xlsx_to_csv(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLSX file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='openpyxl') 
        df.to_csv(output_path, index=False)
        print(f"Converted XLSX to CSV: {output_path}")
    except Exception as e:
        print(f"Error converting XLSX to CSV: {e}")

def convert_xlsx_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLSX file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='openpyxl') 

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_width = pdf.w / (len(df.columns) + 1)
        row_height = pdf.font_size * 1.5

        # Header
        for col in df.columns:
            pdf.cell(col_width, row_height, str(col), border=1)
        pdf.ln(row_height)

        # ows
        for _, row in df.iterrows():
            for val in row:
                pdf.cell(col_width, row_height, str(val), border=1)
            pdf.ln(row_height)

        pdf.output(output_path)
        print(f"Converted XLSX to PDF: {output_path}")
    except Exception as e:
        print(f"Error converting XLSX to PDF: {e}")

def convert_xlsx_to_html(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLSX file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='openpyxl')
        html_table = df.to_html(index=False)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_table)

        print(f"Converted XLSX to HTML: {output_path}")
    except Exception as e:
        print(f"Error converting XLSX to HTML: {e}")
