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
sudo su
source venv/bin/activate
 pip3 install -r requirements.txt
python3 main.py  --profile pci-core --report docx 
```

**Output**
![Screenshot From 2025-06-06 08-06-15](https://github.com/user-attachments/assets/32774795-d3e6-4960-8764-799db45fad63)
and the generated report looks like 
![image](https://github.com/user-attachments/assets/31e51e9e-3e1e-4ed8-a0b8-4011692c4eaa)


```
report.docx: Word document in tabular vulnerability format.
```
**Profiles Supported**
```
pci-core: Ports relevant for PCI-DSS audits.

custom: All ports from 1-1024 (default fallback).
```
**Author**
```
Developed by Astra(3tternp)
```

**Disclaimer**
```
This tool is intended for authorized PCI DSS testing only. Do not use it against networks you do not own or have explicit permission to assess.
```
