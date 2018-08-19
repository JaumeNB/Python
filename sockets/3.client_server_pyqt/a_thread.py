import socket
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import time

class A_Thread(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.thread_to_stop = False

    def __del__(self):
        self.wait()

    def run(self):
        while self.thread_to_stop == False:
            pass

    def finish_thread(self):
        self.thread_to_stop = True

def main():
    a_t = A_Thread()
    a_t.run()
    print 'Exiting'

if __name__ == '__main__':
    main()
