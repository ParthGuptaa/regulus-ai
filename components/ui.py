import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #1f77b4;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
