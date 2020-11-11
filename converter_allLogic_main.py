# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os

os.chdir(r"C:\Users\dominc\OneDrive - kochind.com\Desktop\PY\UnitConverter")

import converter_fun

class MainWindow(QtWidgets.QWidget):

	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Unit Conversion")
		self.main_window()

	def createGroup_1(self):
		groupBox_1 = QtWidgets.QGroupBox()

		self.area_pb        = QtWidgets.QPushButton("Area",                              self)
		self.heatval_pb     = QtWidgets.QPushButton("Heat Volumetric Flow Rate",         self)
		self.dens_pb        = QtWidgets.QPushButton("Density",                           self)

		vbox1 = QtWidgets.QVBoxLayout()
		vbox1.addWidget(self.area_pb)
		vbox1.addWidget(self.heatval_pb)
		vbox1.addWidget(self.dens_pb)
		vbox1.addStretch()
		groupBox_1.setLayout(vbox1)

		self.area_pb.clicked.connect(self.area_win)
		self.heatval_pb.clicked.connect(self.heatval_win)
		self.dens_pb.clicked.connect(self.dens_win)


		return groupBox_1

	def createGroup_2(self):
		groupBox_2 = QtWidgets.QGroupBox()

		self.massfrac_pb    = QtWidgets.QPushButton("Mass Fraction",                     self)
		self.powheatfl_pb   = QtWidgets.QPushButton("Power and Heat Flow Rate",            self)
		self.pressstres_pb  = QtWidgets.QPushButton("Pressure and Stress",                 self)

		vbox2 = QtWidgets.QVBoxLayout()
		vbox2.addWidget(self.massfrac_pb)
		vbox2.addWidget(self.powheatfl_pb)
		vbox2.addWidget(self.pressstres_pb)
		vbox2.addStretch()
		groupBox_2.setLayout(vbox2)

		self.massfrac_pb.clicked.connect(self.massfrac_win)
		self.powheatfl_pb.clicked.connect(self.powheatfl_win)
		self.pressstres_pb.clicked.connect(self.pressstres_win)

		return groupBox_2

	def main_window(self):
		grid1 = QtWidgets.QGridLayout()
		grid1.addWidget(self.createGroup_1(), 0, 0)
		grid1.addWidget(self.createGroup_2(), 0, 1)
		self.setLayout(grid1)
		self.show()

	def area_win(self):
		self.area_win2 = converter_fun.Area_Win()
		self.area_win2.show()

	def heatval_win(self):
		self.heatval_win2 = Heatval_Win()
		self.heatval_win2.show()

	def dens_win(self):
		self.dens_win2 = Dens_Win()
		self.dens_win2.show()

	def massfrac_win(self):
		self.massfrac_win2 = Massfrac_Win()
		self.massfrac_win2.show()

	def powheatfl_win(self):
		self.powheatfl_win2 = Powheatfl_Win()
		self.powheatfl_win2.show()

	def pressstres_win(self):
		self.pressstres_win2 = Pressstres_Win()
		self.pressstres_win2.show()
		
		
		
		
		
aplikace = QtWidgets.QApplication(sys.argv)
aplikace.setStyle("Fusion")
okno = MainWindow()
okno.show()
sys.exit(aplikace.exec())