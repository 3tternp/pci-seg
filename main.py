import argparse
from core.scan_engine import perform_scan_with_evasion
from core.report_generator import report_generator

def main():
    parser = argparse.ArgumentParser(description="PCI-DSS Recon and Vulnerability Report Tool")
    parser.add_argument('--target', required=True, help='Target IP or hostname')
    parser.add_argument('--profile', default='pci-core', help='Scan profile to use')
    parser.add_argument('--report', choices=['html', 'json', 'pdf'], default='html', help='Report format')

    args = parser.parse_args()

    print("[*] Checking Nmap installation...")
    # (Optional: add nmap check here)

    print("[*] Starting scan...")
    try:
        scan_result = perform_scan_with_evasion(args.target, args.profile)
    except Exception as e:
        print(f"[!] Scan failed: {e}")
        return

    report_path = f"output/report.{args.report}"

    print("[*] Generating report...")
    try:
        # Pass only scan_result, report_path, and report format (3 args)
        report_generator(scan_result, report_path, args.report)
        print(f"[+] Report saved: {report_path}")
    except Exception as e:
        print(f"[!] Report generation failed: {e}")

if __name__ == '__main__':
    main()

