import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.25.255.151", 25))
server.listen(5)

print("Server started at 172.25.255.151:25")
while True:
    connection, address = server.accept()
    print(address)
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        break