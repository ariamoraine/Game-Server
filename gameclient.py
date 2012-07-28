import socket
import threading
import pickle

newList = ['this', 'is', 'a', 'list', 'sent', 'from', 'the', 'client']
pickledList = pickle.dumps(newList)

class ConnectionThread(threading.Thread):

    def run(self):
        client = socket.socket()
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
        client.connect (('10.242.11.167', 2727))
        print pickle.loads (client.recv(1024))
        client.send(pickledList)
        client.close()

for x in xrange (5):
   ConnectionThread().start()