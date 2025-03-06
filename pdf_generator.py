from fpdf import FPDF
import os

UPLOAD_FOLDER = "generated_pdfs"

def generate_pdf(summary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set default Arial font
    pdf.set_font("Arial", size=12)

    # Ensure UTF-8 encoding and handle special characters safely
    pdf.multi_cell(0, 10, summary.encode("latin1", "replace").decode("latin1"))

    # Ensure the output directory exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Define output file path
    filename = "summary_notes.pdf"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    pdf.output(filepath)

    # Return's the filename
    return filename
