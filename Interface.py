from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interface(object):
    def setupUi(self, Interface):
        Interface.setObjectName("Interface")
        Interface.resize(700, 362)
        self.label = QtWidgets.QLabel(Interface)
        self.label.setGeometry(QtCore.QRect(-10, -270, 1121, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\back121.jpg"))
        self.label.setObjectName("label")
        self.vk = QtWidgets.QPushButton(Interface)
        self.vk.setGeometry(QtCore.QRect(10, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.vk.setFont(font)
        self.vk.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.vk.setObjectName("vk")
        self.youtube = QtWidgets.QPushButton(Interface)
        self.youtube.setGeometry(QtCore.QRect(150, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.youtube.setFont(font)
        self.youtube.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.youtube.setObjectName("youtube")
        self.XVM = QtWidgets.QPushButton(Interface)
        self.XVM.setGeometry(QtCore.QRect(10, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XVM.setFont(font)
        self.XVM.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.XVM.setObjectName("XVM")
        self.ProTanki = QtWidgets.QPushButton(Interface)
        self.ProTanki.setGeometry(QtCore.QRect(150, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ProTanki.setFont(font)
        self.ProTanki.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.ProTanki.setObjectName("ProTanki")
        self.lichess = QtWidgets.QPushButton(Interface)
        self.lichess.setGeometry(QtCore.QRect(430, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lichess.setFont(font)
        self.lichess.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.lichess.setObjectName("lichess")
        self.steam = QtWidgets.QPushButton(Interface)
        self.steam.setGeometry(QtCore.QRect(290, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.steam.setFont(font)
        self.steam.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.steam.setObjectName("steam")
        self.calculator = QtWidgets.QPushButton(Interface)
        self.calculator.setGeometry(QtCore.QRect(10, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.calculator.setFont(font)
        self.calculator.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.calculator.setObjectName("calculator")
        self.mosru = QtWidgets.QPushButton(Interface)
        self.mosru.setGeometry(QtCore.QRect(570, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mosru.setFont(font)
        self.mosru.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.mosru.setObjectName("mosru")
        self.Lesta = QtWidgets.QPushButton(Interface)
        self.Lesta.setGeometry(QtCore.QRect(290, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Lesta.setFont(font)
        self.Lesta.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.Lesta.setObjectName("Lesta")
        self.Tanksgg = QtWidgets.QPushButton(Interface)
        self.Tanksgg.setGeometry(QtCore.QRect(430, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Tanksgg.setFont(font)
        self.Tanksgg.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.Tanksgg.setObjectName("Tanksgg")
        self.Wottactics = QtWidgets.QPushButton(Interface)
        self.Wottactics.setGeometry(QtCore.QRect(570, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Wottactics.setFont(font)
        self.Wottactics.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"}")
        self.Wottactics.setObjectName("Wottactics")
        self.label_2 = QtWidgets.QLabel(Interface)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffe5b4;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Interface)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffe5b4;")
        self.label_3.setObjectName("label_3")
        self.transfield = QtWidgets.QLineEdit(Interface)
        self.transfield.setGeometry(QtCore.QRect(170, 261, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transfield.setFont(font)
        self.transfield.setStyleSheet("background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;")
        self.transfield.setText("")
        self.transfield.setObjectName("transfield")
        self.searchfield = QtWidgets.QLineEdit(Interface)
        self.searchfield.setGeometry(QtCore.QRect(170, 310, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchfield.setFont(font)
        self.searchfield.setStyleSheet("background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;")
        self.searchfield.setText("")
        self.searchfield.setObjectName("searchfield")
        self.gotrans = QtWidgets.QPushButton(Interface)
        self.gotrans.setGeometry(QtCore.QRect(570, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gotrans.setFont(font)
        self.gotrans.setStyleSheet("QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}")
        self.gotrans.setObjectName("gotrans")
        self.gosearch = QtWidgets.QPushButton(Interface)
        self.gosearch.setGeometry(QtCore.QRect(570, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gosearch.setFont(font)
        self.gosearch.setStyleSheet("QPushButton {\n"
"background-color: #ffe5b4;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ffd485;\n"
"color: rgb(213, 53, 45);\n"
"border: 1px solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}")
        self.gosearch.setObjectName("gosearch")

        self.retranslateUi(Interface)
        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "Quick menu"))
        self.vk.setText(_translate("Interface", "VK"))
        self.youtube.setText(_translate("Interface", "YouTube"))
        self.XVM.setText(_translate("Interface", "XVM"))
        self.ProTanki.setText(_translate("Interface", "Protanki"))
        self.lichess.setText(_translate("Interface", "Lichess"))
        self.steam.setText(_translate("Interface", "Steam"))
        self.calculator.setText(_translate("Interface", "Calculator"))
        self.mosru.setText(_translate("Interface", "Mos ru"))
        self.Lesta.setText(_translate("Interface", "Lesta"))
        self.Tanksgg.setText(_translate("Interface", "Tanks gg"))
        self.Wottactics.setText(_translate("Interface", "WoT Tactics"))
        self.label_2.setText(_translate("Interface", "Translate:"))
        self.label_3.setText(_translate("Interface", "Search:"))
        self.gotrans.setText(_translate("Interface", "Go"))
        self.gosearch.setText(_translate("Interface", "Go"))