from PyQt5 import QtCore, QtGui, QtWidgets
from Functions import MainThread
import sys


class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        Jarvis.resize(1155, 560)
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 1155, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUIs/blank.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(450, 0, 441, 291))
        # self.label_2.setText("")
        # self.label_2.setPixmap(QtGui.QPixmap("GUIs/Iron_Template_1.gif"))
        # self.label_2.setScaledContents(True)
        # self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-50, 300, 501, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("GUIs/Siri_1.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -40, 411, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("GUIs/Jarvis_Loading_Screen.gif"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(420, 230, 421, 331))
        self.label_5.setGeometry(QtCore.QRect(400, 5, 750, 550))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("GUIs/gggf.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(436, 290, 391, 221))
        # self.label_6.setText("")
        # self.label_6.setPixmap(QtGui.QPixmap("GUIs/B.G_Template_1.gif"))
        # self.label_6.setScaledContents(True)
        # self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 510, 101, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(55, 239, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 510, 101, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(55, 239, 255);\n"
"background-color: rgb(218, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        # self.label_7 = QtWidgets.QLabel(self.centralwidget)
        # self.label_7.setGeometry(QtCore.QRect(340, 100, 211, 141))
        # self.label_7.setText("")
        # self.label_7.setPixmap(QtGui.QPixmap("GUIs/Earth.gif"))
        # self.label_7.setScaledContents(True)
        # self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 391, 300))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("GUIs/7LP8.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label.raise_()
        # self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        # self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        # self.label_7.raise_()
        self.label_8.raise_()
        Jarvis.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)

    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "MainWindow"))
        self.pushButton.setText(_translate("Jarvis", "START"))
        self.pushButton_2.setText(_translate("Jarvis", "EXIT"))




startFunction = MainThread()

class Gui_start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_Jarvis()
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)


    def startFunc(self):
        self.jarvis_ui.movies = QtGui.QMovie("GUIs/blank.gif")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        # self.jarvis_ui.movies_2 = QtGui.QMovie("GUIs/Iron_Template_1.gif")
        # self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_2)
        # self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("GUIs/Siri_1.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("GUIs/Jarvis_Loading_Screen.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()


        # self.jarvis_ui.movies_6 = QtGui.QMovie("GUIs/B.G_Template_1.gif")
        # self.jarvis_ui.label_6.setMovie(self.jarvis_ui.movies_6)
        # self.jarvis_ui.movies_6.start()



        # self.jarvis_ui.movies_7 = QtGui.QMovie("GUIs/Earth.gif")
        # self.jarvis_ui.label_7.setMovie(self.jarvis_ui.movies_7)
        # self.jarvis_ui.movies_7.start()


        self.jarvis_ui.movies_8 = QtGui.QMovie("GUIs/7LP8.gif")
        self.jarvis_ui.label_8.setMovie(self.jarvis_ui.movies_8)
        self.jarvis_ui.movies_8.start()

        startFunction.start()
        

if __name__ == "__main__":
    Gui_App = QtWidgets.QApplication(sys.argv)
    Gui_Jarvis = Gui_start()
    Gui_Jarvis.show()
    sys.exit(Gui_App.exec_())

