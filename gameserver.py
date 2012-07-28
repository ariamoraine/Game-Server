import sys
import threading
import socket
import pickle
import os

myList = ["i'm", "a", "list", "sent", "from", "the", "server"]
pickledList = pickle.dumps (myList)

class ClientThread (threading.Thread):

    def __init__ (self, SocketObject, IpAddress):
        self.SocketObject = SocketObject
        self.IpAddress = IpAddress
        threading.Thread.__init__(self)

    def run(self):
        print 'Started a connection with:', self.SocketObject, 'At:', IpAddress
        self.SocketObject.send (pickledList)
        print pickle.loads (self.SocketObject.recv(1024))
        self.SocketObject.close()
        print 'Closed the connection with:', SocketObject, 'At:', IpAddress

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind (('10.242.11.167', 2727))
server.listen (5)

try:
    while True:
        SocketObject, IpAddress = server.accept()
        ClientThread (SocketObject, IpAddress).start()
except KeyboardInterrupt:
    os._exit(0)