# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Vol_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		
		self.setWindowTitle("Volumetric Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)
		
		blanklabel        = QtWidgets.QLabel()
		self.m3i_LinEd    = QtWidgets.QLineEdit()
		self.dm3i_LinEd   = QtWidgets.QLineEdit()
		self.cm3i_LinEd   = QtWidgets.QLineEdit()
		self.in3i_LinEd   = QtWidgets.QLineEdit()
		self.ft3i_LinEd	  = QtWidgets.QLineEdit()
		self.yd3i_LinEd	  = QtWidgets.QLineEdit()
		self.galUSi_LinEd = QtWidgets.QLineEdit()
		self.galUKi_LinEd = QtWidgets.QLineEdit()
		self.barri_LinEd  = QtWidgets.QLineEdit()

		Label_list = ["m\u00B3", "dm\u00B3 & l", "cm\u00B3 & ml", "in\u00B3", "ft\u00B3", "yard\u00B3", "gal<sub>US</sub>", "gal<sub>UK</sub>", "barrel<sub>oil, US</sub>"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_grid.addWidget(blanklabel,        0, 0)
		input_grid.addWidget(self.m3i_LinEd,    1, 0)
		input_grid.addWidget(self.dm3i_LinEd,   2, 0)
		input_grid.addWidget(self.cm3i_LinEd,   3, 0)
		input_grid.addWidget(self.in3i_LinEd,   4, 0)
		input_grid.addWidget(self.ft3i_LinEd,   5, 0)
		input_grid.addWidget(self.yd3i_LinEd,   6, 0)
		input_grid.addWidget(self.galUSi_LinEd, 7, 0)
		input_grid.addWidget(self.galUKi_LinEd, 8, 0)
		input_grid.addWidget(self.barri_LinEd,  9, 0)

		input_group.setLayout(input_grid)

		self.m3i_LinEd.returnPressed.connect(self.m3TO_fun)
		self.dm3i_LinEd.returnPressed.connect(self.dm3TO_fun)
		self.cm3i_LinEd.returnPressed.connect(self.cm3TO_fun)
		self.in3i_LinEd.returnPressed.connect(self.in3TO_fun)
		self.ft3i_LinEd.returnPressed.connect(self.ft3TO_fun)
		self.yd3i_LinEd.returnPressed.connect(self.yd3TO_fun)
		self.galUSi_LinEd.returnPressed.connect(self.galUSTO_fun)
		self.galUKi_LinEd.returnPressed.connect(self.galUKTO_fun)
		self.barri_LinEd.returnPressed.connect(self.barrTO_fun)

		return input_group


	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["m\u00B3", "dm\u00B3 & l", "cm\u00B3 & ml", "in\u00B3", "ft\u00B3", "yard\u00B3", "gal<sub>US</sub>", "gal<sub>UK</sub>", "barrel<sub>oil, US</sub>"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.m3TOm3_res    = QtWidgets.QLabel("0", self)
		self.m3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.m3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.m3TOin3_res   = QtWidgets.QLabel("0", self)
		self.m3TOft3_res   = QtWidgets.QLabel("0", self)
		self.m3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.m3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.m3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.m3TObarr_res  = QtWidgets.QLabel("0", self)

		self.dm3TOm3_res    = QtWidgets.QLabel("0", self)
		self.dm3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.dm3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.dm3TOin3_res   = QtWidgets.QLabel("0", self)
		self.dm3TOft3_res   = QtWidgets.QLabel("0", self)
		self.dm3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.dm3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.dm3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.dm3TObarr_res  = QtWidgets.QLabel("0", self)

		self.cm3TOm3_res    = QtWidgets.QLabel("0", self)
		self.cm3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.cm3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.cm3TOin3_res   = QtWidgets.QLabel("0", self)
		self.cm3TOft3_res   = QtWidgets.QLabel("0", self)
		self.cm3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.cm3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.cm3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.cm3TObarr_res  = QtWidgets.QLabel("0", self)

		self.in3TOm3_res    = QtWidgets.QLabel("0", self)
		self.in3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.in3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.in3TOin3_res   = QtWidgets.QLabel("0", self)
		self.in3TOft3_res   = QtWidgets.QLabel("0", self)
		self.in3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.in3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.in3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.in3TObarr_res  = QtWidgets.QLabel("0", self)

		self.ft3TOm3_res    = QtWidgets.QLabel("0", self)
		self.ft3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.ft3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.ft3TOin3_res   = QtWidgets.QLabel("0", self)
		self.ft3TOft3_res   = QtWidgets.QLabel("0", self)
		self.ft3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.ft3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.ft3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.ft3TObarr_res  = QtWidgets.QLabel("0", self)

		self.yd3TOm3_res    = QtWidgets.QLabel("0", self)
		self.yd3TOdm3_res   = QtWidgets.QLabel("0", self)
		self.yd3TOcm3_res   = QtWidgets.QLabel("0", self)
		self.yd3TOin3_res   = QtWidgets.QLabel("0", self)
		self.yd3TOft3_res   = QtWidgets.QLabel("0", self)
		self.yd3TOyd3_res   = QtWidgets.QLabel("0", self)
		self.yd3TOgalUS_res = QtWidgets.QLabel("0", self)
		self.yd3TOgalUK_res = QtWidgets.QLabel("0", self)
		self.yd3TObarr_res  = QtWidgets.QLabel("0", self)

		self.galUSTOm3_res    = QtWidgets.QLabel("0", self)
		self.galUSTOdm3_res   = QtWidgets.QLabel("0", self)
		self.galUSTOcm3_res   = QtWidgets.QLabel("0", self)
		self.galUSTOin3_res   = QtWidgets.QLabel("0", self)
		self.galUSTOft3_res   = QtWidgets.QLabel("0", self)
		self.galUSTOyd3_res   = QtWidgets.QLabel("0", self)
		self.galUSTOgalUS_res = QtWidgets.QLabel("0", self)
		self.galUSTOgalUK_res = QtWidgets.QLabel("0", self)
		self.galUSTObarr_res  = QtWidgets.QLabel("0", self)

		self.galUKTOm3_res    = QtWidgets.QLabel("0", self)
		self.galUKTOdm3_res   = QtWidgets.QLabel("0", self)
		self.galUKTOcm3_res   = QtWidgets.QLabel("0", self)
		self.galUKTOin3_res   = QtWidgets.QLabel("0", self)
		self.galUKTOft3_res   = QtWidgets.QLabel("0", self)
		self.galUKTOyd3_res   = QtWidgets.QLabel("0", self)
		self.galUKTOgalUS_res = QtWidgets.QLabel("0", self)
		self.galUKTOgalUK_res = QtWidgets.QLabel("0", self)
		self.galUKTObarr_res  = QtWidgets.QLabel("0", self)

		self.barrTOm3_res    = QtWidgets.QLabel("0", self)
		self.barrTOdm3_res   = QtWidgets.QLabel("0", self)
		self.barrTOcm3_res   = QtWidgets.QLabel("0", self)
		self.barrTOin3_res   = QtWidgets.QLabel("0", self)
		self.barrTOft3_res   = QtWidgets.QLabel("0", self)
		self.barrTOyd3_res   = QtWidgets.QLabel("0", self)
		self.barrTOgalUS_res = QtWidgets.QLabel("0", self)
		self.barrTOgalUK_res = QtWidgets.QLabel("0", self)
		self.barrTObarr_res  = QtWidgets.QLabel("0", self)

		output_grid.addWidget(self.m3TOm3_res,    1, 0)
		output_grid.addWidget(self.m3TOdm3_res,   1, 1)
		output_grid.addWidget(self.m3TOcm3_res,   1, 2)
		output_grid.addWidget(self.m3TOin3_res,   1, 3)
		output_grid.addWidget(self.m3TOft3_res,   1, 4)
		output_grid.addWidget(self.m3TOyd3_res,   1, 5)
		output_grid.addWidget(self.m3TOgalUS_res, 1, 6)
		output_grid.addWidget(self.m3TOgalUK_res, 1, 7)
		output_grid.addWidget(self.m3TObarr_res,  1, 8)

		output_grid.addWidget(self.dm3TOm3_res,    2, 0)
		output_grid.addWidget(self.dm3TOdm3_res,   2, 1)
		output_grid.addWidget(self.dm3TOcm3_res,   2, 2)
		output_grid.addWidget(self.dm3TOin3_res,   2, 3)
		output_grid.addWidget(self.dm3TOft3_res,   2, 4)
		output_grid.addWidget(self.dm3TOyd3_res,   2, 5)
		output_grid.addWidget(self.dm3TOgalUS_res, 2, 6)
		output_grid.addWidget(self.dm3TOgalUK_res, 2, 7)
		output_grid.addWidget(self.dm3TObarr_res,  2, 8)

		output_grid.addWidget(self.cm3TOm3_res,    3, 0)
		output_grid.addWidget(self.cm3TOdm3_res,   3, 1)
		output_grid.addWidget(self.cm3TOcm3_res,   3, 2)
		output_grid.addWidget(self.cm3TOin3_res,   3, 3)
		output_grid.addWidget(self.cm3TOft3_res,   3, 4)
		output_grid.addWidget(self.cm3TOyd3_res,   3, 5)
		output_grid.addWidget(self.cm3TOgalUS_res, 3, 6)
		output_grid.addWidget(self.cm3TOgalUK_res, 3, 7)
		output_grid.addWidget(self.cm3TObarr_res,  3, 8)

		output_grid.addWidget(self.in3TOm3_res,    4, 0)
		output_grid.addWidget(self.in3TOdm3_res,   4, 1)
		output_grid.addWidget(self.in3TOcm3_res,   4, 2)
		output_grid.addWidget(self.in3TOin3_res,   4, 3)
		output_grid.addWidget(self.in3TOft3_res,   4, 4)
		output_grid.addWidget(self.in3TOyd3_res,   4, 5)
		output_grid.addWidget(self.in3TOgalUS_res, 4, 6)
		output_grid.addWidget(self.in3TOgalUK_res, 4, 7)
		output_grid.addWidget(self.in3TObarr_res,  4, 8)

		output_grid.addWidget(self.ft3TOm3_res,    5, 0)
		output_grid.addWidget(self.ft3TOdm3_res,   5, 1)
		output_grid.addWidget(self.ft3TOcm3_res,   5, 2)
		output_grid.addWidget(self.ft3TOin3_res,   5, 3)
		output_grid.addWidget(self.ft3TOft3_res,   5, 4)
		output_grid.addWidget(self.ft3TOyd3_res,   5, 5)
		output_grid.addWidget(self.ft3TOgalUS_res, 5, 6)
		output_grid.addWidget(self.ft3TOgalUK_res, 5, 7)
		output_grid.addWidget(self.ft3TObarr_res,  5, 8)

		output_grid.addWidget(self.yd3TOm3_res,    6, 0)
		output_grid.addWidget(self.yd3TOdm3_res,   6, 1)
		output_grid.addWidget(self.yd3TOcm3_res,   6, 2)
		output_grid.addWidget(self.yd3TOin3_res,   6, 3)
		output_grid.addWidget(self.yd3TOft3_res,   6, 4)
		output_grid.addWidget(self.yd3TOyd3_res,   6, 5)
		output_grid.addWidget(self.yd3TOgalUS_res, 6, 6)
		output_grid.addWidget(self.yd3TOgalUK_res, 6, 7)
		output_grid.addWidget(self.yd3TObarr_res,  6, 8)

		output_grid.addWidget(self.galUSTOm3_res,    7, 0)
		output_grid.addWidget(self.galUSTOdm3_res,   7, 1)
		output_grid.addWidget(self.galUSTOcm3_res,   7, 2)
		output_grid.addWidget(self.galUSTOin3_res,   7, 3)
		output_grid.addWidget(self.galUSTOft3_res,   7, 4)
		output_grid.addWidget(self.galUSTOyd3_res,   7, 5)
		output_grid.addWidget(self.galUSTOgalUS_res, 7, 6)
		output_grid.addWidget(self.galUSTOgalUK_res, 7, 7)
		output_grid.addWidget(self.galUSTObarr_res,  7, 8)

		output_grid.addWidget(self.galUKTOm3_res,    8, 0)
		output_grid.addWidget(self.galUKTOdm3_res,   8, 1)
		output_grid.addWidget(self.galUKTOcm3_res,   8, 2)
		output_grid.addWidget(self.galUKTOin3_res,   8, 3)
		output_grid.addWidget(self.galUKTOft3_res,   8, 4)
		output_grid.addWidget(self.galUKTOyd3_res,   8, 5)
		output_grid.addWidget(self.galUKTOgalUS_res, 8, 6)
		output_grid.addWidget(self.galUKTOgalUK_res, 8, 7)
		output_grid.addWidget(self.galUKTObarr_res,  8, 8)

		output_grid.addWidget(self.barrTOm3_res,    9, 0)
		output_grid.addWidget(self.barrTOdm3_res,   9, 1)
		output_grid.addWidget(self.barrTOcm3_res,   9, 2)
		output_grid.addWidget(self.barrTOin3_res,   9, 3)
		output_grid.addWidget(self.barrTOft3_res,   9, 4)
		output_grid.addWidget(self.barrTOyd3_res,   9, 5)
		output_grid.addWidget(self.barrTOgalUS_res, 9, 6)
		output_grid.addWidget(self.barrTOgalUK_res, 9, 7)
		output_grid.addWidget(self.barrTObarr_res,  9, 8)

		output_group.setLayout(output_grid)

		return output_group

	def m3TO_fun(self):
		try:
			m3TOm3_proc    = float(self.m3i_LinEd.text()) * 1
			m3TOdm3_proc   = float(self.m3i_LinEd.text()) * 1e+03
			m3TOcm3_proc   = float(self.m3i_LinEd.text()) * 1e+06
			m3TOin3_proc   = float(self.m3i_LinEd.text()) * 6.102374e+04
			m3TOft3_proc   = float(self.m3i_LinEd.text()) * 3.531467e+01
			m3TOyd3_proc   = float(self.m3i_LinEd.text()) * 1.307951
			m3TOgalUS_proc = float(self.m3i_LinEd.text()) * 2.64172e+02
			m3TOgalUK_proc = float(self.m3i_LinEd.text()) * 2.199692e+02
			m3TObarr_proc  = float(self.m3i_LinEd.text()) * 6.28981

			self.m3TOm3_res.setText(str(round(m3TOm3_proc,       8)))
			self.m3TOdm3_res.setText(str(round(m3TOdm3_proc,     8)))
			self.m3TOcm3_res.setText(str(round(m3TOcm3_proc,     8)))
			self.m3TOin3_res.setText(str(round(m3TOin3_proc,     8)))
			self.m3TOft3_res.setText(str(round(m3TOft3_proc,     8)))
			self.m3TOyd3_res.setText(str(round(m3TOyd3_proc,     8)))
			self.m3TOgalUS_res.setText(str(round(m3TOgalUS_proc, 8)))
			self.m3TOgalUK_res.setText(str(round(m3TOgalUK_proc, 8)))
			self.m3TObarr_res.setText(str(round(m3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def dm3TO_fun(self):
		try:
			dm3TOm3_proc    = float(self.dm3i_LinEd.text()) * 1e-03
			dm3TOdm3_proc   = float(self.dm3i_LinEd.text()) * 1
			dm3TOcm3_proc   = float(self.dm3i_LinEd.text()) * 1e+03
			dm3TOin3_proc   = float(self.dm3i_LinEd.text()) * 6.102374e+01
			dm3TOft3_proc   = float(self.dm3i_LinEd.text()) * 3.531467e-02
			dm3TOyd3_proc   = float(self.dm3i_LinEd.text()) * 1.307951e-03
			dm3TOgalUS_proc = float(self.dm3i_LinEd.text()) * 2.64172e-01
			dm3TOgalUK_proc = float(self.dm3i_LinEd.text()) * 2.199692e-01
			dm3TObarr_proc  = float(self.dm3i_LinEd.text()) * 6.28981e-03

			self.dm3TOm3_res.setText(str(round(dm3TOm3_proc,       8)))
			self.dm3TOdm3_res.setText(str(round(dm3TOdm3_proc,     8)))
			self.dm3TOcm3_res.setText(str(round(dm3TOcm3_proc,     8)))
			self.dm3TOin3_res.setText(str(round(dm3TOin3_proc,     8)))
			self.dm3TOft3_res.setText(str(round(dm3TOft3_proc,     8)))
			self.dm3TOyd3_res.setText(str(round(dm3TOyd3_proc,     8)))
			self.dm3TOgalUS_res.setText(str(round(dm3TOgalUS_proc, 8)))
			self.dm3TOgalUK_res.setText(str(round(dm3TOgalUK_proc, 8)))
			self.dm3TObarr_res.setText(str(round(dm3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def cm3TO_fun(self):
		try:
			cm3TOm3_proc    = float(self.cm3i_LinEd.text()) * 1e-06
			cm3TOdm3_proc   = float(self.cm3i_LinEd.text()) * 1e-03
			cm3TOcm3_proc   = float(self.cm3i_LinEd.text()) * 1
			cm3TOin3_proc   = float(self.cm3i_LinEd.text()) * 6.102374e-02
			cm3TOft3_proc   = float(self.cm3i_LinEd.text()) * 3.531467e-05
			cm3TOyd3_proc   = float(self.cm3i_LinEd.text()) * 1.307951e-06
			cm3TOgalUS_proc = float(self.cm3i_LinEd.text()) * 2.64172e-04
			cm3TOgalUK_proc = float(self.cm3i_LinEd.text()) * 2.199692e-04
			cm3TObarr_proc  = float(self.cm3i_LinEd.text()) * 6.28981e-06

			self.cm3TOm3_res.setText(str(round(cm3TOm3_proc,       8)))
			self.cm3TOdm3_res.setText(str(round(cm3TOdm3_proc,     8)))
			self.cm3TOcm3_res.setText(str(round(cm3TOcm3_proc,     8)))
			self.cm3TOin3_res.setText(str(round(cm3TOin3_proc,     8)))
			self.cm3TOft3_res.setText(str(round(cm3TOft3_proc,     8)))
			self.cm3TOyd3_res.setText(str(round(cm3TOyd3_proc,     8)))
			self.cm3TOgalUS_res.setText(str(round(cm3TOgalUS_proc, 8)))
			self.cm3TOgalUK_res.setText(str(round(cm3TOgalUK_proc, 8)))
			self.cm3TObarr_res.setText(str(round(cm3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def in3TO_fun(self):
		try:
			in3TOm3_proc    = float(self.in3i_LinEd.text()) * 1.638706e-05
			in3TOdm3_proc   = float(self.in3i_LinEd.text()) * 1.638706e-02
			in3TOcm3_proc   = float(self.in3i_LinEd.text()) * 1.638706e+01
			in3TOin3_proc   = float(self.in3i_LinEd.text()) * 1
			in3TOft3_proc   = float(self.in3i_LinEd.text()) * 5.787037e-04
			in3TOyd3_proc   = float(self.in3i_LinEd.text()) * 2.143347e-05
			in3TOgalUS_proc = float(self.in3i_LinEd.text()) * 4.329004e-03
			in3TOgalUK_proc = float(self.in3i_LinEd.text()) * 3.604649e-03
			in3TObarr_proc  = float(self.in3i_LinEd.text()) * 1.030715e-04

			self.in3TOm3_res.setText(str(round(in3TOm3_proc,       8)))
			self.in3TOdm3_res.setText(str(round(in3TOdm3_proc,     8)))
			self.in3TOcm3_res.setText(str(round(in3TOcm3_proc,     8)))
			self.in3TOin3_res.setText(str(round(in3TOin3_proc,     8)))
			self.in3TOft3_res.setText(str(round(in3TOft3_proc,     8)))
			self.in3TOyd3_res.setText(str(round(in3TOyd3_proc,     8)))
			self.in3TOgalUS_res.setText(str(round(in3TOgalUS_proc, 8)))
			self.in3TOgalUK_res.setText(str(round(in3TOgalUK_proc, 8)))
			self.in3TObarr_res.setText(str(round(in3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ft3TO_fun(self):
		try:
			ft3TOm3_proc    = float(self.ft3i_LinEd.text()) * 2.831685e-02
			ft3TOdm3_proc   = float(self.ft3i_LinEd.text()) * 2.831685e+01
			ft3TOcm3_proc   = float(self.ft3i_LinEd.text()) * 2.831685e+04
			ft3TOin3_proc   = float(self.ft3i_LinEd.text()) * 1.728e+03
			ft3TOft3_proc   = float(self.ft3i_LinEd.text()) * 1
			ft3TOyd3_proc   = float(self.ft3i_LinEd.text()) * 3.703704e-02
			ft3TOgalUS_proc = float(self.ft3i_LinEd.text()) * 7.480520
			ft3TOgalUK_proc = float(self.ft3i_LinEd.text()) * 6.228833
			ft3TObarr_proc  = float(self.ft3i_LinEd.text()) * 1.781076e-01

			self.ft3TOm3_res.setText(str(round(ft3TOm3_proc,       8)))
			self.ft3TOdm3_res.setText(str(round(ft3TOdm3_proc,     8)))
			self.ft3TOcm3_res.setText(str(round(ft3TOcm3_proc,     8)))
			self.ft3TOin3_res.setText(str(round(ft3TOin3_proc,     8)))
			self.ft3TOft3_res.setText(str(round(ft3TOft3_proc,     8)))
			self.ft3TOyd3_res.setText(str(round(ft3TOyd3_proc,     8)))
			self.ft3TOgalUS_res.setText(str(round(ft3TOgalUS_proc, 8)))
			self.ft3TOgalUK_res.setText(str(round(ft3TOgalUK_proc, 8)))
			self.ft3TObarr_res.setText(str(round(ft3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def yd3TO_fun(self):
		try:
			yd3TOm3_proc    = float(self.yd3i_LinEd.text()) * 7.645549e-01
			yd3TOdm3_proc   = float(self.yd3i_LinEd.text()) * 7.645549e+02
			yd3TOcm3_proc   = float(self.yd3i_LinEd.text()) * 7.645549e+05
			yd3TOin3_proc   = float(self.yd3i_LinEd.text()) * 4.6656e+04
			yd3TOft3_proc   = float(self.yd3i_LinEd.text()) * 27
			yd3TOyd3_proc   = float(self.yd3i_LinEd.text()) * 1
			yd3TOgalUS_proc = float(self.yd3i_LinEd.text()) * 2.019740e+02
			yd3TOgalUK_proc = float(self.yd3i_LinEd.text()) * 1.681784e+02
			yd3TObarr_proc  = float(self.yd3i_LinEd.text()) * 4.808905

			self.yd3TOm3_res.setText(str(round(yd3TOm3_proc,       8)))
			self.yd3TOdm3_res.setText(str(round(yd3TOdm3_proc,     8)))
			self.yd3TOcm3_res.setText(str(round(yd3TOcm3_proc,     8)))
			self.yd3TOin3_res.setText(str(round(yd3TOin3_proc,     8)))
			self.yd3TOft3_res.setText(str(round(yd3TOft3_proc,     8)))
			self.yd3TOyd3_res.setText(str(round(yd3TOyd3_proc,     8)))
			self.yd3TOgalUS_res.setText(str(round(yd3TOgalUS_proc, 8)))
			self.yd3TOgalUK_res.setText(str(round(yd3TOgalUK_proc, 8)))
			self.yd3TObarr_res.setText(str(round(yd3TObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def galUSTO_fun(self):
		try:
			galUSTOm3_proc    = float(self.galUSi_LinEd.text()) * 3.785412e-03
			galUSTOdm3_proc   = float(self.galUSi_LinEd.text()) * 3.785412
			galUSTOcm3_proc   = float(self.galUSi_LinEd.text()) * 3.785412e+03
			galUSTOin3_proc   = float(self.galUSi_LinEd.text()) * 2.31e+02
			galUSTOft3_proc   = float(self.galUSi_LinEd.text()) * 1.336806e-01
			galUSTOyd3_proc   = float(self.galUSi_LinEd.text()) * 4.951132e-03
			galUSTOgalUS_proc = float(self.galUSi_LinEd.text()) * 1
			galUSTOgalUK_proc = float(self.galUSi_LinEd.text()) * 8.326739e-01
			galUSTObarr_proc  = float(self.galUSi_LinEd.text()) * 2.380952e-02

			self.galUSTOm3_res.setText(str(round(galUSTOm3_proc,       8)))
			self.galUSTOdm3_res.setText(str(round(galUSTOdm3_proc,     8)))
			self.galUSTOcm3_res.setText(str(round(galUSTOcm3_proc,     8)))
			self.galUSTOin3_res.setText(str(round(galUSTOin3_proc,     8)))
			self.galUSTOft3_res.setText(str(round(galUSTOft3_proc,     8)))
			self.galUSTOyd3_res.setText(str(round(galUSTOyd3_proc,     8)))
			self.galUSTOgalUS_res.setText(str(round(galUSTOgalUS_proc, 8)))
			self.galUSTOgalUK_res.setText(str(round(galUSTOgalUK_proc, 8)))
			self.galUSTObarr_res.setText(str(round(galUSTObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def galUKTO_fun(self):
		try:
			galUKTOm3_proc    = float(self.galUKi_LinEd.text()) * 4.546092e-03
			galUKTOdm3_proc   = float(self.galUKi_LinEd.text()) * 4.546092
			galUKTOcm3_proc   = float(self.galUKi_LinEd.text()) * 4.546092e+03
			galUKTOin3_proc   = float(self.galUKi_LinEd.text()) * 2.774196e+02
			galUKTOft3_proc   = float(self.galUKi_LinEd.text()) * 1.605437e-01
			galUKTOyd3_proc   = float(self.galUKi_LinEd.text()) * 5.946064e-03
			galUKTOgalUS_proc = float(self.galUKi_LinEd.text()) * 1.200950
			galUKTOgalUK_proc = float(self.galUKi_LinEd.text()) * 1
			galUKTObarr_proc  = float(self.galUKi_LinEd.text()) * 2.859406e-02

			self.galUKTOm3_res.setText(str(round(galUKTOm3_proc,       8)))
			self.galUKTOdm3_res.setText(str(round(galUKTOdm3_proc,     8)))
			self.galUKTOcm3_res.setText(str(round(galUKTOcm3_proc,     8)))
			self.galUKTOin3_res.setText(str(round(galUKTOin3_proc,     8)))
			self.galUKTOft3_res.setText(str(round(galUKTOft3_proc,     8)))
			self.galUKTOyd3_res.setText(str(round(galUKTOyd3_proc,     8)))
			self.galUKTOgalUS_res.setText(str(round(galUKTOgalUS_proc, 8)))
			self.galUKTOgalUK_res.setText(str(round(galUKTOgalUK_proc, 8)))
			self.galUKTObarr_res.setText(str(round(galUKTObarr_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def barrTO_fun(self):
		try:
			barrTOm3_proc    = float(self.barri_LinEd.text()) * 1.589873e-01
			barrTOdm3_proc   = float(self.barri_LinEd.text()) * 1.589873e+02
			barrTOcm3_proc   = float(self.barri_LinEd.text()) * 1.589873e+05
			barrTOin3_proc   = float(self.barri_LinEd.text()) * 9.702001e+03
			barrTOft3_proc   = float(self.barri_LinEd.text()) * 5.614584
			barrTOyd3_proc   = float(self.barri_LinEd.text()) * 2.079475e-01
			barrTOgalUS_proc = float(self.barri_LinEd.text()) * 4.200000e+01
			barrTOgalUK_proc = float(self.barri_LinEd.text()) * 3.497230e+01
			barrTObarr_proc  = float(self.barri_LinEd.text()) * 1

			self.barrTOm3_res.setText(str(round(barrTOm3_proc,       8)))
			self.barrTOdm3_res.setText(str(round(barrTOdm3_proc,     8)))
			self.barrTOcm3_res.setText(str(round(barrTOcm3_proc,     8)))
			self.barrTOin3_res.setText(str(round(barrTOin3_proc,     8)))
			self.barrTOft3_res.setText(str(round(barrTOft3_proc,     8)))
			self.barrTOyd3_res.setText(str(round(barrTOyd3_proc,     8)))
			self.barrTOgalUS_res.setText(str(round(barrTOgalUS_proc, 8)))
			self.barrTOgalUK_res.setText(str(round(barrTOgalUK_proc, 8)))
			self.barrTObarr_res.setText(str(round(barrTObarr_proc,   8)))
		
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
		