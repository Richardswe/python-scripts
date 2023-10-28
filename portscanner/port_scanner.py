# Author: Rickard Andersson 
import socket
import sys

# 1. Choose target and ports and run python3 port_scanner.py 
target = 'localhost'
ports = [443]
for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((target, port)) == 0:
            print("[+] The port {0} is open".format(port))
        else:
            print("[!]The port {0} is Closed".format(port))
    except socket.error:
        print("[!] Error with socket !")