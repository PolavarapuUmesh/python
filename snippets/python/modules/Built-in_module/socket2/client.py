import socket

# Create a Unix socket
c = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to the server
socket_file = '/home/umesh/user.html'
c.connect(socket_file)

# Send data to the server
c.sendall(b'Hello from client!')

# Receive response from the server
data = c.recv(1024)
print('Received:', data.decode())

# Close the connection
client_socket.close()