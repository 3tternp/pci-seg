# core/report_generator.py
from jinja2 import Template
import json
import pdfkit

def report_generator(scan_data):
    template_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Vulnerability Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f4f4f4;
                font-weight: bold;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .poc {
                white-space: pre-wrap;
                font-family: monospace;
            }

            /* Severity based colors */
            .severity-low {
                background-color: #d9f0d9; /* light green */
            }
            .severity-medium {
                background-color: #fff7cc; /* light yellow */
            }
            .severity-high {
                background-color: #f9d6d5; /* light red */
            }
            .severity-critical {
                background-color: #f28c8c; /* stronger red */
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Vulnerability Report</h1>
        <table>
            <tr><th>Field</th><th>Details</th></tr>
            <tr><td>Affected IP</td><td>{{ scan_data.get('target', 'N/A') }}</td></tr>
            <tr><td>Method Used</td><td>{{ scan_data.get('method', 'Port Scan') }}</td></tr>
            <tr><td>Port Used</td><td>{{ scan_data.get('ports', 'N/A') }}</td></tr>
            <tr class="severity-{{ scan_data.get('severity', 'low').lower() }}"><td>Severity Rating</td><td>{{ scan_data.get('severity', 'Low') }}</td></tr>
            <tr><td>Vulnerability Details</td><td>{{ scan_data.get('vulnerability', 'No specific details') }}</td></tr>
            <tr><td>Attack Vector</td><td>{{ scan_data.get('vector', 'Network') }}</td></tr>
            <tr><td>Attack Complexity</td><td>{{ scan_data.get('complexity', 'Low') }}</td></tr>
            <tr><td>Privileges Required</td><td>{{ scan_data.get('privileges', 'None') }}</td></tr>
            <tr><td>User Interaction</td><td>{{ scan_data.get('interaction', 'None') }}</td></tr>
            <tr><td>Scope</td><td>{{ scan_data.get('scope', 'Unchanged') }}</td></tr>
            <tr><td>Confidentiality</td><td>{{ scan_data.get('confidentiality', 'None') }}</td></tr>
            <tr><td>Integrity</td><td>{{ scan_data.get('integrity', 'None') }}</td></tr>
            <tr><td>Availability</td><td>{{ scan_data.get('availability', 'None') }}</td></tr>
            <tr><td>Business Impact</td><td>{{ scan_data.get('impact', 'Minimal') }}</td></tr>
            <tr><td>Remediation</td><td>{{ scan_data.get('remediation', 'Apply segmentation control') }}</td></tr>
            <tr><td>Explanation of Remediation</td><td>{{ scan_data.get('remediation_explanation', 'Limits lateral movement') }}</td></tr>
            <tr><td>Expected Output After Remediation</td><td>{{ scan_data.get('expected_output', 'Segmented zones') }}</td></tr>
        </table>
    </body>
    </html>
    """
    template = Template(template_str)
    return template.render(scan_data=scan_data)


def report_generator(scan_data, output_path, fmt):
    if fmt == 'json':
        with open(output_path, 'w') as f:
            json.dump(scan_data, f, indent=2)
        print(f"[+] JSON report saved to: {output_path}")
        return

    elif fmt == 'html':
        html_content = generate_html_report(scan_data)
        with open(output_path, 'w') as f:
            f.write(html_content)
        print(f"[+] HTML report saved to: {output_path}")
        return

    elif fmt == 'pdf':
        html_content = generate_html_report(scan_data)
        # NOTE: wkhtmltopdf must be installed manually by the user for this to work
        pdfkit.from_string(html_content, output_path)
        print(f"[+] PDF report saved to: {output_path}")
        return

    else:
        raise ValueError(f"Unsupported report format: {fmt}")

