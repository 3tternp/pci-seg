import argparse
import sys
import os
import json
from datetime import datetime

try:
    from core.scan_engine import perform_scan
    from core.ai_analysis import analyze_segmentation_results
    from core.report_generator import generate_report
except ModuleNotFoundError as e:
    missing_module = str(e).split("No module named ")[-1].strip("'")
    print(f"[!] Missing required module: {missing_module}")
    print("[i] Please make sure all project dependencies are installed.\n    Try: pip install -r requirements.txt")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="PCI DSS Segmentation Testing Tool with AI")
    parser.add_argument('--targets', required=True, help='Target IP/CIDR (e.g., 192.168.1.0/24)')
    parser.add_argument('--profile', default='pci-core', help='Port profile to use (default: pci-core)')
    parser.add_argument('--ai-analysis', action='store_true', help='Enable AI analysis')
    parser.add_argument('--report', choices=['json', 'html'], default='json', help='Report format')
    args = parser.parse_args()

    print("[*] Checking Nmap installation...")
    if os.system("which nmap > /dev/null 2>&1") != 0:
        print("[!] Error: Nmap is not installed. Please install it using:\n    sudo apt update && sudo apt install nmap")
        sys.exit(1)

    print("[*] Starting scan...")
    try:
        scan_data = perform_scan(args.targets, args.profile)
    except Exception as e:
        print(f"[!] Scan failed: {e}")
        sys.exit(1)

    ai_result = ""
    if args.ai_analysis:
        print("[*] Running AI analysis...")
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            print("[!] OPENAI_API_KEY environment variable is not set.")
            sys.exit(1)
        try:
            ai_result = analyze_segmentation_results(scan_data, openai_key)
        except Exception as e:
            print(f"[!] AI analysis failed: {e}")
            ai_result = "[AI analysis failed]"

    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/report_{timestamp}.{args.report}"

    print("[*] Generating report...")
    try:
        generate_report(scan_data, ai_result, report_path, args.report)
        print(f"[+] Report saved: {report_path}")
    except Exception as e:
        print(f"[!] Report generation failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
