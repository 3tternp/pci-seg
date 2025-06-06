import subprocess
from core.scan_engine import perform_scan_with_evasion
from core.report_generator import report_generator

def is_icmp_blocked(source_ip, target_ip):
    try:
        result = subprocess.run(["ping", "-c", "2", target_ip], stdout=subprocess.DEVNULL)
        return result.returncode != 0
    except Exception as e:
        print("[!] Ping failed:", str(e))
        return False  # assume allowed if error

def main():
    print("=== PCI DSS Compliance Scanner ===")
    dept = input("Enter your department name: ")
    source_ip = input("Enter your source IP address: ")
    target_ip = input("Enter target IP address to scan: ")

    findings = []

    # --- ICMP Check ---
    icmp_blocked = is_icmp_blocked(source_ip, target_ip)
    if icmp_blocked:
        findings.append({
            "issue_name": "ICMP Response Blocked - PCI DSS Compliant",
            "targeted_ip": target_ip,
            "source_ip": source_ip,
            "method_used": "ICMP Echo Request",
            "port_used": "N/A",
            "vulnerability_details": "ICMP request blocked; meets PCI DSS compliance.",
            "attack_vector": "Network",
            "attack_complexity": "Low",
            "privileges_required": "None",
            "user_interaction": "None",
            "scope": "Unchanged",
            "confidentiality": "None",
            "integrity": "None",
            "availability": "None",
            "severity_rating": "Informational",
            "business_impact": "Compliant with PCI DSS requirements.",
            "remediation": "No action needed.",
            "proof_of_concept": f"Ping to {target_ip} from {source_ip} failed."
        })
    else:
        findings.append({
            "issue_name": "ICMP Response Allowed - PCI DSS Violation",
            "targeted_ip": target_ip,
            "source_ip": source_ip,
            "method_used": "ICMP Echo Request",
            "port_used": "N/A",
            "vulnerability_details": "ICMP request successful; violates PCI DSS requirement to block ICMP.",
            "attack_vector": "Network",
            "attack_complexity": "Low",
            "privileges_required": "None",
            "user_interaction": "None",
            "scope": "Unchanged",
            "confidentiality": "Low",
            "integrity": "None",
            "availability": "Low",
            "severity_rating": "Medium",
            "business_impact": "May allow network enumeration and reconnaissance.",
            "remediation": "Block ICMP echo requests on perimeter firewall.",
            "proof_of_concept": f"Ping to {target_ip} from {source_ip} succeeded."
        })

    # --- Nmap Firewall Evasion Scan ---
    print("[*] Running firewall bypass scan...")
    scan_results, _ = perform_scan_with_evasion(target_ip, profile="pci-core")

    if scan_results:
        for host in scan_results:
            for port in host["open_ports"]:
                findings.append({
                    "issue_name": "Firewall/IDS Bypass Successful - PCI DSS Violation",
                    "targeted_ip": host["ip"],
                    "source_ip": source_ip,
                    "method_used": "Nmap with evasion flags",
                    "port_used": port["port"],
                    "vulnerability_details": f"Service '{port['service']}' found open via bypass.",
                    "attack_vector": "Network",
                    "attack_complexity": "Low",
                    "privileges_required": "None",
                    "user_interaction": "None",
                    "scope": "Unchanged",
                    "confidentiality": "Low",
                    "integrity": "Low",
                    "availability": "Low",
                    "severity_rating": "High",
                    "business_impact": "Indicates firewall or IDS/IPS may not be properly configured.",
                    "remediation": "Implement proper firewall rules and intrusion detection controls.",
                    "proof_of_concept": f"Port {port['port']} ({port['service']}) discovered using bypass scan."
                })
    else:
        findings.append({
            "issue_name": "Firewall Bypass Blocked - PCI DSS Compliant",
            "targeted_ip": target_ip,
            "source_ip": source_ip,
            "method_used": "Nmap with evasion flags",
            "port_used": "N/A",
            "vulnerability_details": "No open ports discovered with firewall/IDS evasion.",
            "attack_vector": "Network",
            "attack_complexity": "Low",
            "privileges_required": "None",
            "user_interaction": "None",
            "scope": "Unchanged",
            "confidentiality": "None",
            "integrity": "None",
            "availability": "None",
            "severity_rating": "Informational",
            "business_impact": "Firewall and IDS appear to be properly configured.",
            "remediation": "None required.",
            "proof_of_concept": "Nmap with evasion techniques did not reveal any open ports."
        })

    # --- Report Generation ---
    report_generator(findings, "output/pci_report.docx", fmt="docx")

if __name__ == "__main__":
    main()
