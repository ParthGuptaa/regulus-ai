import streamlit as st
from utils.gemini_client import generate_response
from utils.tavily_client import search_web
from utils.prompt_engine import build_grc_prompt
from utils.grc_mapper import basic_framework_mapping
from components.ui import apply_custom_css

st.set_page_config(page_title="Regulus AI", layout="wide")

apply_custom_css()

st.title("🛡️ Regulus AI")
st.subheader("GRC Intelligence. Grounded in Trust.")

# Inputs
industry = st.text_input("Industry")
region = st.text_input("Region")
work_type = st.text_area("Nature of Work")
extra_context = st.text_area("Additional Context")

if st.button("Analyze"):
    with st.spinner("Analyzing compliance landscape..."):

        # Step 1: Basic mapping
        frameworks = basic_framework_mapping(industry, region)

        # Step 2: Tavily search
        search_query = f"{industry} regulations {region} compliance requirements"
        web_results = search_web(search_query)

        web_text = "\n".join([r["content"] for r in web_results[:3]])

        # Step 3: Prompt
        prompt = build_grc_prompt(
            industry,
            region,
            work_type,
            extra_context,
            web_text
        )

        # Step 4: Gemini Response
        result = generate_response(prompt)

        # Output
        st.markdown("### 📊 GRC Analysis")
        st.write(result)

        st.markdown("### 📚 Suggested Frameworks (Base Mapping)")
        for f in frameworks:
            st.write(f"- {f}")
