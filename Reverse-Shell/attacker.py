import socket

HOST, PORT = (socket.gethostbyname(socket.gethostname()), 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(1)

print(f"Listening at port {PORT}")

client, address = sock.accept()

print(f"{address[0]}:{address[1]} Connected!")

while True:
    command = input("$ ")
    if command:
        client.send(command.encode())

        if command == "exit":
            break

        results = client.recv(1024).decode()

        print(results)

client.close()
sock.close()
