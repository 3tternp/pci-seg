
import argparse
from core.scan_engine import perform_scan
from core.ai_analysis import analyze_segmentation_results
from core.report_generator import generate_report
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="PCI DSS Segmentation Testing Tool with AI")
    parser.add_argument('--targets', required=True, help='Target IP/CIDR (e.g., 192.168.1.0/24)')
    parser.add_argument('--profile', default='pci-core', help='Port profile to use (default: pci-core)')
    parser.add_argument('--ai-analysis', action='store_true', help='Enable AI analysis')
    parser.add_argument('--report', choices=['json', 'html'], default='json', help='Report format')
    args = parser.parse_args()

    print("[*] Starting scan...")
    scan_data = perform_scan(args.targets, args.profile)

    ai_result = ""
    if args.ai_analysis:
        print("[*] Running AI analysis...")
        ai_result = analyze_segmentation_results(scan_data)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    report_path = f"reports/report_{timestamp}.{args.report}"

    print("[*] Generating report...")
    generate_report(scan_data, ai_result, report_path, args.report)
    print(f"[+] Report saved: {report_path}")

if __name__ == '__main__':
    main()
