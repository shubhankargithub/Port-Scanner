import socket
from termcolor import colored





def print_port_scanner_pattern():
    pattern = """
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓        ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒      ▒██    ▒ ▒██▀ ▀▀  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░      ░ ▓██▄   ▒██      ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░         ▒   ██▒▒██▄▒▄█▒▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░       ▒██████▒▒▒▀████▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░         ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░          ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░            ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                          ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                   ░                                                         """
    print(colored(pattern, 'red'))

# Call the function to print the pattern
print("\n\n")
print_port_scanner_pattern()




def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Adjust timeout as needed
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(colored(f"Port {port} is open", "green"))
            try:
                service_name = socket.getservbyport(port)
                print(colored(f"Service running on port {port}: {service_name}", "cyan"))
            except socket.error:
                print(colored(f"No service name available for port {port}", "yellow"))
        sock.close()
    except KeyboardInterrupt:
        print("Keyboard Interrupted.")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    except socket.error:
        print("Couldn't connect to server.")
        exit()

def scan_target(target):
    print("Scanning target:", target)
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return

    print("Target IP:", target_ip)

    # Scan ports
    for port in range(1, 1025):  # Adjust port range as needed
        scan_port(target_ip, port)

if __name__ == "__main__":
    target = input("Enter target IP or domain name: ")
    scan_target(target)

