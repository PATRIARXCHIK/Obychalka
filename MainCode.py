from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



mw = 'main'


def MainCodeClass():

    while mw == 'main':
        from main import Ui_MainWindow

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        def on_click():
            print('ok1')
            mw = 'task1'

            return MainCodeClass(mw)

        ui.pushButton.clicked.connect(on_click)
        sys.exit(app.exec_())


    while mw == 'task1':
        from task1 import Ui_MainWindow1

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()



        def on_click1():
            print("OK")


        ui.pushButton_2.clicked.connect(on_click1)
        sys.exit(app.exec_())

MainCodeClass()