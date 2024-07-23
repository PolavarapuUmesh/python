import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345

# Connect to the server
client_socket.connect(("localhost", port))

print("Connected to the server!")

# Receive a welcome message from the server
data = client_socket.recv(1024).decode()
print("Received message from server:", data)

# Send a message to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Receive a response from the server
data = client_socket.recv(1024).decode()
print("Received message from server:", data)

# Close the connection
client_socket.close()