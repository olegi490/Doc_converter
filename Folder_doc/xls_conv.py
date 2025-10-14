import os
import pandas as pd
from fpdf import FPDF

def convert_xls_to_csv(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLS file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='xlrd') 
        df.to_csv(output_path, index=False)
        print(f"Converted XLS to CSV: {output_path}")
    except Exception as e:
        print(f"Error converting XLS to CSV: {e}")

def convert_xls_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLS file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='xlrd')
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_width = pdf.w / (len(df.columns) + 1)
        row_height = pdf.font_size * 1.5

        # header
        for col in df.columns:
            pdf.cell(col_width, row_height, str(col), border=1)
        pdf.ln(row_height)

        # rows
        for _, row in df.iterrows():
            for val in row:
                pdf.cell(col_width, row_height, str(val), border=1)
            pdf.ln(row_height)

        pdf.output(output_path)
        print(f"Converted XLS to PDF: {output_path}")
    except Exception as e:
        print(f"Error converting XLS to PDF: {e}")

def convert_xls_to_html(input_path, output_path):
    if not os.path.exists(input_path):
        print("XLS file not found.")
        return

    try:
        df = pd.read_excel(input_path, engine='xlrd') 
        html_table = df.to_html(index=False)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_table)

        print(f"Converted XLS to HTML: {output_path}")
    except Exception as e:
        print(f"Error converting XLS to HTML: {e}")
