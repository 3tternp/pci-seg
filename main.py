import subprocess
import platform
from core.report_generator import report_generator

def get_user_input():
    department = input("Enter your department: ")
    source_ip = input("Enter your source IP address: ")
    return department, source_ip

def get_target_ip():
    target_ip = input("Enter the target IP address to scan: ")
    return target_ip

def ping_target(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Error pinging target: {e}")
        return False

def run_nmap_firewall_bypass_scan(target_ip):
    try:
        # Using Nmap firewall evasion scan
        command = ["nmap", "-Pn", "-f", "--data-length", "25", "--source-port", "53", target_ip]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running Nmap: {e}")
        return ""

def parse_nmap_output(output):
    open_ports = []
    for line in output.splitlines():
        if "/tcp" in line and "open" in line:
            port_info = line.split()[0]
            open_ports.append(port_info)
    return open_ports

def build_report_data(department, source_ip, target_ip, icmp_status, open_ports):
    if icmp_status:
        icmp_result = {
            "issue_name": "ICMP Response Detected - PCI DSS Violation",
            "targeted_ip": target_ip,
            "source_ip": source_ip,
            "method_used": "ICMP Echo Request",
            "port_used": "N/A",
            "vulnerability_details": "Host responded to ICMP ping; violates PCI DSS requirements.",
            "attack_vector": "Network",
            "attack_complexity": "Low",
            "privileges_required": "None",
            "user_interaction": "None",
            "scope": "Unchanged",
            "confidentiality": "Low",
            "integrity": "None",
            "availability": "Low",
            "severity_rating": "Medium",
            "business_impact": "Potential exposure of internal network structure.",
            "remediation": "Block ICMP ping responses at the firewall for untrusted sources.",
            "proof_of_concept": f"Ping to {target_ip} from {source_ip} was successful."
        }
    else:
        icmp_result = {
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
        }

    report_data = [icmp_result]

    if open_ports:
        for port in open_ports:
            port_number = port.split("/")[0]
            report_data.append({
                "issue_name": "Firewall/IDS Evasion - Port Detected",
                "targeted_ip": target_ip,
                "source_ip": source_ip,
                "method_used": "Nmap Firewall Evasion Scan",
                "port_used": port_number,
                "vulnerability_details": f"Port {port} open despite firewall/IDS evasion scan.",
                "attack_vector": "Network",
                "attack_complexity": "Low",
                "privileges_required": "None",
                "user_interaction": "None",
                "scope": "Unchanged",
                "confidentiality": "Medium",
                "integrity": "Low",
                "availability": "Low",
                "severity_rating": "High",
                "business_impact": "Firewall/IDS misconfiguration may lead to unauthorized access.",
                "remediation": f"Review firewall rules and ensure port {port_number} is necessary and protected.",
                "proof_of_concept": f"Nmap evasion scan revealed port {port} open on {target_ip}."
            })

    return report_data

def main():
    department, source_ip = get_user_input()
    target_ip = get_target_ip()
    icmp_success = ping_target(target_ip)

    nmap_output = run_nmap_firewall_bypass_scan(target_ip)
    open_ports = parse_nmap_output(nmap_output)

    reports = build_report_data(department, source_ip, target_ip, icmp_success, open_ports)

    for idx, report in enumerate(reports):
        output_file = f"output/report_{idx+1}.docx"
        report_generator(report, output_file, fmt="docx")
        print(f"[+] Report generated: {output_file}")

if __name__ == "__main__":
    main()
