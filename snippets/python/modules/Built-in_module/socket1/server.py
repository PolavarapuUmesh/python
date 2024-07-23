import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 8080

# Bind to the port
server_socket.bind(("", port))

# Queue up to 5 requests
server_socket.listen(5)

print("Server started. Listening for incoming connections...")

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from", addr)

    # Send a welcome message to the client
    client_socket.send("Welcome to the server!".encode())

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print("Received message from client:", data)

    # Send a response back to the client
    client_socket.send("Server received your message!".encode())

    # Close the connection
    client_socket.close()