import socket

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            return port
        sock.close()
    except socket.error:
        pass
    return None

def scan_network(target_network, start, end):
    print(f"Scanning network {target_network}...")
    open_ports = []
    network_parts = target_network.split('.')
    base_network = '.'.join(network_parts[:3])
    for host in range(1, 255):
        target_ip = f"{base_network}.{host}"
        for port in range(start, end + 1):
            open_port = scan_port(target_ip, port)
            if open_port:
                open_ports.append(open_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"IP: {target_ip}\tPort: {port}")
    else:
        print("No open ports found.")

target_network = "192.168.1.0"  
start= 1
end= 100

scan_network(target_network, start, end)
