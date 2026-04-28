def basic_framework_mapping(industry, region):
    industry = industry.lower()
    region = region.lower()

    mapping = []

    if "finance" in industry:
        mapping += ["Basel III", "SOX"]

    if "health" in industry:
        mapping += ["HIPAA"]

    if "australia" in region:
        mapping += ["APRA CPS 234", "Privacy Act 1988"]

    return mapping
