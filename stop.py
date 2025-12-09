from jattmail.settings import BREAK, ADDRESS, PORT
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((ADDRESS, PORT))
clientsocket.send(BREAK.encode())