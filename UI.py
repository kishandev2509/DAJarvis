from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jarvis():
    def __init__(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        # Jarvis.setFixedSize(1155, 560)
        Jarvis.setFixedSize(400, 570)
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 1155, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUIs/blank.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.label_5.setGeometry(QtCore.QRect(400, 5, 750, 550))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("GUIs/gggf.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 95, 670, 370))
        font = QtGui.QFont('Arial', 16)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #006A80;border: none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 510, 101, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(55, 239, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 510, 101, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(218, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 391, 300))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("GUIs/7LP8.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_8.raise_()
        self.textEdit.raise_()
        Jarvis.setCentralWidget(self.centralwidget)
        Jarvis.setWindowTitle("Jarvis")
        self.pushButton.setText("START")
        self.pushButton_2.setText("EXIT")
