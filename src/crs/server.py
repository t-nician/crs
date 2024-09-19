from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

from pydantic import BaseModel, Field, ConfigDict


from crs.base import BaseSocket, SocketType
from crs.protocol import MessageType, CommandType


class ServerSocket(BaseSocket):
    socket_type: SocketType = Field(default=SocketType.SERVER)
    listeners: int = Field(default=10)
    
    def __server_establish(self, client_socket: socket):
        assert MessageType(
            client_socket.recv(
                len(MessageType.ACKNOWLEDGE.value)
            )
        ) == MessageType.ACKNOWLEDGE
        
        client_socket.send(MessageType.ACKNOWLEDGE.value)
        
        while True:
            pass
        
    
    def start(self):
        self.self_socket.bind(self.address)
        self.self_socket.listen(self.listeners)
        
        while True:
            client_socket, _ = self.self_socket.accept()
            
            Thread(
                target=self.__server_establish, args=(client_socket,)
            ).start()
            #self.__server_establish(client_socket)