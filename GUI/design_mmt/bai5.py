# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bai5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(850, 395)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 851, 81))
        self.frame.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(480, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.ip_server = QtWidgets.QTextBrowser(self.frame)
        self.ip_server.setGeometry(QtCore.QRect(110, 40, 371, 41))
        self.ip_server.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ip_server.setObjectName("ip_server")
        self.port_server = QtWidgets.QTextBrowser(self.frame)
        self.port_server.setGeometry(QtCore.QRect(480, 40, 371, 41))
        self.port_server.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.port_server.setObjectName("port_server")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        Server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))
        self.label_4.setText(_translate("Server", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Port</span></p></body></html>"))
        self.label_3.setText(_translate("Server", "<html><head/><body><p align=\"center\">IP</p></body></html>"))
        self.label_2.setText(_translate("Server", "<html><head/><body><p align=\"center\">Server</p></body></html>"))
        self.label_5.setText(_translate("Server", "List file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Server = QtWidgets.QMainWindow()
    ui = Ui_Server()
    ui.setupUi(Server)
    Server.show()
    sys.exit(app.exec_())