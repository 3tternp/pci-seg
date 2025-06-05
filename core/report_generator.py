from docx import Document
from docx.shared import Inches
import json
import os

def report_generator(scan_result, ai_result, output_path, report_format):
    if report_format == "docx":
        generate_docx_report(scan_result, ai_result, output_path)
    elif report_format == "html":
        generate_html_report(scan_result, ai_result, output_path)
    elif report_format == "json":
        generate_json_report(scan_result, ai_result, output_path)
    elif report_format == "pdf":
        generate_pdf_report(scan_result, ai_result, output_path)
    else:
        raise ValueError(f"Unsupported report format: {report_format}")

def generate_docx_report(scan_result, ai_result, output_path):
    doc = Document()
    doc.add_heading("PCI Recon Scan Report", 0)

    # Add scan summary
    doc.add_heading("Scan Summary", level=1)
    doc.add_paragraph(f"Target IP: {scan_result.get('target_ip', 'Unknown')}")
    doc.add_paragraph(f"Source IP: {scan_result.get('source_ip', 'Unknown')}")
    doc.add_paragraph(f"Scan Profile: {scan_result.get('profile', 'pci-core')}")

    # Add vulnerabilities section
    doc.add_heading("Vulnerabilities", level=1)
    vulnerabilities = scan_result.get('vulnerabilities', [])

    for vuln in vulnerabilities:
        doc.add_heading(f"Issue: {vuln.get('issue_name', 'Unknown')}", level=2)
        doc.add_paragraph(f"Targeted IP: {vuln.get('target_ip', scan_result.get('target_ip', 'Unknown'))}")
        doc.add_paragraph(f"Source IP: {vuln.get('source_ip', scan_result.get('source_ip', 'Unknown'))}")
        doc.add_paragraph(f"Method Used: {vuln.get('method', 'Unknown')}")
        doc.add_paragraph(f"Port Used: {vuln.get('port', 'Unknown')}")
        doc.add_paragraph(f"Vulnerability Details: {vuln.get('details', 'No details provided')}")
        doc.add_paragraph(f"Attack Vector: {vuln.get('attack_vector', 'Unknown')}")
        doc.add_paragraph(f"Attack Complexity: {vuln.get('attack_complexity', 'Unknown')}")
        doc.add_paragraph(f"Privileges Required: {vuln.get('privileges_required', 'Unknown')}")
        doc.add_paragraph(f"User Interaction: {vuln.get('user_interaction', 'Unknown')}")
        doc.add_paragraph(f"Scope: {vuln.get('scope', 'Unknown')}")
        doc.add_paragraph(f"Confidentiality: {vuln.get('confidentiality', 'Unknown')}")
        doc.add_paragraph(f"Integrity: {vuln.get('integrity', 'Unknown')}")
        doc.add_paragraph(f"Availability: {vuln.get('availability', 'Unknown')}")
        doc.add_paragraph(f"Severity Rating: {vuln.get('severity_rating', 'Unknown')}")
        doc.add_paragraph(f"Business Impact: {vuln.get('business_impact', 'No impact provided')}")
        doc.add_paragraph(f"Remediation: {vuln.get('remediation', 'No remediation provided')}")
        doc.add_paragraph(f"Proof of Concept: {vuln.get('proof_of_concept', 'No PoC provided')}")
        doc.add_paragraph("-" * 50)

    # Save the document
    doc.save(output_path)

def generate_html_report(scan_result, ai_result, output_path):
    # Placeholder for existing HTML report generation
    with open(output_path, 'w') as f:
        f.write("<html><body><h1>PCI Recon Scan Report</h1><p>HTML report placeholder</p></body></html>")

def generate_json_report(scan_result, ai_result, output_path):
    # Placeholder for existing JSON report generation
    with open(output_path, 'w') as f:
        json.dump(scan_result, f, indent=4)

def generate_pdf_report(scan_result, ai_result, output_path):
    # Placeholder for existing PDF report generation
    with open(output_path, 'w') as f:
        f.write("PDF report placeholder")

