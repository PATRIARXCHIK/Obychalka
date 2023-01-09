from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()

def GoTask1():
    Form, Window = uic.loadUiType("task1.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()