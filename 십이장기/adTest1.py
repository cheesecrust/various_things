import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(550, 200, 1000, 700)
        self.setWindowTitle("12 LongTime")

        # 사용자 인터페이스
        choseMessage = QLabel("Chose >", self)
        choseMessage.setFont(QtGui.QFont("궁서", 20))
        choseMessage.move(150, 550)

        stateMessage = QLabel("-", self)
        stateMessage.setFont(QtGui.QFont("궁서", 100))
        stateMessage.setStyleSheet("background:white")
        stateMessage.move(300, 530)
        stateMessage.resize(70, 70)

        resultMessage = QLabel("' 'P WIN", self)
        resultMessage.setFont(QtGui.QFont("궁서", 20))
        resultMessage.move(650, 550)

        firstPlayer = QLabel("1P", self)
        firstPlayer.setFont(QtGui.QFont("궁서", 20))
        firstPlayer.setStyleSheet("color:blue")
        secondPlayer = QLabel("2P", self)
        secondPlayer.setFont(QtGui.QFont("궁서", 20))
        secondPlayer.setStyleSheet("color:red")

        firstPlayer.move(650, 50)
        secondPlayer.move(650, 280)

        a_StealButton = QPushButton("a", self)
        a_StealButton.setFont(QtGui.QFont("궁서", 10))
        a_StealButton.setStyleSheet("color:blue")
        a_StealButton.resize(50, 50)
        a_StealButton.move(650, 110)

        b_StealButton = QPushButton("b", self)
        b_StealButton.setFont(QtGui.QFont("궁서", 10))
        b_StealButton.setStyleSheet("color:blue")
        b_StealButton.resize(50, 50)
        b_StealButton.move(720, 110)

        c_StealButton = QPushButton("c", self)
        c_StealButton.setFont(QtGui.QFont("궁서", 10))
        c_StealButton.setStyleSheet("color:blue")
        c_StealButton.resize(50, 50)
        c_StealButton.move(790, 110)

        d_StealButton = QPushButton("d", self)
        d_StealButton.setFont(QtGui.QFont("궁서", 10))
        d_StealButton.setStyleSheet("color:blue")
        d_StealButton.resize(50, 50)
        d_StealButton.move(650, 200)

        e_StealButton = QPushButton("e", self)
        e_StealButton.setFont(QtGui.QFont("궁서", 10))
        e_StealButton.setStyleSheet("color:blue")
        e_StealButton.resize(50, 50)
        e_StealButton.move(720, 200)

        f_StealButton = QPushButton("f", self)
        f_StealButton.setFont(QtGui.QFont("궁서", 10))
        f_StealButton.setStyleSheet("color:blue")
        f_StealButton.resize(50, 50)
        f_StealButton.move(790, 200)

        g_StealButton = QPushButton("g", self)
        g_StealButton.setFont(QtGui.QFont("궁서", 10))
        g_StealButton.setStyleSheet("color:blue")
        g_StealButton.resize(50, 50)
        g_StealButton.move(650, 340)

        h_StealButton = QPushButton("h", self)
        h_StealButton.setFont(QtGui.QFont("궁서", 10))
        h_StealButton.setStyleSheet("color:blue")
        h_StealButton.resize(50, 50)
        h_StealButton.move(720, 340)

        i_StealButton = QPushButton("i", self)
        i_StealButton.setFont(QtGui.QFont("궁서", 10))
        i_StealButton.setStyleSheet("color:blue")
        i_StealButton.resize(50, 50)
        i_StealButton.move(790, 340)

        j_StealButton = QPushButton("j", self)
        j_StealButton.setFont(QtGui.QFont("궁서", 10))
        j_StealButton.setStyleSheet("color:blue")
        j_StealButton.resize(50, 50)
        j_StealButton.move(650, 430)

        k_StealButton = QPushButton("k", self)
        k_StealButton.setFont(QtGui.QFont("궁서", 10))
        k_StealButton.setStyleSheet("color:blue")
        k_StealButton.resize(50, 50)
        k_StealButton.move(720, 430)

        l_StealButton = QPushButton("l", self)
        l_StealButton.setFont(QtGui.QFont("궁서", 10))
        l_StealButton.setStyleSheet("color:blue")
        l_StealButton.resize(50, 50)
        l_StealButton.move(790, 430)

        # 장기 map
        self.A_button = QPushButton("相", self)
        self.A_button.setFont(QtGui.QFont("궁서", 20))
        self.A_button.setStyleSheet("color:blue; background:yellow")
        self.A_button.resize(100, 100)
        self.A_button.move(50, 50)

        self.B_button = QPushButton("-", self)
        self.B_button.setFont(QtGui.QFont("궁서", 20))
        self.B_button.setStyleSheet("color:blue; background:yellow")
        self.B_button.resize(100, 100)
        self.B_button.move(200, 50)

        self.C_button = QPushButton("-", self)
        self.C_button.setFont(QtGui.QFont("궁서", 20))
        self.C_button.setStyleSheet("color:red; background:teal")
        self.C_button.resize(100, 100)
        self.C_button.move(350, 50)

        self.D_button = QPushButton("將", self)
        self.D_button.setFont(QtGui.QFont("궁서", 20))
        self.D_button.setStyleSheet("color:red; background:teal")
        self.D_button.resize(100, 100)
        self.D_button.move(500, 50)

        self.E_button = QPushButton("王", self)
        self.E_button.setFont(QtGui.QFont("궁서", 20))
        self.E_button.setStyleSheet("color:blue; background:yellow")
        self.E_button.resize(100, 100)
        self.E_button.move(50, 200)

        self.F_button = QPushButton("子", self)
        self.F_button.setFont(QtGui.QFont("궁서", 20))
        self.F_button.setStyleSheet("color:blue; background:yellow")
        self.F_button.resize(100, 100)
        self.F_button.move(200, 200)

        self.G_button = QPushButton("子", self)
        self.G_button.setFont(QtGui.QFont("궁서", 20))
        self.G_button.setStyleSheet("color:red; background:teal")
        self.G_button.resize(100, 100)
        self.G_button.move(350, 200)

        self.H_button = QPushButton("王", self)
        self.H_button.setFont(QtGui.QFont("궁서", 20))
        self.H_button.setStyleSheet("color:red; background:teal")
        self.H_button.resize(100, 100)
        self.H_button.move(500, 200)

        self.I_button = QPushButton("將", self)
        self.I_button.setFont(QtGui.QFont("궁서", 20))
        self.I_button.setStyleSheet("color:blue; background:yellow")
        self.I_button.resize(100, 100)
        self.I_button.move(50, 350)

        self.J_button = QPushButton("-", self)
        self.J_button.setFont(QtGui.QFont("궁서", 20))
        self.J_button.setStyleSheet("color:blue; background:yellow")
        self.J_button.resize(100, 100)
        self.J_button.move(200, 350)

        self.K_button = QPushButton("-", self)
        self.K_button.setFont(QtGui.QFont("궁서", 20))
        self.K_button.setStyleSheet("color:red; background:teal")
        self.K_button.resize(100, 100)
        self.K_button.move(350, 350)

        self.L_button = QPushButton("將", self)
        self.L_button.setFont(QtGui.QFont("궁서", 20))
        self.L_button.setStyleSheet("color:red; background:teal")
        self.L_button.resize(100, 100)
        self.L_button.move(500, 350)


        # 클릭 이후 상태창


        #pybutton = QPushButton('Click me', self)
        self.A_button.clicked.connect(self.mapClickMethod)
        self.B_button.clicked.connect(self.mapClickMethod)
        self.C_button.clicked.connect(self.mapClickMethod)
        self.D_button.clicked.connect(self.mapClickMethod)
        self.E_button.clicked.connect(self.mapClickMethod)
        self.F_button.clicked.connect(self.mapClickMethod)
        self.G_button.clicked.connect(self.mapClickMethod)
        self.H_button.clicked.connect(self.mapClickMethod)
        self.I_button.clicked.connect(self.mapClickMethod)
        self.J_button.clicked.connect(self.mapClickMethod)
        self.K_button.clicked.connect(self.mapClickMethod)
        self.L_button.clicked.connect(self.mapClickMethod)
        #pybutton.resize(100,32)
        #pybutton.move(50, 50)

    def mapClickMethod(self):
        button = self.sender()
        key = button.text()
        print(key)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )