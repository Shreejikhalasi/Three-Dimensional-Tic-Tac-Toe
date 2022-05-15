from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("3d.ui", self)

		# Define A Counter To Keep Track Of Who's Turn It IS
		self.counter = 0

		# Define our widgets
		self.button1 = self.findChild(QPushButton, "pushButton_1")
		self.button2 = self.findChild(QPushButton, "pushButton_2")
		self.button3 = self.findChild(QPushButton, "pushButton_3")
		self.button4 = self.findChild(QPushButton, "pushButton_4")
		self.button5 = self.findChild(QPushButton, "pushButton_5")
		self.button6 = self.findChild(QPushButton, "pushButton_6")
		self.button7 = self.findChild(QPushButton, "pushButton_7")
		self.button8 = self.findChild(QPushButton, "pushButton_8")
		self.button9 = self.findChild(QPushButton, "pushButton_9")
		self.button10 = self.findChild(QPushButton,"pushButton_10")
		self.button11 = self.findChild(QPushButton,"pushButton_11")
		self.button12 = self.findChild(QPushButton,"pushButton_12")
		self.button13 = self.findChild(QPushButton,"pushButton_13")
		self.button14 = self.findChild(QPushButton,"pushButton_14")
		self.button15 = self.findChild(QPushButton,"pushButton_15")
		self.button16 = self.findChild(QPushButton,"pushButton_16")
		self.button17 = self.findChild(QPushButton,"pushButton_17")
		self.button18 = self.findChild(QPushButton,"pushButton_18")
		self.button19 = self.findChild(QPushButton,"pushButton_19")
		self.button20 = self.findChild(QPushButton,"pushButton_20")
		self.button21 = self.findChild(QPushButton,"pushButton_21")
		self.button22 = self.findChild(QPushButton,"pushButton_22")
		self.button23 = self.findChild(QPushButton,"pushButton_23")
		self.button24 = self.findChild(QPushButton,"pushButton_24")
		self.button25 = self.findChild(QPushButton,"pushButton_25")
		self.button26 = self.findChild(QPushButton,"pushButton_26")
		self.button27 = self.findChild(QPushButton,"pushButton_27")
		self.button28 = self.findChild(QPushButton,"pushButton_28")
		self.label = self.findChild(QLabel, "label")

		# Click The Button
		self.button1.clicked.connect(lambda: self.clicker(self.button1))
		self.button2.clicked.connect(lambda: self.clicker(self.button2))
		self.button3.clicked.connect(lambda: self.clicker(self.button3))
		self.button4.clicked.connect(lambda: self.clicker(self.button4))
		self.button5.clicked.connect(lambda: self.clicker(self.button5))
		self.button6.clicked.connect(lambda: self.clicker(self.button6))
		self.button7.clicked.connect(lambda: self.clicker(self.button7))
		self.button8.clicked.connect(lambda: self.clicker(self.button8))
		self.button9.clicked.connect(lambda: self.clicker(self.button9))
		self.button10.clicked.connect(lambda: self.clicker(self.button10))
		self.button11.clicked.connect(lambda: self.clicker(self.button11))
		self.button12.clicked.connect(lambda: self.clicker(self.button12))
		self.button13.clicked.connect(lambda: self.clicker(self.button13))
		self.button14.clicked.connect(lambda: self.clicker(self.button14))
		self.button15.clicked.connect(lambda: self.clicker(self.button15))
		self.button16.clicked.connect(lambda: self.clicker(self.button16))
		self.button17.clicked.connect(lambda: self.clicker(self.button17))
		self.button18.clicked.connect(lambda: self.clicker(self.button18))
		self.button19.clicked.connect(lambda: self.clicker(self.button19))
		self.button20.clicked.connect(lambda: self.clicker(self.button20))
		self.button21.clicked.connect(lambda: self.clicker(self.button21))
		self.button22.clicked.connect(lambda: self.clicker(self.button22))
		self.button23.clicked.connect(lambda: self.clicker(self.button23))
		self.button24.clicked.connect(lambda: self.clicker(self.button24))
		self.button25.clicked.connect(lambda: self.clicker(self.button25))
		self.button26.clicked.connect(lambda: self.clicker(self.button26))
		self.button27.clicked.connect(lambda: self.clicker(self.button27))
		self.button28.clicked.connect(self.reset)
			

		# Show The App
		self.show()

	# Click The Buttons
	def clicker(self, b):
		if self.counter % 2 == 0:
			mark = "X"
			self.label.setText("O's Turn")
		else:
			mark = "O"
			self.label.setText("X's Turn")

		b.setText(mark)
		b.setEnabled(False)

		# Increment The Counter
		self.counter += 1

		

	# Start Over
	def reset(self):
		# Create a List of all our buttons
		button_list = [
		self.button1,
		self.button2,
		self.button3,
		self.button4,
		self.button5,
		self.button6,
		self.button7,
		self.button8,
		self.button9,
		self.button10,
		self.button11,
		self.button12,
		self.button13,
		self.button14,
		self.button15,
		self.button16,
		self.button17,
		self.button18,
		self.button19,
		self.button20,
		self.button21,
		self.button22,
		self.button23,
		self.button24,
		self.button25,
		self.button26,
		self.button27,]

		# Reset The Buttons
		for b in button_list:
			b.setText("")
			b.setEnabled(True)
			# Reset The Button Colors
			b.setStyleSheet('QPushButton {color: #797979;}')

		# Reset The Label
		self.label.setText("X Goes First!")

		# Reset The Counter
		self.counter = 0



	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

