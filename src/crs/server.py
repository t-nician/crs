from socket import socket, AF_INET, SOCK_STREAM

from pydantic import BaseModel, Field, ConfigDict


from crs.base import BaseSocket, SocketType


class ServerSocket(BaseSocket):
    socket_type: SocketType = Field(default=SocketType.SERVER)
    listeners: int = Field(default=10)
    
    def establish(self, client_socket: socket):
        print("server establishing connection with client")
    
    def start(self):
        self.self_socket.bind(self.address)
        self.self_socket.listen(self.listeners)
        
        while True:
            client_socket, _ = self.self_socket.accept()
            self.establish(client_socket)