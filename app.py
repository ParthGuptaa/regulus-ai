import streamlit as st
from utils.gemini_client import generate_response
from utils.tavily_client import search_web
from utils.prompt_engine import build_grc_prompt
from utils.grc_mapper import basic_framework_mapping

st.set_page_config(page_title="Regulus AI", layout="wide")

# Simple clean styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Regulus AI")
st.caption("GRC Intelligence • Grounded in Trust")

# Inputs
col1, col2 = st.columns(2)

with col1:
    industry = st.text_input("Industry")

with col2:
    region = st.text_input("Region")

work_type = st.text_area("Nature of Work")
extra_context = st.text_area("Additional Context")

if st.button("Run GRC Analysis"):

    if not industry or not region:
        st.warning("Please fill Industry and Region")
        st.stop()

    with st.spinner("Analyzing..."):

        # Step 1: Base mapping
        frameworks = basic_framework_mapping(industry, region)

        # Step 2: Tavily search
        query = f"{industry} regulations {region} compliance requirements"
        web_results = search_web(query)

        web_text = "\n".join([
            r.get("content", "") for r in web_results[:3]
        ])

        # Step 3: Prompt
        prompt = build_grc_prompt(
            industry,
            region,
            work_type,
            extra_context,
            web_text
        )

        # Step 4: Gemini
        result = generate_response(prompt)

    # Output
    st.markdown("## 📊 GRC Analysis")
    st.write(result)

    st.markdown("## 📚 Base Framework Suggestions")
    for f in frameworks:
        st.markdown(f"- {f}")
