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
    
    self_socket: socket = Field(
        default_factory=lambda: socket(AF_INET, SOCK_STREAM)
    )
    
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)