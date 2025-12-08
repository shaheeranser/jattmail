import socket
import datetime

class JattMail:
    def __init__(this, connections:int, address:str="0.0.0.0", port=25) -> None:
        this.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this.server.bind((address, port))
        this.server.listen(connections)
    
    def run(this, stopCommand="exit()"):
        # connections:dict = {}
        while True:
            connection, address = this.server.accept()
            command = connection.recv(255)
            print(f"{address[0]}:{address[1]} - {datetime.datetime.now()} - {command}")
            break
            # connections[f"{address[0]}:{address[1]}"] = connection
