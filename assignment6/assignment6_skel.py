import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        name = QLabel("Name:")
        age = QLabel("Age:")
        score = QLabel("Score:")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(name)
        hbox_1.addWidget(self.nameEdit)
        hbox_1.addWidget(age)
        hbox_1.addWidget(self.ageEdit)
        hbox_1.addWidget(score)
        hbox_1.addWidget(self.scoreEdit)

        amount = QLabel("Amount:")
        key = QLabel("Key:")

        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItems(['Name', 'Age', 'Score'])

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(amount)
        hbox_2.addWidget(self.amountEdit)
        hbox_2.addWidget(key)
        hbox_2.addWidget(self.keyEdit)

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        addButton.clicked.connect(self.add)
        delButton.clicked.connect(self.delete)
        findButton.clicked.connect(self.find)
        incButton.clicked.connect(self.inc)
        showButton.clicked.connect(self.shower)

        hbox_3 = QHBoxLayout()
        hbox_3.addStretch(1)
        hbox_3.addWidget(addButton)
        hbox_3.addWidget(delButton)
        hbox_3.addWidget(findButton)
        hbox_3.addWidget(incButton)
        hbox_3.addWidget(showButton)

        result = QLabel("Result:")
        self.resultEdit = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def add(self):
        self.scoredb.append({"Name":self.nameEdit.text(), "Age":int(self.ageEdit.text()), "Score":int(self.scoreEdit.text())})
        self.writeScoreDB()
        self.readScoreDB()

    def delete(self):
        if self.keyEdit.currentText() == "Name":
            tmp = []
            for l in self.scoredb:
                if l['Name'] == self.nameEdit.text():
                    tmp.append(self.scoredb.index(l))
            j = 0
            for i in tmp:
                del self.scoredb[i - j]
                j += 1
            else:
                self.writeScoreDB()
                self.readScoreDB()
        elif self.keyEdit.currentText() == "Age":
            tmp = []
            for l in self.scoredb:
                if l['Age'] == int(self.ageEdit.text()):
                    tmp.append(self.scoredb.index(l))
            j =0
            for i in tmp:
                del self.scoredb[i - j]
                j += 1
            else:
                self.writeScoreDB()
                self.readScoreDB()
        elif self.keyEdit.currentText() == "Score":
            tmp = []
            for l in self.scoredb:
                if l['Score'] == int(self.scoreEdit.text()):
                    tmp.append(self.scoredb.index(l))
            j = 0
            for i in tmp:
                del self.scoredb[i - j]
                j += 1
            else:
                self.writeScoreDB()
                self.readScoreDB()

    def find(self):
        if self.keyEdit.currentText() == "Name":
            self.resultEdit.clear()
            for l in self.scoredb:
                if l['Name'] == self.nameEdit.text():
                    self.resultEdit.insertPlainText("Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))
        elif self.keyEdit.currentText() == "Age":
            self.resultEdit.clear()
            for l in self.scoredb:
                if l['Age'] == int(self.ageEdit.text()):
                    self.resultEdit.insertPlainText(
                        "Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))
        elif self.keyEdit.currentText() == "Score":
            self.resultEdit.clear()
            for l in self.scoredb:
                if l['Score'] == int(self.scoreEdit.text()):
                    self.resultEdit.insertPlainText(
                        "Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))

    def inc(self):
        for l in self.scoredb:
            if l["Name"] == self.nameEdit.text():
                tmp = int(l['Score']) + int(self.amountEdit.text())
                l['Score'] = (tmp)
        else:
            self.writeScoreDB()
            self.readScoreDB()

    def shower(self):
        if self.keyEdit.currentText() == "Name":
            self.resultEdit.clear()
            for l in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
                self.resultEdit.insertPlainText("Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))
            else:
                self.writeScoreDB()

        elif self.keyEdit.currentText() == "Age":
            self.resultEdit.clear()
            for l in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
                self.resultEdit.insertPlainText(
                    "Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))
            else:
                self.writeScoreDB()

        elif self.keyEdit.currentText() == "Score":
            print(1)
            self.resultEdit.clear()
            for l in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
                self.resultEdit.insertPlainText(
                    "Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))
            else:
                self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            fH.close()
            return
        fH.close()

        self.resultEdit.clear()
        for l in self.scoredb:
            self.resultEdit.insertPlainText("Age=%d\t Name=%s\t \t Score:%d\n" % ((l['Age']), l['Name'], (l['Score'])))

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

