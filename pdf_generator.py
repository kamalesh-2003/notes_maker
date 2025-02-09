from fpdf import FPDF
import os

UPLOAD_FOLDER = "generated_pdfs"

def generate_pdf(summary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, summary)

    filename = "summary_notes.pdf"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    pdf.output(filepath)

    return filename
