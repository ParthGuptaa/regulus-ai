def build_grc_prompt(industry, region, work_type, extra_context, web_data):
    return f"""
You are a Governance, Risk, and Compliance (GRC) expert AI.

Context:
Industry: {industry}
Region: {region}
Nature of Work: {work_type}
Additional Context: {extra_context}

External Data:
{web_data}

Tasks:
1. Identify relevant regulatory frameworks
2. Identify applicable security standards
3. Define GRC controls and compliance requirements

For each output include:
- Explanation (why relevant)
- Source reference (if available)
- Confidence score (High/Medium/Low)

Also:
- Highlight latest regulatory updates
- Keep output structured and audit-ready
"""
