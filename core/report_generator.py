import json
from jinja2 import Template

def generate_report(scan_data, ai_result, output_path, fmt):
    if fmt == 'json':
        with open(output_path, 'w') as f:
            json.dump({'scan': scan_data, 'ai': ai_result}, f, indent=4)
    elif fmt == 'html':
        html_template = Template("""
        <html><body>
        <h1>PCI Segmentation Report</h1>
        <h2>Scan Results</h2><pre>{{ scan }}</pre>
        <h2>AI Analysis</h2><pre>{{ ai }}</pre>
        </body></html>
        """)
        with open(output_path, 'w') as f:
            f.write(html_template.render(scan=json.dumps(scan_data, indent=2), ai=ai_result))
