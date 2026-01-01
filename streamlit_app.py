import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Function to summarize text
def summarize_text(text):
    prompt = f"Summarize this for quick revision:\n{text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="LLM Summarizer", layout="wide")
st.title("LLM Summarizer with Gemini API")
st.write("Paste your text below and get a concise summary for quick revision.")

# Input text box
user_input = st.text_area("Enter text here:", height=300)

# Summarize button
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(user_input)
            st.success("Summary generated!")
            st.text_area("Summary:", value=summary, height=200)
