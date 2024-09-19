from time import sleep
from threading import Thread

from crs.base import SocketType

from crs.client import ClientSocket
from crs.server import ServerSocket


def client_main():
    client = ClientSocket(
        connect_on_initialize=True
    )


def server_main():
    ServerSocket().start()


if __name__ == "__main__":
    Thread(target=server_main).start()
    
    sleep(1)
    
    client_main()