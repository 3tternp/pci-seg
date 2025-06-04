# PCI SEG 
# PCI-DSS Recon and Vulnerability Report Tool

## Overview

This tool is designed to perform PCI-DSS-compliant reconnaissance with advanced evasion techniques using Nmap, and generate detailed vulnerability reports in both JSON and HTML formats.

It helps auditors and security professionals conduct stealthy scans and document the findings in a structured format, suitable for audit records or compliance reports.

---

## Features

* **Port Scanning with Evasion:** Leverages Nmap with evasion flags such as fragmenting packets, modifying TTL, using decoys, etc.
* **Profile-based Scanning:** Currently supports `pci-core` and `custom` scanning profiles.
* **HTML Report Generation:** Nicely formatted HTML report using a Jinja2 template.
* **JSON Report Option:** Machine-readable output for integrations.

---

## Project Structure

```bash
.
├── core
│   ├── scan_engine.py          # Scanning engine with Nmap and evasion flags
│   └── report_generator.py     # HTML and JSON report generator using Jinja2
├── templates                   # (Optional) Folder for storing HTML templates (currently inlined)
├── output                      # Output folder for scan results and reports
├── main.py                     # Main entry point for running scan + report (to be added)
└── README.md                   # Project documentation (this file)
```

---

## Installation

```bash
pip install -r requirements.txt
```

**Dependencies:**

* `nmap` (ensure it is installed and available in the system PATH)
* `jinja2`

---

## Usage

### From Python Script

```python
from core.scan_engine import perform_scan_with_evasion
from core.report_generator import report_generator

scan_result = perform_scan_with_evasion("192.168.1.1", "pci-core")

# Mock AI Result or leave as empty string
ai_result = "This PoC demonstrates service exposure on port 443 due to misconfigured SSL."

report_generator(scan_result[0], ai_result, "output/report.html", "html")
```

### Output

* `report.html`: A detailed human-readable vulnerability report.
* `report.json`: Same data in structured JSON format.

---

## Profiles Supported

* **pci-core**: Ports relevant for PCI-DSS audits.
* **custom**: All ports from 1-1024 (default fallback).

---

## Future Enhancements

* CLI wrapper for easy terminal use
* Integration with vulnerability databases (e.g., CVE lookup)
* Option to customize template files

---

## License

MIT License

---

## Author

Developed by Vairav Technology Security Pvt. Ltd.

---

## Disclaimer

This tool is intended for authorized security assessments only. Unauthorized use is strictly prohibited.
