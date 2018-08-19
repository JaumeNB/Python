from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui
import sys
import socket
from server_ui import Ui_Form
from tcpServer import TcpServer
from a_thread import A_Thread

class Main(QWidget, Ui_Form):

    def started(self):
        QtGui.QMessageBox.information(self, "Started!", "thread started")

    def finished(self):
        QtGui.QMessageBox.information(self, "Finished!", "thread finished")

    @pyqtSignature("")
    def on_server_start_btn_pressed(self):
        self.ServerThread = TcpServer()
        self.connect(self.ServerThread, QtCore.SIGNAL("started()"), self.started)
        self.connect(self.ServerThread, QtCore.SIGNAL("finished()"), self.finished)
        self.ServerThread.start()

    @pyqtSignature("")
    def on_thread_start_btn_pressed(self):
        self.a_thread = A_Thread()
        self.connect(self.a_thread, QtCore.SIGNAL("started()"), self.started)
        self.connect(self.a_thread, QtCore.SIGNAL("finished()"), self.finished)
        self.a_thread.start()

    @pyqtSignature("")
    def on_thread_finish_btn_pressed(self):
        self.a_thread.finish_thread()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.threads_count = 1

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
