import pickle
from PyQt5.QtWidgets import *


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.dbfilename = 'halligalli_scores.txt'
        self.string=''
        fH = open(self.dbfilename, 'rb')
        try:
            self.scoredb = pickle.load(fH)
        except EOFError:
            self.scoredb = []
        self.showScoreDB(self.scoredb)

    def initUI(self):
        lbl1 = QLabel('현재 1등은 ')
        self.nameedit =QLineEdit()
        self.nameedit.setReadOnly(True)
        lbl2 = QLabel('점수는 ')
        self.scoreedit= QLineEdit()
        self.scoreedit.setReadOnly(True)
        hbox = QHBoxLayout()
        hbox.addWidget(lbl1)
        hbox.addWidget(self.nameedit)
        hbox.addWidget(lbl2)
        hbox.addWidget(self.scoreedit)
        self.display = QTextEdit()
        self.display.setReadOnly(True)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.display)

        self.setLayout(vbox)
        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle("Ranking")
        self.show()


    def addScoreDB(self, name, cards):
        text = {"name":name, "cards":cards}
        self.scoredb += [text]
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        self.showScoreDB(self.scoredb)
        fH.close()


    def showScoreDB(self, db):
        string = ''

        for p in sorted(db,reverse=True, key=lambda db: int(db["cards"])):
            for attr in sorted(p):
                string += attr + "=" + str(p[attr]) + ' '
            string += "\n"
        self.display.setText(string)
        try:
            string = string.split('=')
            string1 = string[1].split(' ')
            string2 = string[2].split(' ')
            self.scoreedit.setText(string1[0])
            self.nameedit.setText(string2[0])
        except:
            pass