import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

while True:
    msg = input("Client: ")
    client.send(msg.encode())
    reply = client.recv(1024).decode()
    if not reply:
        break
    print("Server:", reply)

client.close()

