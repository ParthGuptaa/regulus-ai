from google import genai
import streamlit as st

# Initialize client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # Safe extraction
        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return str(response)

    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"
