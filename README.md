#🚀 Features

    🔒 Designed for PCI DSS segmentation validation

    🛡️ Uses aggressive evasion flags to simulate attacker behavior (e.g., TTL, decoy, packet fragmentation)

    🧪 Supports both standard and custom scan profiles

    📄 Generates detailed vulnerability reports in HTML and JSON format

    🐳 Docker support for easy deployment

```
🛠️ Installation
⬇️ Clone the repo

git clone https://github.com/your-org/pci-seg.git

cd pci-seg
```
```
📦 Install Python dependencies

pip install -r requirements.txt
```

🐳 Or use Docker
```
docker build -t pci-seg .
docker run --rm -v $(pwd)/reports:/app/reports pci-seg --target 192.168.1.1 --profile pci-core
```
⚙️ Usage
```
python3 main.py --target <TARGET_IP> --profile <pci-core|custom> --format <html|json>

Example

python3 main.py --target 10.0.0.1 --profile pci-core --format html
```

Arguments
Argument	Description
--target	IP address or hostname to scan
--profile	Scan profile: pci-core (default) or custom
--format	Output format: html (default) or json
```
📄 Output

Reports are saved under the reports/ directory.

    report_<timestamp>.html – Full vulnerability report in styled table format

    report_<timestamp>.json – Raw scan and result data
```
🔧 Scan Evasion Techniques

The tool uses several Nmap evasion options to simulate real-world attacks and test firewall/IPS filtering:

    -f : Fragment packets

    --data-length 20 : Add random data

    --ttl 128 : Set Time-To-Live

    --badsum : Send bad checksum packets

    -T2 : Set timing template

    -D RND:10 : Use 10 decoy source IPs

📦 Dependencies

    Python 3.8+

    Nmap

    jinja2 (for HTML report rendering)

Install manually:

pip install jinja2

Or use the included requirements.txt.
📌 To Do

Add unit tests

CI/CD integration for automated scans

    Add CVE-based enrichment

🛡️ Disclaimer

This tool is intended for authorized PCI DSS testing only. Do not use it against networks you do not own or have explicit permission to assess.
