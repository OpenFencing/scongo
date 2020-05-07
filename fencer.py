from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Fencer():
    def __init__(self, fencerData):
        #TODO init with dict containing fencer info
        self.hitBox = QLabel()
        self.hitBox.setPixmap(QPixmap("greenHit.jpg"))
        self.score = 0
        self.scoreScreen = QLCDNumber()

        self.name = fencerData["name"]  #TODO optional variable
        self.nameScreen = QLabel(self.name)
        self.nationality = fencerData["nationality"]   #TODO with enums
        self.nationalityScreen = QLabel(self.nationality)

        self.cardScreen = QLabel()
        self.cardScreen.setPixmap(QPixmap("cardYellow.jpg"))
        self.card = "RED"   #TODO cards with enum
    def placeWidgets(self):
        layout = QVBoxLayout()
        nameLayout = QHBoxLayout()
        nameLayout.addWidget(self.nameScreen)
        nameLayout.addWidget(self.nationalityScreen)
        layout.addLayout(nameLayout)
        layout.addWidget(self.hitBox)
        layout.addWidget(self.scoreScreen)
        layout.addWidget(self.cardScreen)
        return layout
    def updateScore(self, value):
        self.score = self.score + value
        self.scoreScreen.display(score)
    def updateCard(self, refCard):    
        if((self.card == "YELLOW" and refCard == "YELLOW") or refCard == "RED"):
            self.card = "RED"
            self.cardScreen.show()
            self.cardScreen.setPixmap(QPixmap("redCard.jpg"))
        else:
            self.cardScreen.show()
            self.card == "YELLOW"
            self.cardScreen.setPixmap(QPixmap("yellowCard.jpg"))
    def resetFencer(self):
        self.score = 0
        self.scoreScreen.display(0)

        self.card = "NOCARD"
        self.cardScreen.hide()

        #TODO Name reset