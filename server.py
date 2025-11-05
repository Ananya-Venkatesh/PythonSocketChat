import socket

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server running at {HOST}:{PORT}")

client_socket, address = server.accept()
print("Connected with", address)

while True:
    msg = client_socket.recv(1024).decode()
    if not msg:
        break
    print("Client:", msg)
    reply = input("Server: ")
    client_socket.send(reply.encode())

client_socket.close()
server.close()
