from PyQt5.QtWidgets import QApplication, QWidget,QTabWidget, QMainWindow, QSpinBox,QMessageBox, QDialog, QListWidget, QLabel, QListWidgetItem, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon, QPen, QFont
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect, QRectF


class window_example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(350, 50, 1400, 700)
        self.setFixedWidth(700)
        self.setFixedHeight(666)
        self.setWindowTitle("\t Startup")

        self.text1 = ''
        self.text2 = ''

        self.username = "mobicash"

        self.header = QLabel("    Please Select an Option")
        self.header.setFont(QFont("times new roman", 27))
        self.header.setFixedHeight(240)
        self.header.setFixedWidth(407)

        self.btn_new = QPushButton()
        self.btn_new.setText("New User")
        self.btn_new.setStyleSheet('background-color:white')
        self.btn_new.setFont(QFont('Sanserif', 36))
        self.btn_new.setFixedWidth(407)
        self.btn_new.clicked.connect(self.openTab2)

        self.btn_existing = QPushButton()
        self.btn_existing.setText("Existing User")
        self.btn_existing.setFont(QFont('Sanserif', 36))
        self.btn_existing.setFixedWidth(407)
        self.btn_existing.setStyleSheet('background-color:white')
        self.btn_existing.clicked.connect(self.openTab3)

        self.tab1 = QWidget()
        self.tab1.layout = QVBoxLayout()
        self.tab1.setFixedWidth(453)
        self.tab1.layout.addWidget(self.header)
        self.tab1.layout.addWidget(self.btn_new)
        self.tab1.layout.addWidget(self.btn_existing)

        self.tab1.setLayout(self.tab1.layout)

        box_layout = QVBoxLayout()

        hbox1 = QHBoxLayout()

        self.label1 = QLabel("Username")
        self.label1.setFixedHeight(40)
        self.label1.setFixedWidth(48)
        self.label1.setStyleSheet("background-color:white")
        self.label1.setFont(QFont('Sanserif', 8))
        hbox1.addWidget(self.label1)

        self.username_text = QLabel()
        self.username_text.setFixedHeight(40)
        self.username_text.setFixedWidth(302)
        self.username_text.setStyleSheet("background-color:white")
        self.username_text.setFont(QFont('Sanserif', 24))
        hbox1.addWidget(self.username_text)

        self.btn1 = QPushButton(" Change\n Username")
        self.btn1.setFixedHeight(40)
        self.btn1.setFixedWidth(52)
        self.btn1.setStyleSheet("background-color:white")
        self.btn1.setFont(QFont('Sanserif', 8))
        self.btn1.clicked.connect(self.username_input)
        hbox1.addWidget(self.btn1)

        box_layout.addLayout(hbox1)

        hbox2 = QHBoxLayout()

        self.label2 = QLabel("PIN ")
        self.label2.setFixedHeight(40)
        self.label2.setFixedWidth(48)
        self.label2.setStyleSheet("background-color:white")
        self.label2.setFont(QFont('Sanserif', 12))
        hbox2.addWidget(self.label2)

        self.label = QLabel()
        self.label.setFixedHeight(40)
        self.label.setFixedWidth(302)
        self.label.setStyleSheet("background-color:white")
        self.label.setFont(QFont('Sanserif', 24))
        hbox2.addWidget(self.label)

        box_layout.addLayout(hbox2)

        vbox = QGridLayout()

        btn1 = QPushButton("1")
        btn1.setStyleSheet("background-color:white")
        btn1.setGeometry(0, 0, 120, 120)
        btn1.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn1, 0, 0)
        btn1.clicked.connect(self.value_func41)

        btn2 = QPushButton("2")
        btn2.setStyleSheet("background-color:white")
        btn2.setGeometry(120, 0, 120, 120)
        btn2.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn2, 0, 1)
        btn2.clicked.connect(self.value_func42)

        btn3 = QPushButton("3")
        btn3.setStyleSheet("background-color:white")
        btn3.setGeometry(0, 120, 120, 120)
        btn3.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn3, 0, 2)
        btn3.clicked.connect(self.value_func43)

        btn4 = QPushButton("4")
        btn4.setStyleSheet("background-color:white")
        btn4.setGeometry(120, 120, 120, 120)
        btn4.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn4, 1, 0)
        btn4.clicked.connect(self.value_func44)

        btn5 = QPushButton("5")
        btn5.setStyleSheet("background-color:white")
        btn5.setGeometry(0, 240, 120, 120)
        btn5.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn5, 1, 1)
        btn5.clicked.connect(self.value_func45)

        btn6 = QPushButton("6")
        btn6.setStyleSheet("background-color:white")
        btn6.setGeometry(120, 240, 120, 120)
        btn6.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn6, 1, 2)
        btn6.clicked.connect(self.value_func46)

        btn7 = QPushButton("7")
        btn7.setStyleSheet("background-color:white")
        btn7.setGeometry(0, 360, 120, 120)
        btn7.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn7, 2, 0)
        btn7.clicked.connect(self.value_func47)

        btn8 = QPushButton("8")
        btn8.setStyleSheet("background-color:white")
        btn8.setGeometry(120, 360, 120, 120)
        btn8.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn8, 2, 1)
        btn8.clicked.connect(self.value_func48)

        btn9 = QPushButton("9")
        btn9.setStyleSheet("background-color:white")
        btn9.setGeometry(120, 360, 120, 120)
        btn9.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn9, 2, 2)
        btn9.clicked.connect(self.value_func49)

        btn10 = QPushButton("Del")
        btn10.setStyleSheet("background-color:white")
        btn10.setGeometry(120, 360, 120, 120)
        btn10.setFont(QFont('Sanserif', 24))
        btn10.setFixedHeight(122)
        vbox.addWidget(btn10, 3, 0)
        btn10.clicked.connect(self.value_func_del)

        btn11 = QPushButton()
        btn11.setText("0")
        btn11.setStyleSheet("background-color:white")
        btn11.setGeometry(120, 360, 120, 120)
        btn11.setFont(QFont('Sanserif', 72))
        vbox.addWidget(btn11, 3, 1)
        btn11.clicked.connect(self.value_func40)

        btn12 = QPushButton("Enter")
        btn12.setStyleSheet("background-color:white")
        btn12.setGeometry(120, 360, 120, 120)
        btn12.setFont(QFont('Sanserif', 16))
        btn12.setFixedHeight(122)
        vbox.addWidget(btn12, 3, 2)
        btn12.clicked.connect(self.value_func_enter_new)

        box_layout.addLayout(vbox)
        self.tab2 = QWidget()
        self.setFixedWidth(453)
        self.tab2.setLayout(box_layout)

        box_layout2 = QVBoxLayout()

        hbox3 = QHBoxLayout()

        self.label3 = QLabel("Username")
        self.label3.setFixedHeight(40)
        self.label3.setFixedWidth(48)
        self.label3.setStyleSheet("background-color:white")
        self.label3.setFont(QFont('Sanserif', 8))
        hbox3.addWidget(self.label3)

        self.username_text2 = QLabel()
        self.username_text2.setFixedHeight(40)
        self.username_text2.setFixedWidth(302)
        self.username_text2.setStyleSheet("background-color:white")
        self.username_text2.setFont(QFont('Sanserif', 24))
        hbox3.addWidget(self.username_text2)

        self.btn2 = QPushButton(" Change\n Username")
        self.btn2.setFixedHeight(40)
        self.btn2.setFixedWidth(52)
        self.btn2.setStyleSheet("background-color:white")
        self.btn2.setFont(QFont('Sanserif', 8))
        self.btn2.clicked.connect(self.username_input)
        hbox3.addWidget(self.btn2)

        box_layout2.addLayout(hbox3)

        hbox4 = QHBoxLayout()

        self.label4 = QLabel("PIN ")
        self.label4.setFixedHeight(40)
        self.label4.setFixedWidth(27)
        self.label4.setStyleSheet("background-color:white")
        self.label4.setFont(QFont('Sanserif', 12))
        hbox4.addWidget(self.label4)

        self.label5 = QLabel()
        self.label5.setFixedHeight(40)
        self.label5.setFixedWidth(302)
        self.label5.setStyleSheet("background-color:white")
        self.label5.setFont(QFont('Sanserif', 24))
        hbox4.addWidget(self.label5)

        box_layout2.addLayout(hbox4)

        vbox2 = QGridLayout()

        btnx1 = QPushButton("1")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func1)

        btnx2 = QPushButton("2")
        btnx2.setStyleSheet("background-color:white")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func2)

        btnx3 = QPushButton("3")
        btnx3.setStyleSheet("background-color:white")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func3)

        btnx4 = QPushButton("4")
        btnx4.setStyleSheet("background-color:white")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func4)

        btnx5 = QPushButton("5")
        btnx5.setStyleSheet("background-color:white")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func5)

        btnx6 = QPushButton("6")
        btnx6.setStyleSheet("background-color:white")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func6)

        btnx7 = QPushButton("7")
        btnx7.setStyleSheet("background-color:white")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func7)

        btnx8 = QPushButton("8")
        btnx8.setStyleSheet("background-color:white")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func8)

        btnx9 = QPushButton("9")
        btnx9.setStyleSheet("background-color:white")
        btnx9.setGeometry(120, 360, 120, 120)
        btnx9.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx9, 2, 2)
        btnx9.clicked.connect(self.value_func9)

        btnx10 = QPushButton("Del")
        btnx10.setStyleSheet("background-color:white")
        btnx10.setGeometry(120, 360, 120, 120)
        btnx10.setFont(QFont('Sanserif', 24))
        btnx10.setFixedHeight(122)
        vbox2.addWidget(btnx10, 3, 0)
        btnx10.clicked.connect(self.value_func_del2)

        btnx11 = QPushButton("0")
        btnx11.setStyleSheet("background-color:white")
        btnx11.setGeometry(120, 360, 120, 120)
        btnx11.setFont(QFont('Sanserif', 72))
        vbox2.addWidget(btnx11, 3, 1)
        btnx11.clicked.connect(self.value_func0)

        btnx12 = QPushButton("Enter")
        btnx12.setStyleSheet("background-color:white")
        btnx12.setGeometry(120, 360, 120, 120)
        btnx12.setFont(QFont('Sanserif', 16))
        btnx12.setFixedHeight(122)
        vbox2.addWidget(btnx12, 3, 2)
        btnx12.clicked.connect(self.value_func_enter_existing)

        box_layout2.addLayout(vbox2)
        self.tab3 = QWidget()
        self.setFixedWidth(453)
        self.tab3.setLayout(box_layout2)


        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab1, 'Tab 1')
        self.tabs1.addTab(self.tab2, 'Tab2')
        self.tabs1.addTab(self.tab3, 'Tab 3')

        vbox4 = QVBoxLayout()

        vbox4.addWidget(self.tabs1)

        self.setLayout(vbox4)

        self.show()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:

        if event.text() == '1':
            if self.tabs1.currentIndex() == 1:
                self.value_func41()
            elif self.tabs1.currentIndex() == 2:
                self.value_func1()

        if event.text() == '2':
            if self.tabs1.currentIndex() == 1:
                self.value_func42()
            elif self.tabs1.currentIndex() == 2:
                self.value_func2()

        if event.text() == '3':
            if self.tabs1.currentIndex() == 1:
                self.value_func43()
            elif self.tabs1.currentIndex() == 2:
                self.value_func3()

        if event.text() == '4':
            if self.tabs1.currentIndex() == 1:
                self.value_func44()
            elif self.tabs1.currentIndex() == 2:
                self.value_func4()

        if event.text() == '5':
            if self.tabs1.currentIndex() == 1:
                self.value_func45()
            elif self.tabs1.currentIndex() == 2:
                self.value_func5()

        if event.text() == '6':
            if self.tabs1.currentIndex() == 1:
                self.value_func46()
            elif self.tabs1.currentIndex() == 2:
                self.value_func6()

        if event.text() == '7':
            if self.tabs1.currentIndex() == 1:
                self.value_func47()
            elif self.tabs1.currentIndex() == 2:
                self.value_func7()

        if event.text() == '8':
            if self.tabs1.currentIndex() == 1:
                self.value_func48()
            elif self.tabs1.currentIndex() == 2:
                self.value_func8()

        if event.text() == '9':
            if self.tabs1.currentIndex() == 1:
                self.value_func49()
            elif self.tabs1.currentIndex() == 2:
                self.value_func9()

        if event.text() == '0':
            if self.tabs1.currentIndex() == 1:
                self.value_func40()
            elif self.tabs1.currentIndex() == 2:
                self.value_func0()

        if event.key() == 16777219:
            if self.tabs1.currentIndex() == 1:
                self.value_func_del()
            elif self.tabs1.currentIndex() == 2:
                self.value_func_del2()

        if event.key() == 16777223:
            if self.tabs1.currentIndex() == 1:
                self.value_func_del()
            elif self.tabs1.currentIndex() == 2:
                self.value_func_del2()

        if event.key() == 16777221:
            if self.tabs1.currentIndex() == 1:
                self.value_func_enter_new()
            elif self.tabs1.currentIndex() == 2:
                self.value_func_enter_existing()

    def openTab2(self):
        QTabWidget.setCurrentIndex(self.tabs1, 1)
        self.username_input()
        self.username_text.setText(self.username)

    def openTab3(self):
        QTabWidget.setCurrentIndex(self.tabs1, 2)
        self.username_input()
        self.username_text2.setText(self.username)

    def value_func41(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '1'

    def value_func42(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '2'

    def value_func43(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '3'

    def value_func44(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '4'

    def value_func45(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '5'

    def value_func46(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '6'

    def value_func47(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '7'

    def value_func48(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '8'

    def value_func49(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '9'

    def value_func40(self):
        text = self.label.text().lstrip().rstrip()
        self.label.setText('    ' + text + '*')
        self.text1 = self.text1 + '0'

    def value_func_del(self):
        text = self.label.text().lstrip().rstrip()
        if len(text) < 1:
            return
        text = [item for item in text]
        index = len(text) - 1
        a = text.pop(index)
        new_text = ''
        for i in text:
            new_text = new_text + i
        if new_text == '':
            self.label.setText(new_text)
        else:
            self.label.setText('    ' + new_text)

        text2 = [item for item in self.text1]
        index = len(text2) - 1
        a = text2.pop(index)
        new_text2 = ''
        for i in text2:
            new_text2 = new_text2 + i
        self.text1 = new_text2

    def value_func1(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '1'

    def value_func2(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '2'

    def value_func3(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '3'

    def value_func4(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '4'

    def value_func5(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '5'

    def value_func6(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '6'

    def value_func7(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '7'

    def value_func8(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '8'

    def value_func9(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '9'

    def value_func0(self):
        text = self.label5.text().lstrip().rstrip()
        self.label5.setText('    ' + text + '*')
        self.text2 = self.text2 + '0'

    def value_func_del2(self):
        text = self.label5.text().lstrip().rstrip()
        if len(text) < 1:
            return
        text = [item for item in text]
        index = len(text) - 1
        a = text.pop(index)
        new_text = ''
        for i in text:
            new_text = new_text + i
        if new_text == '':
            self.label5.setText(new_text)
        else:
            self.label5.setText('    ' + new_text)

        text2 = [item for item in self.text2]
        index = len(text2) - 1
        a = text2.pop(index)
        new_text2 = ''
        for i in text2:
            new_text2 = new_text2 + i
        self.text2 = new_text2

    def value_func_enter_new(self):
        clearance = True
        text = self.text1
        fhandle_append = open('pin.txt', 'a')
        fhandle_read = open('pin.txt', 'r')
        for data in fhandle_read:
            if data.lstrip().rstrip().split()[1] == self.username.lstrip().rstrip():
                clearance = False

        if clearance:
            fhandle_append.writelines(' Username:\t' + self.username.lstrip().rstrip() + "\t,\tPIN:\t" + text + " \n")
        elif clearance == False:
            QMessageBox.information(self, "\tInformation", "\tUsername already exists\n\n\t Please try another one")
            return
        fhandle_append.close()
        QMessageBox.information(self, "\tInformation", "\tPIN saved Successfully")
        self.label.setText("")
        self.text1 = ''
        self.username_text.setText(" ")
        QTabWidget.setCurrentIndex(self.tabs1, 0)


    def value_func_enter_existing(self):
        password = False
        text = self.text2.lstrip().rstrip()
        username = self.username_text2.text().lstrip().rstrip()
        fhandle_read = open('pin.txt', 'r')
        found = False
        line_number = ''
        for i, line in enumerate(fhandle_read):
            if line.lstrip().rstrip().split()[1] == username:
                if line.lstrip().rstrip().split()[4] == text:
                    line_number = line_number + str(i + 1)
                    password = True
                found = True

        fhandle_read.close()
        if found:
            if password:
                QMessageBox.information(self, "\tInformation", "\tID with Username\n\t{} \n\tFound\n\n\tat line number \n\t\t{}".format(username, line_number))
            elif password == False:
                QMessageBox.information(self, "\tInformation", "\tIncorrect PIN\n\n\t Please try again")
                return
        elif found == False:
            QMessageBox.information(self, "\tInformation", "\tID with Username\n\t{} \n\t   Not  Found".format(username))

        self.label5.setText("")
        self.text2 = ''
        self.username_text2.setText(" ")
        QTabWidget.setCurrentIndex(self.tabs1, 0)

    def username_input(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:white")
        settings_dialog.setWindowTitle("\ttext file")
        settings_dialog.setGeometry(200, 120, 400, 300)
        box_layout = QVBoxLayout()

        self.tf_label = QLabel("\tEnter the User-name below\t")
        self.tf_label.setFont(QFont("times new roman", 36))
        box_layout.addWidget(self.tf_label)

        self.ledit = QLineEdit()
        self.ledit.setFixedHeight(60)
        self.ledit.setStyleSheet("background-color:white")
        self.ledit.setFont(QFont('Sanserif', 24))
        box_layout.addWidget(self.ledit)

        self.proceed_btn = QPushButton("PROCEED")
        self.proceed_btn.setFont(QFont('times new roman', 36))
        box_layout.addWidget(self.proceed_btn)
        self.proceed_btn.clicked.connect(self.close_dialog)
        self.proceed_btn.clicked.connect(lambda: settings_dialog.close())

        settings_dialog.setLayout(box_layout)
        settings_dialog.exec_()

    def close_dialog(self):
        self.username = self.ledit.text().lstrip().rstrip()
        if self.tabs1.currentIndex() == 1:
            self.username_text.setText(self.username)
        elif self.tabs1.currentIndex() == 2:
            self.username_text2.setText(self.username)






app = QApplication(sys.argv)
"""style = '''
        QWidget{
            background: #00ffa2
        }        
        
        QLabel{
                background: #5885f5;
                border: 12px solid #00FFFF;
                border-radius: 120px;
                padding: -12px;
        }
        QLineEdit {
                background: #547812;
                border: 2px solid #00FFFF;
                border-radius: 2px;
                padding: 2px;
                color: #13CF54;
        }
        QPushButton
        {
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            outline: none;
            color: #0577a8;   
            background: yellow;
        }
        QPushButton:hover{
                background: #f00;
        }
'''
"""
# app.setStyleSheet(style)

window = window_example()
window.show()
sys.exit(app.exec_())





