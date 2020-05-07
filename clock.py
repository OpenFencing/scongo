from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import time
import math
class Clock():
    def __init__(self):
        self.active = False
        #self.minute = 0
        self.seconds = 50
        self.minutesClock = QLCDNumber()
        self.secondsClock = QLCDNumber()
    def getLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.minutesClock)
        layout.addWidget(self.secondsClock)
        return layout
    def runClock(self):
        while(self.active):
            time.sleep(1)
            self.seconds = self.seconds - 1
            #print(self.seconds)
            self.displayTime()
            if(self.seconds == 0):
                self.active = False 
    def displayTime(self):
        self.minutesClock.display(math.floor(self.seconds / 60))
        self.secondsClock.display(self.seconds % 60)        
    def resetClock(self):
        #self.minute = 0
        self.seconds = 0
        self.displayTime()
    def preset(self, length):
        if(length == "3min"):   #TODO use enums 
            #self.minute = 3
            self.seconds = 180 
        self.displayTime()     
    def startClock(self):
        if(self.active == False):
            self.active = True
            x =threading.Thread(target=self.runClock)   #threaded to avoid blocking the gui or the rest of the code
            x.start()
    def stopClock(self):
        self.active = False