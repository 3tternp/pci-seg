**PCI-DSS Recon and Vulnerability Report Tool**
```
This tool is designed to perform PCI-DSS-compliant reconnaissance with advanced evasion techniques using Nmap, and generate detailed vulnerability reports in HTML, JSON, and DOCX formats.

It helps auditors and security professionals conduct stealthy scans and document the findings in a structured format, suitable for audit records or compliance reports.
```
**Features**
```
Port Scanning with Evasion: Leverages Nmap with evasion flags such as fragmenting packets, modifying TTL, using decoys, etc.

Profile-based Scanning: Currently supports pci-core and custom scanning profiles.

HTML Report Generation: Nicely formatted HTML report using a Jinja2 template.

JSON Report Option: Machine-readable output for integrations.

DOCX Report Output: Automatically fills a vulnerability table in a .docx file.
```
**Project Structure**
```
.
├── core
│   ├── scan_engine.py          # Scanning engine with Nmap and evasion flags
│   └── report_generator.py     # HTML, DOCX, and JSON report generator
├── templates/
│   └── report_template.docx    # (optional) Base design
└── output/
    └── final_report.docx       # Filled report output
```
**Installation**
```
pip install -r requirements.txt
```
**Dependencies:**
```
nmap (ensure it is installed and available in the system PATH)

jinja2

python-docx
```
**Usage**

```
Output

```
report.html: A detailed human-readable vulnerability report.

report.json: Same data in structured JSON format.

report.docx: Word document in tabular vulnerability format.
```
Profiles Supported
```
pci-core: Ports relevant for PCI-DSS audits.

custom: All ports from 1-1024 (default fallback).
```
**Future Enhancements**
```
CLI wrapper for easy terminal use

Integration with vulnerability databases (e.g., CVE lookup)

Option to customize template files
```
Author
```
Developed by Astra(3tternp)
```

**Disclaimer**

This tool is intended for authorized PCI DSS testing only. Do not use it against networks you do not own or have explicit permission to assess.
