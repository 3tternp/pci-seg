import subprocess
import platform
import xml.etree.ElementTree as ET

def ping_host(ip):
    """Returns True if ping is successful."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"[!] Ping failed for {ip}: {e}")
        return False

def perform_scan_with_evasion(target_ip, profile):
    evasion_flags = [
        "-f",
        "--data-length", "20",
        "--ttl", "128",
        "--badsum",
        "-T2",
        "-D", "RND:10"
    ]

    profile_ports = {
        "pci-core": "21,22,23,25,53,80,110,139,143,443,445,3389",
        "custom": "1-1024"
    }

    ports = profile_ports.get(profile, profile_ports["pci-core"])

    command = [
        "nmap",
        "-Pn",
        "-p", ports,
        "-sS",
        "-n",
        "--open",
        "-oX", "-"
    ] + evasion_flags + [target_ip]

    print("[*] Executing Nmap command with evasion:", " ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"[!] Nmap scan failed: {result.stderr.strip()}")

    parsed = parse_nmap_xml(result.stdout)
    return parsed, result.stdout

def parse_nmap_xml(xml_data):
    try:
        root = ET.fromstring(xml_data)
        scan_results = []
        for host in root.findall('host'):
            ip_elem = host.find('address')
            ip = ip_elem.attrib['addr'] if ip_elem is not None else 'unknown'

            ports = []
            for port in host.findall('.//port'):
                port_id = port.attrib.get('portid')
                state = port.find('state').attrib.get('state')
                service_elem = port.find('service')
                service = service_elem.attrib.get('name') if service_elem is not None else 'unknown'
                if state == 'open':
                    ports.append({"port": port_id, "service": service})

            icmp_status = ping_host(ip)
            icmp_result = {
                "icmp_status": "failed" if not icmp_status else "successful",
                "pci_dss_compliance": "Compliant" if not icmp_status else "Non-Compliant"
            }

            scan_results.append({
                "ip": ip,
                "icmp_check": icmp_result,
                "open_ports": ports
            })

        return scan_results
    except Exception as e:
        raise RuntimeError(f"[!] Failed to parse Nmap XML output: {e}")
