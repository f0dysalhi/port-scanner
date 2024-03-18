import socket
import re
from concurrent.futures import ThreadPoolExecutor

def validate_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(ip_pattern.match(ip))

def validate_port_range(port_range):
    port_range_pattern = re.compile(r"(\d+)-(\d+)")
    match = port_range_pattern.match(port_range.replace(" ", ""))
    if match:
        start_port = int(match.group(1))
        end_port = int(match.group(2))
        if 0 <= start_port <= end_port <= 65535:
            return start_port, end_port
    return None, None

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port
    except Exception as e:
        pass

def main():
    print(r"""
     ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████████████▓▒░░▒▓█▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
     ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
           ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
           ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
              """)
    print("\n* ==>  https://github.com/f0dysalhi  <==")

    while True:
        ip = input("\nPlease enter the IP address that you want to scan: ")
        if validate_ip(ip):
            print(f"{ip} is a valid IP address.")
            break
        else:
            print("Invalid IP address. Please try again.")

    while True:
        port_range = input("Please enter the range of ports you want to scan (e.g., 60-120): ")
        start_port, end_port = validate_port_range(port_range)
        if start_port is not None and end_port is not None:
            break
        else:
            print("Invalid port range. Please try again.")

    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            if future.result():
                open_ports.append(port)

    if open_ports:
        print("\nHOST IS UP. TARGET HAS BEEN SCANNED.")
        print("The open ports are:", open_ports)
    else:
        print("\nNo open ports found on the target.")

if __name__ == "__main__":
    main()
 
