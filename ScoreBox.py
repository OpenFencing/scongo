from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from fencer import Fencer
from clock import Clock
class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("Scoring machine")
		self.fencerRed = Fencer({"name" : "Red Leftie", "nationality" : "PYT"})
		self.fencerGreen = Fencer({"name" : "Green Righty", "nationality" : "CPP"})
		self.clock = Clock()
		print("got this far")
		layotOuter = QVBoxLayout()
		layotOuter.addLayout(self.clock.getLayout())
		layoutFencers = QHBoxLayout()
		layoutFencers.addLayout(self.fencerRed.placeWidgets())
		layoutFencers.addLayout(self.fencerGreen.placeWidgets())
		widget = QWidget()
		layotOuter.addLayout(layoutFencers)
		widget.setLayout(layotOuter)
		self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.clock.startClock()
window.show()
app.exec_()	
