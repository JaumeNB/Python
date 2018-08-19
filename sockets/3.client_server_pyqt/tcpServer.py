import socket
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

class TcpServer(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5004
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.wait()

    def run(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        print('Starting socket server (host {}, port {})'.format(self.host, self.port))

        while True:
            print("Wating for connection ... ")
            self.c, self.addr = self.s.accept()
            print('Client {} connected'.format(self.addr))
            while True:
                data = self.c.recv(1024).decode('utf-8')
                if not data:
                    break
                print("From connected user: " + data)
                print("Sending: " + data)
                self.c.send(data.encode('utf-8'))
            self.c.close()
            break



def main():
    server = TcpServer()
    server.run()
    print 'Exiting'

if __name__ == '__main__':
    main()
