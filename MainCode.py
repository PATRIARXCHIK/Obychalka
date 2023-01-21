from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from task1 import Ui_MainWindow1
from main import Ui_MainWindow
import sys

__name__ == '__main__'

while __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def on_click():
        print('ok1')
        __name__ = '__task1__'

    ui.pushButton.clicked.connect(on_click)
    sys.exit(app.exec_())


while __name__ == '__task1__':
    import sys
    app1 = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow1()
    ui1.setupUi(MainWindow1)
    MainWindow1.show()

    def on_click1():
            print("OK")

    ui1.pushButton.clicked.connect(on_click1)
    sys.exit(app1.exec_())