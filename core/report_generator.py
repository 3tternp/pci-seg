from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def format_heading(document, text, level=1):
    heading = document.add_heading(text, level=level)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT

def format_paragraph(document, title, content):
    run = document.add_paragraph().add_run(f"{title}: {content}")
    run.font.size = Pt(11)

def generate_vuln_section(document, vuln):
    format_heading(document, vuln.get("issue_name", "Vulnerability"), level=2)
    format_paragraph(document, "Targeted IP", vuln.get("targeted_ip", "N/A"))
    format_paragraph(document, "Source IP", vuln.get("source_ip", "N/A"))
    format_paragraph(document, "Method Used", vuln.get("method_used", "N/A"))
    format_paragraph(document, "Port Used", vuln.get("port_used", "N/A"))
    format_paragraph(document, "Vulnerability Details", vuln.get("vulnerability_details", "N/A"))
    format_paragraph(document, "Attack Vector", vuln.get("attack_vector", "N/A"))
    format_paragraph(document, "Attack Complexity", vuln.get("attack_complexity", "N/A"))
    format_paragraph(document, "Privileges Required", vuln.get("privileges_required", "N/A"))
    format_paragraph(document, "User Interaction", vuln.get("user_interaction", "N/A"))
    format_paragraph(document, "Scope", vuln.get("scope", "N/A"))
    format_paragraph(document, "Confidentiality Impact", vuln.get("confidentiality", "N/A"))
    format_paragraph(document, "Integrity Impact", vuln.get("integrity", "N/A"))
    format_paragraph(document, "Availability Impact", vuln.get("availability", "N/A"))
    format_paragraph(document, "Severity Rating", vuln.get("severity_rating", "N/A"))
    format_paragraph(document, "Business Impact", vuln.get("business_impact", "N/A"))
    format_paragraph(document, "Remediation", vuln.get("remediation", "N/A"))
    format_paragraph(document, "Proof of Concept", vuln.get("proof_of_concept", "N/A"))
    document.add_paragraph("\n")

def report_generator(data, output_path, fmt="docx"):
    """
    Generates a DOCX report.
    
    :param data: A dictionary or list of dictionaries containing vulnerability info.
    :param output_path: Path to save the generated file.
    :param fmt: Format (currently only 'docx' supported).
    """
    if fmt != "docx":
        raise ValueError("Only 'docx' format is supported at the moment.")

    document = Document()
    document.add_heading("Security Assessment Report", level=0)

    if isinstance(data, dict):
        data = [data]  # Wrap in list if it's a single entry

    for vuln in data:
        generate_vuln_section(document, vuln)

    document.save(output_path)
    print(f"[+] Report saved to {output_path}")
