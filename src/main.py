from time import sleep
from threading import Thread

from crs.base import SocketType

from crs.client import ClientSocket
from crs.server import ServerSocket


def client_main():
    client = ClientSocket()


def server_main():
    pass



if __name__ == "__main__":
    Thread(target=server_main).start()
    
    sleep(1)
    
    client_main()