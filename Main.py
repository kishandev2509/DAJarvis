from PyQt5 import QtWidgets
from GuiStart import Gui_start
import sys


if __name__ == "__main__":
    Gui_App = QtWidgets.QApplication(sys.argv)
    Gui_Jarvis = Gui_start()
    Gui_Jarvis.show()
    sys.exit(Gui_App.exec_())

