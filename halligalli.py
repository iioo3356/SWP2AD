import sys
from PyQt5.QtCore import Qt,QSize,QTimer, QTime
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtWidgets import *
from scoreDB import ScoreDB
import random
from cards import Card
from sound import Sound
import time

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100,100,900,1000)
        self.setWindowTitle("HalliGalli")

        #초기 시작 배경화면
        oImage = QImage("halligalli_line.jpeg")
        sImage = oImage.scaled(QSize(900,1000))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.sound = Sound()
        self.cimage = Card()
        self.correct = False
        #
        # self.rd=20 #내 남은 카드 수
        # self.lu=20 #상대 남은 카드 수
        # self.ru=0 #내가 낸 카드 수
        # self.ld=0


        #start button , 함수
        self.startButton = QPushButton('Start', self)
        self.startButton.setGeometry(50, 400, 200, 50)
        self.startButton.setStyleSheet("color:blue; background:yellow")
        font = QFont()
        font.setBold(True)
        font.setPointSize(18)
        self.startButton.setFont(font)
        self.startButton.clicked.connect(self.startClicked)

        #ranking button, 함수
        self.rankingButton =QPushButton('Ranking',self)
        self.rankingButton.setGeometry(50,470,200,50)
        self.rankingButton.setFont(font)
        self.rankingButton.clicked.connect(self.rankClicked)



        self.restartButton = QPushButton('Restart?',self)
        self.restartButton.setGeometry(50,540,200,50)
        self.restartButton.setFont(font)
        self.restartButton.clicked.connect(self.startClicked)
        self.restartButton.setVisible(False)



        font.setPointSize(70)
        self.num1 = QLabel("",self)
        self.num2 = QLabel("",self)
        self.num1.setStyleSheet("color:white")
        self.num2.setStyleSheet("color:white")
        self.num1.setGeometry(620,400,100,100)
        self.num2.setGeometry(770,400,100,100)
        self.num1.setEnabled(False)
        self.num2.setEnabled(False)
        self.num1.setAlignment(Qt.AlignCenter)
        self.num2.setAlignment(Qt.AlignCenter)
        self.num1.setFont(font)
        self.num2.setFont(font)
        self.num1.setVisible(False)
        self.num2.setVisible(False)


        font.setPointSize(18)
        self.lbl = QLabel("합이 위 수들일 때만 치세요.",self)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color:black")
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.setGeometry(620,520,800,60)
        self.lbl.setVisible(False)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.time = 180
        # 라벨 글씨 키우기
        # 위에도 추가해주기

        font.setPointSize(40)

        self.rdLabel=QLabel(self)
        self.rdLabel.setGeometry(800, 900,60,60)
        self.rdLabel.setFont(font)
        self.rdLabel.setAlignment(Qt.AlignCenter)
        self.rdLabel.setStyleSheet('color:blue')
        self.rdLabel.setVisible(False)

        self.luLabel = QLabel(self)
        self.luLabel.setGeometry(30, 30, 60, 60)
        self.luLabel.setFont(font)
        self.luLabel.setAlignment(Qt.AlignCenter)
        self.luLabel.setStyleSheet('color:red')
        self.luLabel.setVisible(False)

        self.ruLabel = QLabel(self)
        self.ruLabel.setGeometry(800, 30, 60, 60)
        self.ruLabel.setFont(font)
        self.ruLabel.setAlignment(Qt.AlignCenter)
        self.ruLabel.setStyleSheet('color:black')
        self.ruLabel.setVisible(False)

        self.ldLabel = QLabel(self)
        self.ldLabel.setGeometry(30, 900, 60, 60)
        self.ldLabel.setFont(font)
        self.ldLabel.setAlignment(Qt.AlignCenter)
        self.ldLabel.setStyleSheet('color:black')
        self.ldLabel.setVisible(False)



        self.yb = QPushButton("",self)
        self.yb.setFixedHeight(330)
        self.yb.setFixedWidth(275)
        self.yb.setIcon(QIcon('back.jpg'))
        self.yb.setIconSize(QSize(275,330))
        self.yb.setVisible(False)


        self.yf = QPushButton("",self)
        self.yf.setFixedHeight(330)
        self.yf.setFixedWidth(275)
        self.yf.setIcon(QIcon('kmu.jpg'))
        self.yf.setIconSize(QSize(275,330))
        self.yf.setVisible(False)

        # card1.setGeometry(70,50,250,300)
        # card2.setGeometry(500,50,250,300)
        self.ringButton = QPushButton('',self)
        self.ringButton.setFixedHeight(306)
        self.ringButton.setFixedWidth(306)
        self.ringButton.setIcon(QIcon('ring.jpg'))
        self.ringButton.setIconSize(QSize(306,306))
        self.ringButton.setVisible(False)
        self.ringButton.clicked.connect(self.ringClicked)


        # ringButton.setGeometry(300,370,200,200)


        self.mf = QPushButton("",self)
        self.mf.setFixedHeight(330)
        self.mf.setFixedWidth(275)
        self.mf.setIcon(QIcon('kmu.jpg'))
        self.mf.setIconSize(QSize(275,330))
        self.mf.setVisible(False)


        self.mb = QPushButton("",self)
        self.mb.setFixedHeight(330)
        self.mb.setFixedWidth(275)
        self.mb.setIcon(QIcon('back.jpg'))
        self.mb.setIconSize(QSize(275, 330))
        self.mb.setVisible(False)
        self.mb.clicked.connect(self.BackClicked)

        # card3.setGeometry(70,580,250,300)
        # card4.setGeometry(500,580,250,300)
 # 사이즈가 조정
 #        self.sum(self.c1, self.c2)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.yb)
        hbox1.addWidget(self.yf)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.mf)
        hbox2.addWidget(self.mb)


        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.ringButton)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox2)
        self.setLayout(vbox1)

        self.c1 =''
        self.c2 = ''

        self.show()

        if self.time == 0:
            self.gameOver()


    def startClicked(self):
        self.sound.start()
        oImage = QImage("dark_green.jpg")
        sImage = oImage.scaled(QSize(900, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)


        self.rd = 30
        self.lu = 30
        self.ru = 0
        self.ld = 0

        self.rdLabel.setText(str(self.rd))  # 내 남은 카드 수
        self.luLabel.setText(str(self.lu))  # 내 남은 카드 수
        self.ruLabel.setText(str(self.ru))  # 내 남은 카드 수
        self.ldLabel.setText(str(self.ld))  # 내 남은 카드 수

        self.mf.setVisible(True)
        self.yf.setVisible(True)
        self.yb.setVisible(True)
        self.mb.setVisible(True)

        self.rdLabel.setVisible(True)
        self.ringButton.setVisible(True)
        self.luLabel.setVisible(True)
        self.ruLabel.setVisible(True)
        self.ldLabel.setVisible(True)

        self.number1 = random.randint(4,8)


        while True:
            self.number2 = random.randint(4,8)
            if self.number1 != self.number2:
                break


        self.num1.setText(str(self.number1))
        self.num2.setText(str(self.number2))
        self.num1.setVisible(True)
        self.num2.setVisible(True)
        self.lbl.setVisible(True)

        self.timer.start()
        self.restartButton.setVisible(False)
        self.startButton.setEnabled(True)

        # self.sum(self.c1, self.c2)


    def BackClicked(self):
        self.rt=time.time()
        self.correct = False

        self.time2 = time.time()
        if self.ru == self.ld +1:
            self.c1 = self.cimage.randomPicture()
            self.mf.setIcon(QIcon(self.c1))
            self.rd -= 1
            self.rdLabel.setText(str(self.rd))
            self.ld += 1
            self.ldLabel.setText(str(self.ld))

        if self.rd == 0 or self.lu==0:
            self.gameOver()


    def computerClicked(self):

        self.c2 = self.cimage.randomPicture()
        self.yf.setIcon(QIcon(self.c2))
        self.lu -= 1
        self.luLabel.setText(str(self.lu))

        self.ru += 1
        self.ruLabel.setText(str(self.ru))

        if self.rd == 0 or self.lu == 0:
            self.gameOver()

    def timeout(self):
        self.time -= 1
        self.startButton.setText("{}분 {}초".format(self.time//60, self.time%60))
        if self.time == 0:
            self.gameOver()
            self.time = 180

        if self.time %2 == 0 and self.ru== self.ld:
            self.computerClicked()



    def rankClicked(self):
        self.ranking = ScoreDB()
        self.ranking.show()

    def gameOver(self):
        self.sound.end()
        self.timer.stop()
        self.startButton.setText("Game Over")
        self.restartButton.setVisible(True)
        self.startButton.setEnabled(False)
        text, ok = QInputDialog.getText(self, '이름', '이름을 입력하세요.')
        if ok:
            self.ranking = ScoreDB()
            self.ranking.addScoreDB(text, self.rd)
            self.ranking.show()
    #


    def ringClicked(self):
        self.lt=time.time()
        if self.cimage.sumPicture(self.c1, self.c2) == self.number1 or self.cimage.sumPicture(self.c1, self.c2) == self.number2:
            if self.lt-self.rt<random.randint(1,4):
                self.rd += self.ru
                self.rd += self.ld
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.rdLabel.setText(str(self.rd))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))
            else:
                self.lu += self.ld
                self.lu += self.ru
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.luLabel.setText(str(self.lu))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))

        elif self.cimage.sumPicture(self.c1,self.c2) == 0 and (self.cimage.numPicture(self.c1) == self.number1 or self.cimage.numPicture(self.c1) == self.number2):
            if self.lt - self.rt < 3:
                self.rd += self.ru
                self.rd += self.ld
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.rdLabel.setText(str(self.rd))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))
            else:
                self.lu += self.ld
                self.lu += self.ru
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.luLabel.setText(str(self.lu))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))
        elif self.cimage.sumPicture(self.c1,self.c2) == 0 and (self.cimage.numPicture(self.c2) == self.number1 or self.cimage.numPicture(self.c2) == self.number2):
            if self.lt - self.rt < 3:
                self.rd += self.ru
                self.rd += self.ld
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.rdLabel.setText(str(self.rd))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))
            else:
                self.lu += self.ld
                self.lu += self.ru
                self.ld = 0
                self.ru = 0
                self.ldLabel.setText(str(self.ld))
                self.ruLabel.setText(str(self.ru))
                self.luLabel.setText(str(self.lu))
                self.yf.setIcon(QIcon('kmu.jpg'))
                self.mf.setIcon(QIcon('kmu.jpg'))
        else:
            self.lu+=1
            self.luLabel.setText(str(self.lu))
            self.rd-=1
            self.rdLabel.setText(str(self.rd))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    Mainwindow = MainWindow()
    sys.exit(app.exec_())
