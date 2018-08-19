import socket

class TcpServer():

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5004
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        print('Starting socket server (host {}, port {})'.format(self.host, self.port))

        while True:
            print("Wating for connection ... ")
            self.c, self.addr = self.s.accept()

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
