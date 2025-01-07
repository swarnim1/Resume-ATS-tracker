from PyPDF2 import PdfReader
import streamlit as st

def extract_pdf_text(file):
    """Extract text from a PDF file."""
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def input_pdf_setup(uploaded_file):
    """Handles the PDF upload and extraction process."""
    if uploaded_file:
        st.write("PDF Uploaded Successfully.")
        try:
            # Extract and return PDF content
            pdf_text = extract_pdf_text(uploaded_file)
            return pdf_text
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please upload a PDF file.")
    return None
