from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Clock():
    def __init__(self):
        self.active = False
        self.minute = 0
        self.seconds = 0
        self.minutesClock = QLCDNumber()
        self.secondsClock = QLCDNumber()
    def getLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.minutesClock)
        layout.addWidget(self.secondsClock)
        return layout
    def runClock(self):
        print("work in progress")
    def displayTime(self):
        self.minutesClock.display(self.minute)
        self.secondsClock.display(self.seconds)        
    def resetClock(self):
        self.minute = 0
        self.seconds = 0
        self.displayTime()
    def preset(self, length):
        if(length == "3min"):   #TODO use enums 
            self.minute = 3
            self.seconds = 0 
        self.displayTime()     
    def startClock(self):
        if(self.active == False):
            self.active = True
            self.runClock()
    def stopClock(self):
        self.active = False    