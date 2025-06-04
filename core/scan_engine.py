# core/scan_engine.py
import subprocess
import json

def perform_scan_with_evasion(targets, profile):
    # Example evasion flags: -f (fragment), --data-length, --ttl, --badsum, -D for decoy
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
    ] + evasion_flags + [targets]

    print("[*] Executing Nmap command with evasion:", " ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Nmap scan failed: {result.stderr.strip()}")

    return parse_nmap_xml(result.stdout)

def parse_nmap_xml(xml_data):
    try:
        import xml.etree.ElementTree as ET
        root = ET.fromstring(xml_data)
        scan_results = []
        for host in root.findall('host'):
            ip_elem = host.find('address')
            ip = ip_elem.attrib['addr'] if ip_elem is not None else 'unknown'

            ports = []
            for port in host.findall('.//port'):
                port_id = port.attrib.get('portid')
                state = port.find('state').attrib.get('state')
                service = port.find('service').attrib.get('name', 'unknown')
                if state == 'open':
                    ports.append({"port": port_id, "service": service})

            if ports:
                scan_results.append({"ip": ip, "open_ports": ports})
        return scan_results
    except Exception as e:
        raise RuntimeError(f"Failed to parse Nmap XML output: {e}")
