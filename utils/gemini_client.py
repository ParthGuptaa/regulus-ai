from google import genai
import streamlit as st

# Initialize client using Streamlit secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"
