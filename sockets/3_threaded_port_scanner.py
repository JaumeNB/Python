import threading
from Queue import Queue
import time
import socket

print_lock = threading.Lock()

server = '192.168.1.3'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((server, port))
        with print_lock:
            print('Port', port, 'is open')
        con.close()
    except:
        pass

def threader():
    while True:
        port_number = q.get()
        portscan(port_number)
        q.task_done()

q = Queue()


for x in range(500):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for port_number in range(5800, 6000):
    q.put(port_number)

q.join()
