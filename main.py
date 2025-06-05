# after scan completes
from core.report_generator import report_generator

scan_data = {
    "issue_name": "Unsecured FTP",
    "targeted_ip": "192.168.1.20",
    "source_ip": "192.168.1.5",
    "method_used": "TCP SYN Scan",
    "port_used": "21",
    "vulnerability_details": "Anonymous login allowed.",
    "attack_vector": "Network",
    "attack_complexity": "Low",
    "privileges_required": "None",
    "user_interaction": "None",
    "scope": "Unchanged",
    "confidentiality": "Low",
    "integrity": "None",
    "availability": "None",
    "severity_rating": "Medium",
    "business_impact": "Data leakage",
    "remediation": "Disable anonymous FTP",
    "proof_of_concept": "Login with user 'anonymous' succeeded."
}

report_generator(scan_data, "output/report.docx", fmt="docx")
