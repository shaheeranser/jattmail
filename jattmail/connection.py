from socket import socket

class Connection:
  def __init__(self, address:tuple[str,int], connection:socket) -> None:
    self.address = f"{address[0]}:{address[1]}"
    self.connection = connection
    self.session_id = ""
  
  def match(self, address:tuple[str,int]) -> bool:
    return self.address == f"{address[0]}:{address[1]}"