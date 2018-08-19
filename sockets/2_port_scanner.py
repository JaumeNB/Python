import socket

#create a socket object
#AF_INET connection type
#SOCK_STREAM for TCP


#communicate with a server
server = '192.168.1.3'



ports_to_scan = [22, 80, 443, 5900, 12345]

for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server, port))
        print 'Port', port, 'is open'
    except Exception as e:
        print port, e
s.close()
