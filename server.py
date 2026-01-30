import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'   # localhost
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)

print("Server started... waiting for client")

conn, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    client_msg = conn.recv(1024).decode()
    if not client_msg or client_msg.lower() == "exit":
        print("Client disconnected")
        break

    print("Client:", client_msg)

    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()