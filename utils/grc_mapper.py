def basic_framework_mapping(industry, region):
    mapping = []

    if "finance" in industry.lower():
        mapping.append("Basel III")
        mapping.append("SOX")

    if "health" in industry.lower():
        mapping.append("HIPAA")

    if "australia" in region.lower():
        mapping.append("APRA CPS 234")
        mapping.append("Privacy Act 1988")

    return mapping
