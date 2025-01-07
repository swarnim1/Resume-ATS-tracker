import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt, pdf_content, job_description):
    """Generates a response using the Gemini API."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, pdf_content, job_description])
    return response.text
