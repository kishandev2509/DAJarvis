from PyQt5 import QtWidgets,QtGui
from UI import Ui_Jarvis
import sys
from Functions import MainThread
        
startFunction = MainThread()

class Gui_start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_Jarvis(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)


    def startFunc(self):
        self.jarvis_ui.movies = QtGui.QMovie("GUIs/blank.gif")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("GUIs/Siri_1.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("GUIs/Jarvis_Loading_Screen.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_8 = QtGui.QMovie("GUIs/7LP8.gif")
        self.jarvis_ui.label_8.setMovie(self.jarvis_ui.movies_8)
        self.jarvis_ui.movies_8.start()

        startFunction.start()
        

if __name__ == "__main__":
    Gui_App = QtWidgets.QApplication(sys.argv)
    Gui_Jarvis = Gui_start()
    Gui_Jarvis.show()
    sys.exit(Gui_App.exec_())