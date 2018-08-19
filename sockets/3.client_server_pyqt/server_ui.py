# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.server_close_btn = QtGui.QPushButton(Form)
        self.server_close_btn.setObjectName(_fromUtf8("server_close_btn"))
        self.verticalLayout.addWidget(self.server_close_btn)
        self.server_start_btn = QtGui.QPushButton(Form)
        self.server_start_btn.setObjectName(_fromUtf8("server_start_btn"))
        self.verticalLayout.addWidget(self.server_start_btn)
        self.thread_start_btn = QtGui.QPushButton(Form)
        self.thread_start_btn.setObjectName(_fromUtf8("thread_start_btn"))
        self.verticalLayout.addWidget(self.thread_start_btn)
        self.thread_finish_btn = QtGui.QPushButton(Form)
        self.thread_finish_btn.setObjectName(_fromUtf8("thread_finish_btn"))
        self.verticalLayout.addWidget(self.thread_finish_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.server_close_btn.setText(_translate("Form", "Close server", None))
        self.server_start_btn.setText(_translate("Form", "Start server", None))
        self.thread_start_btn.setText(_translate("Form", "Start thread", None))
        self.thread_finish_btn.setText(_translate("Form", "Finish thread", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
