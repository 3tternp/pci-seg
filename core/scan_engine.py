import nmap

def perform_scan(targets, profile):
    nm = nmap.PortScanner()
    print(f"[*] Scanning {targets} with profile {profile}...")
    scan_result = nm.scan(hosts=targets, arguments='-sS -Pn')
    return scan_result
