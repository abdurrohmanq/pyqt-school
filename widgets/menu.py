# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class SignSignal(QObject):
    fikr_up=pyqtSignal()
    sign_up_signal=pyqtSignal()
    about_signal=pyqtSignal()
class Ui_MenuWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.s_up=SignSignal()
        self.fikr_signal=SignSignal()
        self.about_up=SignSignal()
    def setupUimenu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.haqida = QtWidgets.QPushButton(parent=self.centralwidget)
        self.haqida.setGeometry(QtCore.QRect(230, 460, 299, 43))
        self.haqida.setMinimumSize(QtCore.QSize(120, 43))
        self.haqida.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.haqida.setFont(font)
        self.haqida.setStyleSheet("background-color: rgb(83, 112, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:18px;")
        self.haqida.clicked.connect(self.click_aboutbtn)
        self.haqida.setObjectName("haqida")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 390, 411, 45))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kurs = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.kurs.setMinimumSize(QtCore.QSize(120, 43))
        self.kurs.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.kurs.setFont(font)
        self.kurs.setStyleSheet("background-color: rgb(83, 112, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:18px;")
        self.kurs.setObjectName("kurs")
        self.kurs.clicked.connect(self.click_regbtn)
        self.horizontalLayout.addWidget(self.kurs)
        self.fikr = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.fikr.setMinimumSize(QtCore.QSize(120, 43))
        self.fikr.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fikr.setFont(font)
        self.fikr.setStyleSheet("background-color: rgb(83, 112, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:18px;")
        self.fikr.clicked.connect(self.click_fikrbtn)
        self.fikr.setObjectName("fikr")
        self.horizontalLayout.addWidget(self.fikr)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 721, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/online-maktab-darslar-large.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.haqida.setText(_translate("MainWindow", "Maktab haqida"))
        self.kurs.setText(_translate("MainWindow", "Kurslar"))
        self.fikr.setText(_translate("MainWindow", "Feedback"))
    def click_regbtn(self):
        self.s_up.sign_up_signal.emit()
        self.hide()
    def click_fikrbtn(self):
        self.fikr_signal.fikr_up.emit()
        self.hide()
    def click_aboutbtn(self):
        self.about_up.about_signal.emit()
        self.hide()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
    #sys.exit(app.exec())
