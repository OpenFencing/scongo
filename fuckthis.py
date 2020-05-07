from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("My Awesome App")
		layout = QGridLayout()
		self.ScoreRed = QLCDNumber(4)
		self.ScoreGreen = QLCDNumber(5)
		self.BoxRed = QLabel("RED HITBOX")
		self.BoxRed.setPixmap(QPixmap("redHit.jpg"))
		self.BoxGreen = QLabel("GREEN HITBOX")
		self.BoxGreen.setPixmap(QPixmap("greenHit.jpg"))
		self.CardRed = QLabel("RED Card")
		self.CardRed.setPixmap(QPixmap("cardYellow.jpg"))
		self.CardGreen = QLabel("Card Green")
		self.CardGreen.setPixmap(QPixmap("cardYellow.jpg"))
		self.TimerM = QLCDNumber()
		self.Round = QLabel("1/9")
		self.TimerM.display(1)
		self.TimerS = QLCDNumber()


		self.TimerS.display(59)


		self.ScoreGreen.display(14)
		self.ScoreRed.display(15)
		
		
		layout.addWidget(self.BoxRed, 1, 1)
		layout.addWidget(self.BoxGreen, 1,4)
		layout.addWidget(self.CardRed, 1, 0)
		layout.addWidget(self.CardGreen,1, 5)
		layout.addWidget(self.TimerM, 0, 2)
		layout.addWidget(self.TimerS, 0, 3)
		layout.addWidget(self.Round, 1,2)
		layout.addWidget(self.ScoreGreen, 2, 4)
		layout.addWidget(self.ScoreRed, 2, 1)
		widget = QWidget()
        widget.setLayout(layout)	
		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
        self.setCentralWidget(widget)
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
print(window.BoxGreen)
app.exec_()
print("did something")

# Your application won't reach here until you exit and the event 
# loop has stopped