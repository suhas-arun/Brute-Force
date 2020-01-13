"""Port Scanner"""
import socket

ip = input("Enter ip address: ")
open_ports: list = []
try:
    for port in range(1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        recv = s.connect_ex((ip, port))
        if recv == 0:
            print(f"***Port {port}: open***")
            open_ports.append(port)
        else:
            print(f"Port {port}: not open")

except socket.gaierror:
    print("\nThere was an error. Please check the IP address and try again.")

except KeyboardInterrupt:
    print("\nStopping scanner...")

if open_ports:
    print("\nThe following open ports were found:", end=" ")
    for port in open_ports:
        print(port, end=" ")
    print()

else:
    print("\nNo open ports were found.")
