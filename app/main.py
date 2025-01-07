import streamlit as st
from pdf_handler import extract_pdf_text, input_pdf_setup
from gemini_handler import get_gemini_response
from prompts import INPUT_PROMPT1, INPUT_PROMPT3
import os


# Streamlit app layout
st.title("ATS Resume Tracker")

# Taking Job Description
input_text = st.text_area("Job Description: ", key="input")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(INPUT_PROMPT1, pdf_content, input_text)
            st.subheader("The Response is:")
            st.write(response)
    else:
        st.warning("Please upload a resume.")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(INPUT_PROMPT3, pdf_content, input_text)
            st.subheader("The Response is:")
            st.write(response)
    else:
        st.warning("Please upload a resume.")
