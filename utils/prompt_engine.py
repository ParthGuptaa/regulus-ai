def build_grc_prompt(industry, region, work_type, extra_context, web_data):
    return f"""
You are an expert in Governance, Risk, and Compliance (GRC).

Context:
- Industry: {industry}
- Region: {region}
- Nature of Work: {work_type}
- Additional Context: {extra_context}

External Insights:
{web_data}

Tasks:
1. Identify relevant regulatory frameworks
2. Identify applicable security standards
3. Define GRC controls and compliance requirements

For each item include:
- Explanation (why relevant)
- Source reference (if available)
- Confidence Score (High/Medium/Low)

Also:
- Highlight recent regulatory updates
- Keep response structured and concise
"""
