# main.py
import argparse
import os
from core.scan_engine import perform_scan_with_evasion
from core.report_generator import report_generator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PCI Recon Scanner")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--profile", default="pci-core", help="Scan profile: pci-core or custom")
    parser.add_argument('--report', choices=['html', 'json', 'pdf'], default='html', help='Report format')

    args = parser.parse_args()

    print("[*] Checking Nmap installation...")
    if not os.system("which nmap > /dev/null 2>&1") == 0:
        print("[!] Nmap not installed or not in PATH.")
        exit(1)

    try:
        print("[*] Starting scan...")
        scan_result, raw_output = perform_scan_with_evasion(args.target, args.profile)
    except Exception as e:
        print(f"[!] Scan failed: {e}")
        exit(1)

    try:
        print("[*] Generating report...")
        ai_result = ""  # Optional, placeholder for AI-based risk analysis
        output_path = os.path.join("output", f"report.{args.report}")
        os.makedirs("output", exist_ok=True)
        report_generator(scan_result, ai_result, output_path, args.report)
        print(f"[+] Report saved: {output_path}")
    except Exception as e:
        print(f"[!] Report generation failed: {e}")
