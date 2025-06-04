from jinja2 import Template
import json
import os

# Optional: choose between pdfkit or weasyprint
USE_PDFKIT = True  # Set False to use WeasyPrint instead

def report_generator(scan_data, output_path, fmt):
    severity = scan_data.get('severity', 'Low').lower()

    severity_class = {
        'critical': 'critical',
        'high': 'high',
        'medium': 'medium',
        'low': 'low',
    }.get(severity, 'low')

    template_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Vulnerability Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { text-align: center; color: #333; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
            th { background-color: #f4f4f4; }
            tr.low { background-color: #d4edda; }      /* Green */
            tr.medium { background-color: #fff3cd; }   /* Yellow */
            tr.high { background-color: #f8d7da; }     /* Red */
            tr.critical { background-color: #721c24; color: white; } /* Dark Red */
        </style>
    </head>
    <body>
        <h1>Vulnerability Report</h1>
        <table>
            <tr><th>Field</th><th>Details</th></tr>
            {% for key, value in scan_data.items() %}
                {% if key != 'severity' %}
                <tr class="{{ severity_class }}"><td>{{ key.replace('_', ' ').title() }}</td><td>{{ value }}</td></tr>
                {% endif %}
            {% endfor %}
            <tr class="{{ severity_class }}"><td>Severity</td><td>{{ scan_data.get('severity', 'Low') }}</td></tr>
        </table>
    </body>
    </html>
    """

    template = Template(template_str)
    rendered_html = template.render(scan_data=scan_data, severity_class=severity_class)

    if fmt == 'html':
        with open(output_path, 'w') as f:
            f.write(rendered_html)
    elif fmt == 'pdf':
        html_file = output_path.replace('.pdf', '.html')
        with open(html_file, 'w') as f:
            f.write(rendered_html)

        if USE_PDFKIT:
            import pdfkit
            pdfkit.from_file(html_file, output_path)
        else:
            from weasyprint import HTML
            HTML(html_file).write_pdf(output_path)

        os.remove(html_file)
    else:
        with open(output_path, 'w') as f:
            json.dump({"scan_data": scan_data}, f, indent=2)

