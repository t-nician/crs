from socket import socket, AF_INET, SOCK_STREAM

from pydantic import BaseModel, Field, ConfigDict


from crs.base import BaseSocket


class ServerSocket(BaseSocket):
    pass