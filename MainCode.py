from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class main(QWidget):

    def __init__(self):
        super(main, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle('main')
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.pushButton_m = QtWidgets.QPushButton(self)
        self.pushButton_m.setGeometry(QtCore.QRect(70, 30, 251, 31))
        self.pushButton_m.setObjectName("pushButton")
        self.pushButton_2_m = QtWidgets.QPushButton(self)
        self.pushButton_2_m.setGeometry(QtCore.QRect(390, 30, 251, 31))
        self.pushButton_2_m.setObjectName("pushButton_2")
        self.pushButton_3_m = QtWidgets.QPushButton(self)
        self.pushButton_3_m.setGeometry(QtCore.QRect(70, 80, 571, 31))
        self.pushButton_3_m.setObjectName("pushButton_3")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main", "MainWindow"))
        self.pushButton_m.setText(_translate("main", "Виды и свойства информации (Тест 1)"))
        self.pushButton_2_m.setText(_translate("main", "Виды и свойства информации (Тест 2)"))
        self.pushButton_3_m.setText(_translate("main", "Информационный объём фрагмента текста"))



class task1(QWidget):
    def __init__(self):
        super(task1, self).__init__()
        self.setWindowTitle('task1')
        self.setMinimumWidth(815)
        self.setMinimumHeight(574)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(310, 0, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(340, 100, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(550, 100, 201, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(130, 40, 621, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 321, 31))
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(440, 160, 16, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(640, 160, 16, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(0, 200, 331, 31))
        self.label_6.setObjectName("label_6")
        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(440, 210, 70, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setGeometry(QtCore.QRect(640, 210, 70, 17))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(0, 240, 331, 61))
        self.label_7.setObjectName("label_7")
        self.checkBox_5 = QtWidgets.QCheckBox(self)
        self.checkBox_5.setGeometry(QtCore.QRect(440, 270, 70, 17))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self)
        self.checkBox_6.setGeometry(QtCore.QRect(640, 270, 70, 17))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(6, 312, 321, 61))
        self.label_8.setObjectName("label_8")
        self.checkBox_7 = QtWidgets.QCheckBox(self)
        self.checkBox_7.setGeometry(QtCore.QRect(440, 330, 70, 17))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self)
        self.checkBox_8.setGeometry(QtCore.QRect(640, 330, 70, 17))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(10, 380, 321, 41))
        self.label_9.setObjectName("label_9")
        self.checkBox_9 = QtWidgets.QCheckBox(self)
        self.checkBox_9.setGeometry(QtCore.QRect(440, 390, 70, 17))
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self)
        self.checkBox_10.setGeometry(QtCore.QRect(640, 390, 31, 17))
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 480, 171, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(440, 480, 221, 81))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(0, 90, 761, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(0, 130, 751, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(0, 179, 751, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(0, 220, 751, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(0, 280, 761, 51))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(0, 349, 751, 51))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(0, 420, 761, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(750, 100, 16, 331))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(550, 100, 21, 331))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(327, 102, 20, 331))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(-4, 102, 16, 331))
        self.label_21.setObjectName("label_21")

        task1.menubar = QtWidgets.QMenuBar()
        task1.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        task1.menubar.setObjectName("menubar")

        QtCore.QMetaObject.connectSlotsByName(self)
        task1.setTabOrder(self.checkBox, self.checkBox_2)
        task1.setTabOrder(self.checkBox_2, self.checkBox_3)
        task1.setTabOrder(self.checkBox_3, self.checkBox_4)
        task1.setTabOrder(self.checkBox_4, self.checkBox_5)
        task1.setTabOrder(self.checkBox_5, self.checkBox_6)
        task1.setTabOrder(self.checkBox_6, self.checkBox_7)
        task1.setTabOrder(self.checkBox_7, self.checkBox_8)
        task1.setTabOrder(self.checkBox_8, self.checkBox_9)
        task1.setTabOrder(self.checkBox_9, self.checkBox_10)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow1", "Тест 1"))
        self.label.setText(_translate("MainWindow1", "<html><head/><body><p><span style=\" font-size:18pt;\">Проверь себя!</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Декларативные знания</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Процедурные знания</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Распределите виды знаний в соответствии с их классификацией</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Земля вращается вокруг Солнца</span></p></body></html>"))
        self.checkBox.setToolTip(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Пушкин родился в 1799 году</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Байкал - самое глубокое</span></p><p align=\"center\"><span style=\" font-size:14pt;\"> пресное озеро</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Квадрат гипотенузы равен сумме</span></p><p align=\"center\"><span style=\" font-size:14pt;\"> квадратов катетов</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Как собрать радиоприемник</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow1", "Назад"))
        self.pushButton_2.setText(_translate("MainWindow1", "Ответ"))
        self.label_10.setText(_translate("MainWindow1", "<html><head/><body><p><span style=\" font-size:20pt;\">Текст</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_12.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_13.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_14.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_15.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_16.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_17.setText(_translate("MainWindow1", "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"))
        self.label_18.setText(_translate("MainWindow1", "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        ""))
        self.label_19.setText(_translate("MainWindow1", "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        ""))
        self.label_20.setText(_translate("MainWindow1", "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃"))
        self.label_21.setText(_translate("MainWindow1", "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃\n"
                                                        "┃"))

class task2(QWidget):
    def __init__(self):
        super(task2, self).__init__()
        self.setWindowTitle('Window1')
        self.setMinimumWidth(874)
        self.setMinimumHeight(600)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(570, 90, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 90, 551, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 521, 51))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 180, 251, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 581, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(600, 260, 231, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 491, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 330, 231, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 401, 31))
        self.label_5.setObjectName("label_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(430, 400, 251, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 460, 191, 61))
        self.pushButton.setMinimumSize(QtCore.QSize(191, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(191, 16777215))
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 450, 261, 71))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 0, 191, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 50, 241, 31))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.comboBox_4.raise_()
        self.label_4.raise_()
        self.comboBox_3.raise_()
        self.label_5.raise_()
        self.comboBox_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Вещество"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Электричество"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Информация"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Энергия"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'OpenSans\'; font-size:14pt; color:#000000; background-color:#ffffff;\">1.Среди фундаментальных понятий современной науки лишним является:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">1.Среди фундаментальных понятий современной науки лишним является:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">2. Информацию, отражающую истинное положение дел, называют:</span></p></body></html>\n"""))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Актуальной"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Объективной"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Полной"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Достоверной"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style= \"font-size:12pt; \">3. Информацию, достаточную для решения поставленной задачи, называют:</span></p></body></html>\n"""))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Актуальной"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Объективной"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Полной"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Достоверной"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"font-size:12pt;\">4. Визуальную информацию человек воспринимает органом:</span></p></body></html>\n"""))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Слуха"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Осязания"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Зрения"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Обоняния"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">5. Примером текстовой информации может служить:</span></p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Иллюстрация в книге"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Таблица умножения"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Музыкальное сопровождение"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Стихи из сборника"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Ответ</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Ответ</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Ответ"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Результат</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Проверь себя!</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Выбери 1 из 4 ответов</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle('MainWindow')
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(70, 10, 251, 31))
        self.button.setObjectName("pushButton")
        self.button.setText(_translate("MainWindow", "Начать"))

    def show_main(self):
        self.w1 = main()

        self.w1.pushButton_m.clicked.connect(self.show_task1)
        self.w1.pushButton_m.clicked.connect(self.w1.close)

        self.w1.show()

    def show_task1(self):
        self.w2 = task1()

        self.w2.pushButton.clicked.connect(self.show_main)
        self.w2.pushButton.clicked.connect(self.w2.close)

        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Pl = MainWindow()
    Pl.show_main()

    sys.exit(app.exec_())