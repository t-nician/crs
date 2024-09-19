from socket import socket, AF_INET, SOCK_STREAM


from pydantic import BaseModel, Field, ConfigDict

from crs.base import BaseSocket, SocketType
from crs.protocol import MessageType, CommandType


class ClientSocket(BaseSocket):
    socket_type: SocketType = Field(default=SocketType.CLIENT)
    
    def __client_establish(self):
        self.self_socket.send(MessageType.ACKNOWLEDGE.value)
        
        assert MessageType(
            self.self_socket.recv(len(MessageType.ACKNOWLEDGE.value))
        ) == MessageType.ACKNOWLEDGE
        
        while True:
            pass
    
    def connect(self):
        print("client attempting to connect")
        
        self.self_socket.connect(self.address)
        self.__client_establish()
        