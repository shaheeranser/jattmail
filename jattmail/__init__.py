from jattmail.settings import ADDRESS, PORT, CONNECTIONS, BREAK
from jattmail.logs import Logs
from jattmail.connection import Connection
import socket

class JattMail:
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ADDRESS, PORT))
        self.server.listen(CONNECTIONS)
        self.logger = Logs()
        self.connections:set[Connection] = set()
    
    def isConnectionExists(self, address:tuple[str,int]) -> bool:
        for connection in self.connections:
            if connection.match(address):
                return True
        return False

    def run(self):
        self.logger.customLog("----- Server started -----\n")
        while True:
            connection, address = self.server.accept()
            data = connection.recv(255)

            # Checking for BREAK command
            if data.decode() == BREAK:
                self.logger.customLog("----- Server stopped -----\n")
                self.logger.close()
                break

            # Checking existing connection
            if not self.isConnectionExists(address):
                self.connections.add(Connection(address, connection))
            self.logger.new(address, data)
