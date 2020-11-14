# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Area_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Area Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel        = QtWidgets.QLabel()
		self.m2i_LinEd    = QtWidgets.QLineEdit()
		self.cm2i_LinEd   = QtWidgets.QLineEdit()

		self.LinEd_list = [self.m2i_LinEd, self.cm2i_LinEd]
		
		Label_list = [blanklabel, "m\u00B2", "cm\u00B2"]

		i = 1
		for item in self.LinEd_list:
			input_grid.addWidget(item, i, 0)
			i = i + 1

		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_group.setLayout(input_grid)

		
		self.m2i_LinEd.returnPressed.connect(self.m2TO_fun)
		self.cm2i_LinEd.returnPressed.connect(self.cm2TO_fun)

		return input_group	  
	  

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["m\u00B2", "cm\u00B2"]
		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.m2TOm2_res    = QtWidgets.QLabel("0", self)
		self.m2TOcm2_res   = QtWidgets.QLabel("0", self)

		self.cm2TOm2_res    = QtWidgets.QLabel("0", self)
		self.cm2TOcm2_res   = QtWidgets.QLabel("0", self)

		
		m2TO_Label = [self.m2TOm2_res, self.m2TOcm2_res]

		cm2TO_Label = [self.cm2TOm2_res, self.cm2TOcm2_res]

		i = 0
		for item in m2TO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in cm2TO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1


		output_group.setLayout(output_grid)

		return output_group
		
		
	def m2TO_fun(self):
		try:
			m2TOm2_proc    = float(self.m2i_LinEd.text()) * 1
			m2TOcm2_proc   = float(self.m2i_LinEd.text()) * 1e+04

			self.m2TOm2_res.setText(str(round(m2TOm2_proc,       8)))
			self.m2TOcm2_res.setText(str(round(m2TOcm2_proc,     8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
		

	def cm2TO_fun(self):
		try:
			cm2TOm2_proc    = float(self.cm2i_LinEd.text()) * 1e-04
			cm2TOcm2_proc   = float(self.cm2i_LinEd.text()) * 1

			self.cm2TOm2_res.setText(str(cm2TOm2_proc))
			self.cm2TOcm2_res.setText(str(cm2TOcm2_proc))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()

aplikace = QtWidgets.QApplication(sys.argv)
aplikace.setStyle("Fusion")