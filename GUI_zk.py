# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class MainWindow(QtWidgets.QWidget):

	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Unit Conversion")

		self.main_window()

	def createGroup_1(self):
		groupBox_1 = QtWidgets.QGroupBox()

		self.area_pb        = QtWidgets.QPushButton("Area",                              self)
		self.heatval_pb     = QtWidgets.QPushButton("Heat Value",                        self)

		vbox1 = QtWidgets.QVBoxLayout()
		vbox1.addWidget(self.area_pb)
		vbox1.addWidget(self.heatval_pb)
		vbox1.addStretch()
		groupBox_1.setLayout(vbox1)

		self.area_pb.clicked.connect(self.area_win)
		self.heatval_pb.clicked.connect(self.heatval_win)

		return groupBox_1

	def createGroup_2(self):
		groupBox_2 = QtWidgets.QGroupBox()

		self.powheatfl_pb   = QtWidgets.QPushButton("Power & Heat Flow Rate",            self)
		self.pressstres_pb  = QtWidgets.QPushButton("Pressure & Stress",                 self)

		vbox2 = QtWidgets.QVBoxLayout()
		vbox2.addWidget(self.powheatfl_pb)
		vbox2.addWidget(self.pressstres_pb)
		vbox2.addStretch()
		groupBox_2.setLayout(vbox2)

		self.powheatfl_pb.clicked.connect(self.powheatfl_win)
		self.pressstres_pb.clicked.connect(self.pressstres_win)

		return groupBox_2

	def main_window(self):
		grid = QtWidgets.QGridLayout()
		grid.addWidget(self.createGroup_1(), 0, 0)
		grid.addWidget(self.createGroup_2(), 0, 1)
		self.setLayout(grid)
		self.show()

	def area_win(self):
		self.area_win2 = Area_Win()
		self.area_win2.show()

	def heatval_win(self):
		self.heatval_win2 = Heatval_Win()
		self.heatval_win2.show()

	def powheatfl_win(self):
		self.powheatfl_win2 = Powheatfl_Win()
		self.powheatfl_win2.show()

	def pressstres_win(self):
		self.pressstres_win2 = Pressstres_Win()
		self.pressstres_win2.show()



class Area_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Area Converter")

		self.m2i_LinEd = QtWidgets.QLineEdit(self) 
		self.m2u_Label = QtWidgets.QLabel("m2",self)
		self.mm2i_LinEd = QtWidgets.QLineEdit(self)
		self.mm2u_Label = QtWidgets.QLabel(self)

	def createGroup_input(self):
		area_grid = QtWidgets.QGridLayout("Input", self)

		area_H1 = QtWidgets.QHBoxLayout()
		# area_H2 = QtWidgets.QHBoxLayout()

		area_H1.addWidget(self.m2i_LinEd)
		area_H1.addWidget(self.mm2i_LinEd)

		area_H2.addWidget(self.m2u_Label)
		area_H2.addWidget(self.mm2u_Label)

		area_grid.addWidget(area_H1, 0, 0)
		area_grid.addWidget(area_H2, 0, 1)

	def main_window(self):
		groupbox = QtWidgets.QGroupBox()

		groupbox.addWidget(self.createGroup_input)
		


class Heatval_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatval_Win")

class Powheatfl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Powheatfl_Win")

class Pressstres_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressstres_Win")



aplikace = QtWidgets.QApplication(sys.argv)
okno = MainWindow()
okno.show()
sys.exit(aplikace.exec_())

