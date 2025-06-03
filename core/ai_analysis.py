
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def analyze_segmentation_results(scan_data):
    prompt = f"""
    You are a PCI DSS segmentation testing expert. Analyze the following scan results
    for any segmentation violations between CDE and non-CDE systems.
    Provide:
    1. Summary of findings
    2. PCI DSS requirement mapping
    3. Risk rating
    4. Recommendations

    Scan Results:
    {scan_data}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a PCI DSS segmentation auditing expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
