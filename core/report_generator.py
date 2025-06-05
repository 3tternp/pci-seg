from docx import Document
import json
from jinja2 import Template
import os

def report_generator(scan_data, output_path, fmt='html'):
    if fmt == 'json':
        with open(output_path, 'w') as f:
            json.dump(scan_data, f, indent=2)
        return

    elif fmt == 'html':
        generate_html_report(scan_data, output_path)
        return

    elif fmt == 'docx':
        generate_docx_report(scan_data, output_path)
        return

    else:
        raise ValueError("Unsupported report format. Use html, json, or docx.")


def generate_html_report(scan_data, output_path):
    template_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Vulnerability Report</title>
        <style>
            body { font-family: Arial; padding: 30px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 10px; }
            th { background-color: #eee; }
        </style>
    </head>
    <body>
        <h2>Vulnerability Report</h2>
        <table>
            {% for key, value in scan_data.items() %}
            <tr>
                <th>{{ key.replace("_", " ").title() }}</th>
                <td>{{ value }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    template = Template(template_str)
    rendered_html = template.render(scan_data=scan_data)
    with open(output_path, 'w') as f:
        f.write(rendered_html)


def generate_docx_report(scan_data, output_path):
    doc = Document()
    doc.add_heading("Vulnerability Report", 0)

    # Add table
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Field'
    hdr_cells[1].text = 'Details'

    for field in [
        'Issue Name', 'Targeted IP', 'Source IP', 'Method used', 'Port Used',
        'Vulnerability details', 'Attack Vector', 'Attack Complexity',
        'Privileges Required', 'User Interaction', 'Scope',
        'Confidentiality', 'Integrity', 'Availability', 'Severity-Rating',
        'Business impact', 'Remediation', 'Proof of Concept'
    ]:
        value = scan_data.get(field.lower().replace(" ", "_"), 'N/A')
        row_cells = table.add_row().cells
        row_cells[0].text = field
        row_cells[1].text = str(value)

    doc.save(output_path)
