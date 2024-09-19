from socket import socket, AF_INET, SOCK_STREAM


from pydantic import BaseModel, Field, ConfigDict

from crs.base import BaseSocket, SocketType


class ClientSocket(BaseSocket):
    socket_type: SocketType = Field(default=SocketType.CLIENT)
    
    
    def connect(self):
        print("client attempting to connect")
        self.self_socket.connect(self.address)
        