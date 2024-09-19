from enum import Enum
from socket import socket, AF_INET, SOCK_STREAM
from typing import Any


from pydantic import BaseModel, Field, ConfigDict


class SocketType(Enum):
    SERVER = "SERVER_SOCKET"
    CLIENT = "CLIENT_SOCKET"
    UNKNOWN = "UNKNOWN_SOCKET"


class BaseSocket(BaseModel):
    address: tuple[str, int] = Field(
        default_factory=lambda: ("127.0.0.1", 5000)
    )
    
    socket_type: SocketType = Field(default=SocketType.UNKNOWN)
    connect_on_initialize: bool = Field(default=False)
    
    
    def model_post_init(self, __context: Any) -> None:
        if self.connect_on_initialize:
            match self.socket_type:
                case SocketType.SERVER:
                    self.server_connect()
                case SocketType.CLIENT:
                    self.client_connect()
                case _:
                    raise Exception(f"connect_on_initialize true but socket_type is {self.socket_type}!")
        
        return super().model_post_init(__context)
    
    """
        Establish connection exchange
        
    """
    
    def server_connect(self):
        pass
    
    
    def client_connect(self):
        pass