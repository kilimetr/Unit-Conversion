# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os

os.chdir(r"C:\Users\dominc\OneDrive - kochind.com\Desktop\PY\UnitConverter")

import converter_allLogic_fun

class Window(QtWidgets.QMainWindow):

	def __init__(self, **kwargs):
		super().__init__()
		# super(Window, self).__init__(**kwargs)

		self.setWindowTitle("Unit Conversion")
		# self.setWindowIcon(QtGui.QIcon("xxx.png"))
		
		self.main_window()
		self.show()
		
	def main_window(self):
		formular = QtWidgets.QWidget()
		formularLayout = QtWidgets.QHBoxLayout()
		formular.setLayout(formularLayout)
		
		vbox1 = QtWidgets.QVBoxLayout()
		vbox2 = QtWidgets.QVBoxLayout()
		
		formularLayout.addStretch()
		formularLayout.addLayout(vbox1)
		formularLayout.addLayout(vbox2)
		formularLayout.addStretch()
		
		menubar     = self.menuBar()
		contentMenu = menubar.addMenu("Content")
		
		descAction = QtWidgets.QAction("Description", self)
		infoAction = QtWidgets.QAction("Info",        self)
		
		descAction.triggered.connect(self.Descbar_fun)
		infoAction.triggered.connect(self.Infobar_fun)
		
		contentMenu.addAction(descAction)
		contentMenu.addAction(infoAction)
		
		
		self.area_pb        = QtWidgets.QPushButton("Area",                      self)
		self.heatval_pb     = QtWidgets.QPushButton("Heat Volumetric Flow Rate", self)
		self.dens_pb        = QtWidgets.QPushButton("Density",                   self)

		vbox1.addWidget(self.area_pb)
		vbox1.addWidget(self.heatval_pb)
		vbox1.addWidget(self.dens_pb)

		self.massfrac_pb    = QtWidgets.QPushButton("Mass Fraction",            self)
		self.powheatfl_pb   = QtWidgets.QPushButton("Power and Heat Flow Rate", self)
		self.pressstres_pb  = QtWidgets.QPushButton("Pressure and Stress",      self)
		
		vbox2.addWidget(self.massfrac_pb)
		vbox2.addWidget(self.powheatfl_pb)
		vbox2.addWidget(self.pressstres_pb)
		
		
		self.setCentralWidget(formular)
		
		
		self.area_pb.clicked.connect(self.area_win)
		self.heatval_pb.clicked.connect(self.heatval_win)
		self.dens_pb.clicked.connect(self.dens_win)
		
		self.massfrac_pb.clicked.connect(self.massfrac_win)
		self.powheatfl_pb.clicked.connect(self.powheatfl_win)
		self.pressstres_pb.clicked.connect(self.pressstres_win)		
		
		
	def Descbar_fun(self):
		choice = QtWidgets.QMessageBox.information(self, "Description", "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01", 
				 QtWidgets.QMessageBox.Ok)
	
	
	def Infobar_fun(self):
		choice = QtWidgets.QMessageBox.information(self, "Information", "Version: 1.0;\n" "Author: Dominik Capkovic;\n" "Contact: domcapkovic@gmail.com;\n"
				 "LinkedIn Profile: https://www.linkedin.com/in/dominik-%C4%8Dapkovi%C4%8D-b0ab8575/ ", QtWidgets.QMessageBox.Ok)
	
	
	def area_win(self):
		self.area_win2 = converter_allLogic_fun.Area_Win()
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
okno = Window()
# okno.show()
sys.exit(aplikace.exec())