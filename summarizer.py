import google.generativeai as genai
import os

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

def summarize_text(text):
    """Uses Google Gemini AI to summarize text into study notes."""
    model = genai.GenerativeModel("gemini-pro")  

    response = model.generate_content(f"Summarize this text into concise study notes with bullet points:\n{text}")
    
    return response.text if response.text else "Error generating summary"
