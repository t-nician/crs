from time import sleep
from threading import Thread

from crs.base import SocketType

from crs.client import ClientSocket
from crs.server import ServerSocket


def client_main():
    print("client_main ran")
    client = ClientSocket(
        connect_on_initialize=True
    )
    
    # client.client_establish() is ran when connect_on_initialize is true


def server_main():
    print("server_main ran")
    ServerSocket().start()


if __name__ == "__main__":
    Thread(target=server_main).start()
    
    sleep(1)
    
    client_main()