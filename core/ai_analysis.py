import openai

def analyze_segmentation_results(scan_data, api_key):
    openai.api_key = api_key
    prompt = f"Analyze the following PCI DSS segmentation scan results and provide recommendations:\n{scan_data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
