import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #those arguments are address family ipv4 & connection oriented tcp protocol
port = 9090
server_socket.bind(("", port)) #here we are bindinng port num or ip add 
server_socket.listen(5) #it accepts the request where the request comes from the client side
print("Server started. Listening for incoming connections...")
while True:
    client_socket, addr = server_socket.accept()
    print("Got a connection from", addr)
    client_socket.send("Welcome to the server!".encode())
    data = client_socket.recv(1024).decode()
    print("Received message from client:", data)
    client_socket.send("Server received your message!".encode())
    client_socket.close()