# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 90, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
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


if __name__ == 'task2':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    def on_click3():
        print("OK")

    ui.pushButton.clicked.connect(on_click3)
    sys.exit(app.exec_())
