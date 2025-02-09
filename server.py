import os
from flask import Flask, request, jsonify, send_file
from summarizer import summarize_text
from pdf_generator import generate_pdf
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

UPLOAD_FOLDER = "generated_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    email = data.get('email', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    summary = summarize_text(text)  # Call LLM API
    pdf_path = generate_pdf(summary)

    if email:
        send_email(email, pdf_path)
        return jsonify({'message': 'PDF emailed successfully'})

    return jsonify({'pdf_url': f'http://127.0.0.1:5000/download/{pdf_path}'})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

def send_email(to_email, file_path):
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = "Your Summarized Study Notes"

    attachment = open(file_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
    msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, msg.as_string())
    server.quit()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
