# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tic_tac_toe.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 543)

        self.p1=0
        self.p2=0

        self.chance = 'X'
        self.turn = 0
        self.mw = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(150, 40, 231, 20))
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(150, 70, 231, 20))
        self.input2.setObjectName("input2")

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(80, 100, 131, 121))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(210, 100, 131, 121))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(340, 100, 131, 121))
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(340, 220, 131, 121))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(210, 220, 131, 121))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(80, 220, 131, 121))
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(340, 340, 131, 121))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(210, 340, 131, 121))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(80, 340, 131, 121))
        self.nine.setObjectName("nine")
        self.winner = QtWidgets.QLineEdit(self.centralwidget)
        self.winner.setGeometry(QtCore.QRect(540, 250, 131, 31))
        self.winner.setObjectName("winner")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.select_o = QtWidgets.QPushButton(self.centralwidget)
        self.select_o.setGeometry(QtCore.QRect(388, 30, 65, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_o.setFont(font)
        self.select_o.setObjectName("select_o")
        self.select_x = QtWidgets.QPushButton(self.centralwidget)
        self.select_x.setGeometry(QtCore.QRect(388, 60, 65, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_x.setFont(font)
        self.select_x.setObjectName("select_x")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(540, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.your_Result = QtWidgets.QLineEdit(self.centralwidget)
        self.your_Result.setGeometry(QtCore.QRect(560, 120, 81, 31))
        self.your_Result.setObjectName("your_Result")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 160, 111, 21))
        self.label_3.setObjectName("label_3")
        self.systemResult = QtWidgets.QLineEdit(self.centralwidget)
        self.systemResult.setGeometry(QtCore.QRect(560, 180, 81, 31))
        self.systemResult.setObjectName("systemResult")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(540, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.counts = 0
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 90, 111, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.one, self.two)
        MainWindow.setTabOrder(self.two, self.three)
        MainWindow.setTabOrder(self.three, self.four)
        MainWindow.setTabOrder(self.four, self.five)
        MainWindow.setTabOrder(self.five, self.six)
        MainWindow.setTabOrder(self.six, self.seven)
        MainWindow.setTabOrder(self.seven, self.eight)
        MainWindow.setTabOrder(self.eight, self.nine)
        MainWindow.setTabOrder(self.nine, self.winner)

        self.one.clicked.connect(self.changebtn1)
        self.two.clicked.connect(self.changebtn2)
        self.three.clicked.connect(self.changebtn3)
        self.four.clicked.connect(self.changebtn4)
        self.five.clicked.connect(self.changebtn5)
        self.six.clicked.connect(self.changebtn6)
        self.seven.clicked.connect(self.changebtn7)
        self.eight.clicked.connect(self.changebtn8)
        self.nine.clicked.connect(self.changebtn9)
        self.reset.clicked.connect(self.rst)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "            WINNER               "))
        self.select_o.setText(_translate("MainWindow", "X"))
        self.select_x.setText(_translate("MainWindow", "O"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.label_2.setText(_translate("MainWindow", " Enter Player Name"))
        self.label_3.setText(_translate("MainWindow", " O SCORE :"))
        self.start.setText(_translate("MainWindow", "START"))
        self.label_4.setText(_translate("MainWindow", " X SCORE :"))
        self.your_Result.setText(str(self.p1))
        self.systemResult.setText(str(self.p2))


        self.combination= [[self.one, self.two, self.three],[self.four, self.five, self.six],
                        [self.seven, self.eight, self.nine],[self.one, self.five, self.seven],
                        [self.three, self.five, self.nine],[self.one, self.six, self.nine],
                        [self.two, self.five, self.eight], [self.three, self.four, self.seven]]

    def changebtn1(self):
        text = self.changeValue(self.one)

    def changebtn2(self):
        text = self.changeValue(self.two)

    def changebtn3(self):
        text = self.changeValue(self.three)

    def changebtn4(self):
        text = self.changeValue(self.four)

    def changebtn5(self):
        text = self.changeValue(self.five)

    def changebtn6(self):
        text = self.changeValue(self.six)

    def changebtn7(self):
        text = self.changeValue(self.seven)

    def changebtn8(self):
        text = self.changeValue(self.eight)

    def changebtn9(self):
        text = self.changeValue(self.nine)

    def rst(self):
        self.one.setText('')
        self.two.setText('')
        self.three.setText('')
        self.four.setText('')
        self.five.setText('')
        self.six.setText('')
        self.seven.setText('')
        self.eight.setText('')
        self.nine.setText('')

    def changeValue(self, btn):
        player1 = self.input1.text()
        player2 = self.input2.text()
        if player1 and player2:

            text = btn.text()

            if "X" in text or "O" in text:
                pass
            else:
                btn.setText(self.chance)
                if "X" in self.chance:
                    self.chance = "O"
                else:
                    self.chance = "X"
            self.turn += 1
            if self.turn > 4:
                check = self.checker(btn)
                is_winner = self.checker(btn)
                if is_winner:
                    if 'O' in self.chance:

                        self.winner.setText(f' {player1} win')
                        print("winner is player1")
                        self.p1=(self.p1)+1
                        self.your_Result.setText(str(self.p1))
                        self.rst()
                        self.turn=0


                        return
                    else:
                        self.winner.setText(f' {player2} win ')
                        print("winner is player2")
                        self.p2=(self.p2)+1
                        self.systemResult.setText(str(self.p2))
                        self.rst()
                        self.turn=0
                        return

            if self.turn == 9:
                print("draw")
                return
        else:
            self.winner.setText("Players names ?")

    def checker(self, btn):
        value = btn.text()
        for row in self.combination:
            if btn in row:
                flag = True
                for item in row:
                    if value == item.text():
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    return True
        return False





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
