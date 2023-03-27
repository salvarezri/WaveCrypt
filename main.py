# -** escuchar la señal y pasarla a texto

from gui.gui import Gui
from PyQt6 import QtWidgets

if __name__ == '__main__':
    # in order to reproduce the sound, you must press the send button in the window
    import sys
    # create window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # Start Gui
    ui = Gui()
    ui.start(MainWindow)
    MainWindow.show()
    # exit
    sys.exit(app.exec())

