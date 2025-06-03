
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_report(scan_data, ai_text, output_path, fmt):
    Path("reports").mkdir(exist_ok=True)
    if fmt == "json":
        with open(output_path, 'w') as f:
            json.dump({"scan_data": scan_data, "ai_analysis": ai_text}, f, indent=2)
    elif fmt == "html":
        env = Environment(loader=FileSystemLoader("core"))
        template = env.get_template("report_template.html")
        html = template.render(scan_data=scan_data, ai_analysis=ai_text)
        with open(output_path, "w") as f:
            f.write(html)
