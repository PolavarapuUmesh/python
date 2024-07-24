import socket
import os 

s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) #create a unix socket

socket_file='/home/umesh/user.html' #create  a file for socket 
if os.path.exists(socket_file): #if the file already exists it won't
    os.remove(socket_file) # Send response back to the client
s.bind(socket_file) #bind the socket to the file
s.listen(1) #it listens on incoming connections
print('server listens on',socket_file)
while True: 
    connection, address = s.accept() # Accept incoming connections
    print('Connection from', address)
    data = connection.recv(1024)   # Receive data from the client
    print('Received:', data.decode())
    connection.sendall(b'Hello from server!') # # Send response back to the client
    connection.close() #connection closed