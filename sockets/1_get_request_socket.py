import socket

#create a socket object
#AF_INET connection type
#SOCK_STREAM for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#communicate with a server
server = 'pythonprogramming.net'

def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False

for x in range(1, 26):
    if pscan(x):
        print('Port', x, 'is open')
