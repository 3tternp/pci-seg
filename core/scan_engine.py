
import nmap
import json
import ipaddress
from scapy.all import sr1, IP, ICMP

def ping_host(ip):
    resp = sr1(IP(dst=ip)/ICMP(), timeout=1, verbose=0)
    return resp is not None

def perform_scan(targets, profile):
    from pathlib import Path
    profile_path = Path("configs/ports.json")
    ports = json.load(profile_path.open())[profile]
    scanner = nmap.PortScanner()
    scan_data = []
    if "/" in targets:
        hosts = [str(ip) for ip in ipaddress.IPv4Network(targets).hosts()]
    else:
        hosts = [targets]

    for ip in hosts:
        reachable = ping_host(ip)
        if reachable:
            scanner.scan(hosts=ip, arguments=f'-Pn -p {",".join(map(str, ports))}')
            open_ports = [port for port in ports if port in scanner[ip]['tcp'] and scanner[ip]['tcp'][port]['state'] == 'open']
        else:
            open_ports = []
        scan_data.append({"ip": ip, "reachable": reachable, "open_ports": open_ports})
    return scan_data
