# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Volflow_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Volumetric Flow Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel         = QtWidgets.QLabel()
		self.dm3si_LinEd   = QtWidgets.QLineEdit()
		self.dm3hi_LinEd   = QtWidgets.QLineEdit()
		self.m3si_LinEd    = QtWidgets.QLineEdit()
		self.m3hi_LinEd    = QtWidgets.QLineEdit()
		self.ft3si_LinEd   = QtWidgets.QLineEdit()
		self.ft3hi_LinEd   = QtWidgets.QLineEdit()
		self.gpmUSi_LinEd  = QtWidgets.QLineEdit()
		self.gphUSi_LinEd  = QtWidgets.QLineEdit()
		self.bblhUSi_LinEd = QtWidgets.QLineEdit()

		LinEd_list = [self.dm3si_LinEd, self.dm3hi_LinEd, self.m3si_LinEd, self.m3hi_LinEd, self.ft3si_LinEd, self.ft3hi_LinEd, self.gpmUSi_LinEd, self.gphUSi_LinEd, 
					  self.bblhUSi_LinEd]

		Label_list = [blanklabel, "dm<sup>3</sup>/s", "dm<sup>3</sup>/h", "m<sup>3</sup>/s", "m<sup>3</sup>/h", "ft<sup>3</sup>/s", "ft<sup>3</sup>/h", "gpm<sub>US</sub>",
					  "gph<sub>US</sub>", "bbl<sub>US</sub>/h"]
		
		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		i = 1
		for item in LinEd_list:
			input_grid.addWidget(item, i, 0)
			i = i + 1

		input_group.setLayout(input_grid)
		
		self.dm3si_LinEd.returnPressed.connect(self.dm3sTO_fun)
		self.dm3hi_LinEd.returnPressed.connect(self.dm3hTO_fun)
		self.m3si_LinEd.returnPressed.connect(self.m3sTO_fun)
		self.m3hi_LinEd.returnPressed.connect(self.m3hTO_fun)
		self.ft3si_LinEd.returnPressed.connect(self.ft3sTO_fun)
		self.ft3hi_LinEd.returnPressed.connect(self.ft3hTO_fun)
		self.gpmUSi_LinEd.returnPressed.connect(self.gpmUSTO_fun)
		self.gphUSi_LinEd.returnPressed.connect(self.gphUSTO_fun)
		self.bblhUSi_LinEd.returnPressed.connect(self.bblhUSTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["dm<sup>3</sup>/s", "dm<sup>3</sup>/h", "m<sup>3</sup>/s", "m<sup>3</sup>/h", "ft<sup>3</sup>/s", "ft<sup>3</sup>/h", "gpm<sub>US</sub>",
					  "gph<sub>US</sub>", "bbl<sub>US</sub>/h"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.dm3sTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.dm3sTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.dm3sTOm3s_res    = QtWidgets.QLabel("0", self)
		self.dm3sTOm3h_res    = QtWidgets.QLabel("0", self)
		self.dm3sTOft3s_res   = QtWidgets.QLabel("0", self)
		self.dm3sTOft3h_res   = QtWidgets.QLabel("0", self)
		self.dm3sTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.dm3sTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.dm3sTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.dm3hTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.dm3hTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.dm3hTOm3s_res    = QtWidgets.QLabel("0", self)
		self.dm3hTOm3h_res    = QtWidgets.QLabel("0", self)
		self.dm3hTOft3s_res   = QtWidgets.QLabel("0", self)
		self.dm3hTOft3h_res   = QtWidgets.QLabel("0", self)
		self.dm3hTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.dm3hTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.dm3hTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.m3sTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.m3sTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.m3sTOm3s_res    = QtWidgets.QLabel("0", self)
		self.m3sTOm3h_res    = QtWidgets.QLabel("0", self)
		self.m3sTOft3s_res   = QtWidgets.QLabel("0", self)
		self.m3sTOft3h_res   = QtWidgets.QLabel("0", self)
		self.m3sTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.m3sTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.m3sTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.m3hTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.m3hTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.m3hTOm3s_res    = QtWidgets.QLabel("0", self)
		self.m3hTOm3h_res    = QtWidgets.QLabel("0", self)
		self.m3hTOft3s_res   = QtWidgets.QLabel("0", self)
		self.m3hTOft3h_res   = QtWidgets.QLabel("0", self)
		self.m3hTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.m3hTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.m3hTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.ft3sTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.ft3sTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.ft3sTOm3s_res    = QtWidgets.QLabel("0", self)
		self.ft3sTOm3h_res    = QtWidgets.QLabel("0", self)
		self.ft3sTOft3s_res   = QtWidgets.QLabel("0", self)
		self.ft3sTOft3h_res   = QtWidgets.QLabel("0", self)
		self.ft3sTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.ft3sTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.ft3sTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.ft3hTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.ft3hTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.ft3hTOm3s_res    = QtWidgets.QLabel("0", self)
		self.ft3hTOm3h_res    = QtWidgets.QLabel("0", self)
		self.ft3hTOft3s_res   = QtWidgets.QLabel("0", self)
		self.ft3hTOft3h_res   = QtWidgets.QLabel("0", self)
		self.ft3hTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.ft3hTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.ft3hTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.gpmUSTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.gpmUSTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.gpmUSTOm3s_res    = QtWidgets.QLabel("0", self)
		self.gpmUSTOm3h_res    = QtWidgets.QLabel("0", self)
		self.gpmUSTOft3s_res   = QtWidgets.QLabel("0", self)
		self.gpmUSTOft3h_res   = QtWidgets.QLabel("0", self)
		self.gpmUSTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.gpmUSTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.gpmUSTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.gphUSTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.gphUSTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.gphUSTOm3s_res    = QtWidgets.QLabel("0", self)
		self.gphUSTOm3h_res    = QtWidgets.QLabel("0", self)
		self.gphUSTOft3s_res   = QtWidgets.QLabel("0", self)
		self.gphUSTOft3h_res   = QtWidgets.QLabel("0", self)
		self.gphUSTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.gphUSTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.gphUSTObblhUS_res = QtWidgets.QLabel("0", self)
		
		self.bblhUSTOdm3s_res   = QtWidgets.QLabel("0", self)
		self.bblhUSTOdm3h_res   = QtWidgets.QLabel("0", self)
		self.bblhUSTOm3s_res    = QtWidgets.QLabel("0", self)
		self.bblhUSTOm3h_res    = QtWidgets.QLabel("0", self)
		self.bblhUSTOft3s_res   = QtWidgets.QLabel("0", self)
		self.bblhUSTOft3h_res   = QtWidgets.QLabel("0", self)
		self.bblhUSTOgpmUS_res  = QtWidgets.QLabel("0", self)
		self.bblhUSTOgphUS_res  = QtWidgets.QLabel("0", self)
		self.bblhUSTObblhUS_res = QtWidgets.QLabel("0", self)
		
		dm3sTO_Label = [self.dm3sTOdm3s_res, self.dm3sTOdm3h_res, self.dm3sTOm3s_res, self.dm3sTOm3h_res, self.dm3sTOft3s_res,
						self.dm3sTOft3h_res, self.dm3sTOgpmUS_res, self.dm3sTOgphUS_res, self.dm3sTObblhUS_res]
		
		dm3hTO_Label = [self.dm3hTOdm3s_res, self.dm3hTOdm3h_res, self.dm3hTOm3s_res, self.dm3hTOm3h_res, self.dm3hTOft3s_res,
						self.dm3hTOft3h_res, self.dm3hTOgpmUS_res, self.dm3hTOgphUS_res, self.dm3hTObblhUS_res]

		m3sTO_Label = [self.m3sTOdm3s_res, self.m3sTOdm3h_res, self.m3sTOm3s_res, self.m3sTOm3h_res, self.m3sTOft3s_res,
					   self.m3sTOft3h_res, self.m3sTOgpmUS_res, self.m3sTOgphUS_res, self.m3sTObblhUS_res]

		m3hTO_Label = [self.m3hTOdm3s_res, self.m3hTOdm3h_res, self.m3hTOm3s_res, self.m3hTOm3h_res, self.m3hTOft3s_res,
					   self.m3hTOft3h_res, self.m3hTOgpmUS_res, self.m3hTOgphUS_res, self.m3hTObblhUS_res]
		
		ft3sTO_Label = [self.ft3sTOdm3s_res, self.ft3sTOdm3h_res, self.ft3sTOm3s_res, self.ft3sTOm3h_res, self.ft3sTOft3s_res,
						self.ft3sTOft3h_res, self.ft3sTOgpmUS_res, self.ft3sTOgphUS_res, self.ft3sTObblhUS_res]
		
		ft3hTO_Label = [self.ft3hTOdm3s_res, self.ft3hTOdm3h_res, self.ft3hTOm3s_res, self.ft3hTOm3h_res, self.ft3hTOft3s_res,
						self.ft3hTOft3h_res, self.ft3hTOgpmUS_res, self.ft3hTOgphUS_res, self.ft3hTObblhUS_res]
		
		gpmUSTO_Label = [self.gpmUSTOdm3s_res, self.gpmUSTOdm3h_res, self.gpmUSTOm3s_res, self.gpmUSTOm3h_res, 
						 self.gpmUSTOft3s_res, self.gpmUSTOft3h_res, self.gpmUSTOgpmUS_res, self.gpmUSTOgphUS_res,
						 self.gpmUSTObblhUS_res]
		
		gphUSTO_Label = [self.gphUSTOdm3s_res, self.gphUSTOdm3h_res, self.gphUSTOm3s_res, self.gphUSTOm3h_res, 
						 self.gphUSTOft3s_res, self.gphUSTOft3h_res, self.gphUSTOgpmUS_res, self.gphUSTOgphUS_res,
						 self.gphUSTObblhUS_res]
		
		bblhUSTO_Label = [self.bblhUSTOdm3s_res, self.bblhUSTOdm3h_res, self.bblhUSTOm3s_res, self.bblhUSTOm3h_res,
						  self.bblhUSTOft3s_res, self.bblhUSTOft3h_res, self.bblhUSTOgpmUS_res, self.bblhUSTOgphUS_res,
						  self.bblhUSTObblhUS_res]
		
		i = 0
		for item in dm3sTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in dm3hTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in m3sTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in m3hTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in ft3sTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in ft3hTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in gpmUSTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in gphUSTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in bblhUSTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		
		output_group.setLayout(output_grid)

		return output_group

	def dm3sTO_fun(self):
		try:
			dm3sTOdm3s_proc   = float(self.dm3si_LinEd.text()) * 1
			dm3sTOdm3h_proc   = float(self.dm3si_LinEd.text()) * 3600
			dm3sTOm3s_proc    = float(self.dm3si_LinEd.text()) * 1e-03
			dm3sTOm3h_proc    = float(self.dm3si_LinEd.text()) * 1e-03 * 3600
			dm3sTOft3s_proc   = float(self.dm3si_LinEd.text()) * 1e-03 * 35.3146667
			dm3sTOft3h_proc   = float(self.dm3si_LinEd.text()) * 1e-03 * 35.3146667 * 3600
			dm3sTOgpmUS_proc  = float(self.dm3si_LinEd.text()) * 1e-03 * 15850.323141
			dm3sTOgphUS_proc  = float(self.dm3si_LinEd.text()) * 1e-03 * 15850.323141 * 60
			dm3sTObblhUS_proc = float(self.dm3si_LinEd.text()) * 1e-03 * 22643.32

			self.dm3sTOdm3s_res.setText(str(round(dm3sTOdm3s_proc,     8)))
			self.dm3sTOdm3h_res.setText(str(round(dm3sTOdm3h_proc,     8)))
			self.dm3sTOm3s_res.setText(str(round(dm3sTOm3s_proc,       8)))
			self.dm3sTOm3h_res.setText(str(round(dm3sTOm3h_proc,       8)))
			self.dm3sTOft3s_res.setText(str(round(dm3sTOft3s_proc,     8)))
			self.dm3sTOft3h_res.setText(str(round(dm3sTOft3h_proc,     8)))
			self.dm3sTOgpmUS_res.setText(str(round(dm3sTOgpmUS_proc,   8)))
			self.dm3sTOgphUS_res.setText(str(round(dm3sTOgphUS_proc,   8)))
			self.dm3sTObblhUS_res.setText(str(round(dm3sTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()

	def dm3hTO_fun(self):
		try:
			dm3hTOdm3s_proc   = float(self.dm3hi_LinEd.text()) * 1 / 3600
			dm3hTOdm3h_proc   = float(self.dm3hi_LinEd.text()) * 1
			dm3hTOm3s_proc    = float(self.dm3hi_LinEd.text()) * 1e-03 / 3600 
			dm3hTOm3h_proc    = float(self.dm3hi_LinEd.text()) * 1e-03
			dm3hTOft3s_proc   = float(self.dm3hi_LinEd.text()) * 1e-03 * 35.314667 / 3600
			dm3hTOft3h_proc   = float(self.dm3hi_LinEd.text()) * 1e-03 * 35.314667
			dm3hTOgpmUS_proc  = float(self.dm3hi_LinEd.text()) * 1e-03 * 15850.323141 / 3600
			dm3hTOgphUS_proc  = float(self.dm3hi_LinEd.text()) * 1e-03 * 15850.323141
			dm3hTObblhUS_proc = float(self.dm3hi_LinEd.text()) * 1e-03 * 22643.32 * 3600

			self.dm3hTOdm3s_res.setText(str(round(dm3hTOdm3s_proc,     8)))
			self.dm3hTOdm3h_res.setText(str(round(dm3hTOdm3h_proc,     8)))
			self.dm3hTOm3s_res.setText(str(round(dm3hTOm3s_proc,       8)))
			self.dm3hTOm3h_res.setText(str(round(dm3hTOm3h_proc,       8)))
			self.dm3hTOft3s_res.setText(str(round(dm3hTOft3s_proc,     8)))
			self.dm3hTOft3h_res.setText(str(round(dm3hTOft3h_proc,     8)))
			self.dm3hTOgpmUS_res.setText(str(round(dm3hTOgpmUS_proc,   8)))
			self.dm3hTOgphUS_res.setText(str(round(dm3hTOgphUS_proc,   8)))
			self.dm3hTObblhUS_res.setText(str(round(dm3hTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def m3sTO_fun(self):
		try:
			m3sTOdm3s_proc   = float(self.m3si_LinEd.text()) * 1e+03
			m3sTOdm3h_proc   = float(self.m3si_LinEd.text()) * 1e+03 * 3600
			m3sTOm3s_proc    = float(self.m3si_LinEd.text()) * 1
			m3sTOm3h_proc    = float(self.m3si_LinEd.text()) * 3600
			m3sTOft3s_proc   = float(self.m3si_LinEd.text()) * 35.3146667
			m3sTOft3h_proc   = float(self.m3si_LinEd.text()) * 35.3146667 * 3600
			m3sTOgpmUS_proc  = float(self.m3si_LinEd.text()) * 15850.323141
			m3sTOgphUS_proc  = float(self.m3si_LinEd.text()) * 15850.323141 * 3600
			m3sTObblhUS_proc = float(self.m3si_LinEd.text()) * 22643.32

			self.m3sTOdm3s_res.setText(str(round(m3sTOdm3s_proc,     8)))
			self.m3sTOdm3h_res.setText(str(round(m3sTOdm3h_proc,     8)))
			self.m3sTOm3s_res.setText(str(round(m3sTOm3s_proc,       8)))
			self.m3sTOm3h_res.setText(str(round(m3sTOm3h_proc,       8)))
			self.m3sTOft3s_res.setText(str(round(m3sTOft3s_proc,     8)))
			self.m3sTOft3h_res.setText(str(round(m3sTOft3h_proc,     8)))
			self.m3sTOgpmUS_res.setText(str(round(m3sTOgpmUS_proc,   8)))
			self.m3sTOgphUS_res.setText(str(round(m3sTOgphUS_proc,   8)))
			self.m3sTObblhUS_res.setText(str(round(m3sTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def m3hTO_fun(self):
		try:
			m3hTOdm3s_proc   = float(self.m3hi_LinEd.text()) * 1e+03 / 3600
			m3hTOdm3h_proc   = float(self.m3hi_LinEd.text()) * 1e+03
			m3hTOm3s_proc    = float(self.m3hi_LinEd.text()) * 1 / 3600
			m3hTOm3h_proc    = float(self.m3hi_LinEd.text()) * 1
			m3hTOft3s_proc   = float(self.m3hi_LinEd.text()) * 35.3146667 * 3600
			m3hTOft3h_proc   = float(self.m3hi_LinEd.text()) * 35.3146667
			m3hTOgpmUS_proc  = float(self.m3hi_LinEd.text()) * 15850.323141 * 3600
			m3hTOgphUS_proc  = float(self.m3hi_LinEd.text()) * 15850.323141 * 60
			m3hTObblhUS_proc = float(self.m3hi_LinEd.text()) * 22643.32 * 3600

			self.m3hTOdm3s_res.setText(str(round(m3hTOdm3s_proc,     8)))
			self.m3hTOdm3h_res.setText(str(round(m3hTOdm3h_proc,     8)))
			self.m3hTOm3s_res.setText(str(round(m3hTOm3s_proc,       8)))
			self.m3hTOm3h_res.setText(str(round(m3hTOm3h_proc,       8)))
			self.m3hTOft3s_res.setText(str(round(m3hTOft3s_proc,     8)))
			self.m3hTOft3h_res.setText(str(round(m3hTOft3h_proc,     8)))
			self.m3hTOgpmUS_res.setText(str(round(m3hTOgpmUS_proc,   8)))
			self.m3hTOgphUS_res.setText(str(round(m3hTOgphUS_proc,   8)))
			self.m3hTObblhUS_res.setText(str(round(m3hTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def ft3sTO_fun(self):
		try:
			ft3sTOdm3s_proc   = float(self.ft3si_LinEd.text()) * 1e+03 / 35.3146667
			ft3sTOdm3h_proc   = float(self.ft3si_LinEd.text()) * 1e+03 / 35.3146667 * 3600
			ft3sTOm3s_proc    = float(self.ft3si_LinEd.text()) * 1 / 35.3146667
			ft3sTOm3h_proc    = float(self.ft3si_LinEd.text()) * 1 / 35.3146667 * 3600
			ft3sTOft3s_proc   = float(self.ft3si_LinEd.text()) * 1
			ft3sTOft3h_proc   = float(self.ft3si_LinEd.text()) * 3600
			ft3sTOgpmUS_proc  = float(self.ft3si_LinEd.text()) * 0.12467532 * 3600
			ft3sTOgphUS_proc  = float(self.ft3si_LinEd.text()) * 7.48051905 * 3600
			ft3sTObblhUS_proc = float(self.ft3si_LinEd.text()) * 22463.32 / 35.3146667

			self.ft3sTOdm3s_res.setText(str(round(ft3sTOdm3s_proc,     8)))
			self.ft3sTOdm3h_res.setText(str(round(ft3sTOdm3h_proc,     8)))
			self.ft3sTOm3s_res.setText(str(round(ft3sTOm3s_proc,       8)))
			self.ft3sTOm3h_res.setText(str(round(ft3sTOm3h_proc,       8)))
			self.ft3sTOft3s_res.setText(str(round(ft3sTOft3s_proc,     8)))
			self.ft3sTOft3h_res.setText(str(round(ft3sTOft3h_proc,     8)))
			self.ft3sTOgpmUS_res.setText(str(round(ft3sTOgpmUS_proc,   8)))
			self.ft3sTOgphUS_res.setText(str(round(ft3sTOgphUS_proc,   8)))
			self.ft3sTObblhUS_res.setText(str(round(ft3sTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def ft3hTO_fun(self):
		try:
			ft3hTOdm3s_proc   = float(self.ft3hi_LinEd.text()) * 1 / 35.3146667 * 1e+03
			ft3hTOdm3h_proc   = float(self.ft3hi_LinEd.text()) * 1 / 35.3146667 * 1e+03 * 3600
			ft3hTOm3s_proc    = float(self.ft3hi_LinEd.text()) * 1 / 35.3146667
			ft3hTOm3h_proc    = float(self.ft3hi_LinEd.text()) * 1 / 35.3146667 * 3600
			ft3hTOft3s_proc   = float(self.ft3hi_LinEd.text()) * 1 / 3600
			ft3hTOft3h_proc   = float(self.ft3hi_LinEd.text()) * 1
			ft3hTOgpmUS_proc  = float(self.ft3hi_LinEd.text()) * 0.12467532
			ft3hTOgphUS_proc  = float(self.ft3hi_LinEd.text()) * 7.48051905
			ft3hTObblhUS_proc = float(self.ft3hi_LinEd.text()) * 22463.32 / 35.146667 * 3600

			self.ft3hTOdm3s_res.setText(str(round(ft3hTOdm3s_proc,     8)))
			self.ft3hTOdm3h_res.setText(str(round(ft3hTOdm3h_proc,     8)))
			self.ft3hTOm3s_res.setText(str(round(ft3hTOm3s_proc,       8)))
			self.ft3hTOm3h_res.setText(str(round(ft3hTOm3h_proc,       8)))
			self.ft3hTOft3s_res.setText(str(round(ft3hTOft3s_proc,     8)))
			self.ft3hTOft3h_res.setText(str(round(ft3hTOft3h_proc,     8)))
			self.ft3hTOgpmUS_res.setText(str(round(ft3hTOgpmUS_proc,   8)))
			self.ft3hTOgphUS_res.setText(str(round(ft3hTOgphUS_proc,   8)))
			self.ft3hTObblhUS_res.setText(str(round(ft3hTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def gpmUSTO_fun(self):
		try:
			gpmUSTOdm3s_proc   = float(self.gpmUSi_LinEd.text()) * 1e+03 / 15850.323141
			gpmUSTOdm3h_proc   = float(self.gpmUSi_LinEd.text()) * 1e+03 / 15850.323141 * 3600
			gpmUSTOm3s_proc    = float(self.gpmUSi_LinEd.text()) * 1 / 15850.323141
			gpmUSTOm3h_proc    = float(self.gpmUSi_LinEd.text()) * 1 / 15850.323141 * 3600
			gpmUSTOft3s_proc   = float(self.gpmUSi_LinEd.text()) * 8.020836 / 3600
			gpmUSTOft3h_proc   = float(self.gpmUSi_LinEd.text()) * 8.020836
			gpmUSTOgpmUS_proc  = float(self.gpmUSi_LinEd.text()) * 1
			gpmUSTOgphUS_proc  = float(self.gpmUSi_LinEd.text()) * 60
			gpmUSTObblhUS_proc = float(self.gpmUSi_LinEd.text()) * 1.428571465

			self.gpmUSTOdm3s_res.setText(str(round(gpmUSTOdm3s_proc,     8)))
			self.gpmUSTOdm3h_res.setText(str(round(gpmUSTOdm3h_proc,     8)))
			self.gpmUSTOm3s_res.setText(str(round(gpmUSTOm3s_proc,       8)))
			self.gpmUSTOm3h_res.setText(str(round(gpmUSTOm3h_proc,       8)))
			self.gpmUSTOft3s_res.setText(str(round(gpmUSTOft3s_proc,     8)))
			self.gpmUSTOft3h_res.setText(str(round(gpmUSTOft3h_proc,     8)))
			self.gpmUSTOgpmUS_res.setText(str(round(gpmUSTOgpmUS_proc,   8)))
			self.gpmUSTOgphUS_res.setText(str(round(gpmUSTOgphUS_proc,   8)))
			self.gpmUSTObblhUS_res.setText(str(round(gpmUSTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def gphUSTO_fun(self):
		try:
			gphUSTOdm3s_proc   = float(self.gphUSi_LinEd.text()) * 1e+03 / 15850.323141 * 60
			gphUSTOdm3h_proc   = float(self.gphUSi_LinEd.text()) * 1e+03 / 15850.323141 * 3600 * 60
			gphUSTOm3s_proc    = float(self.gphUSi_LinEd.text()) * 1 / 15850.323141 * 60
			gphUSTOm3h_proc    = float(self.gphUSi_LinEd.text()) * 1 / 15850.323141 * 3600 * 60
			gphUSTOft3s_proc   = float(self.gphUSi_LinEd.text()) * 8.020836 / 3600 * 60
			gphUSTOft3h_proc   = float(self.gphUSi_LinEd.text()) * 8.020836 * 60
			gphUSTOgpmUS_proc  = float(self.gphUSi_LinEd.text()) * 60
			gphUSTOgphUS_proc  = float(self.gphUSi_LinEd.text()) * 1
			gphUSTObblhUS_proc = float(self.gphUSi_LinEd.text()) * 1.428571465 * 60

			self.gphUSTOdm3s_res.setText(str(round(gphUSTOdm3s_proc,     8)))
			self.gphUSTOdm3h_res.setText(str(round(gphUSTOdm3h_proc,     8)))
			self.gphUSTOm3s_res.setText(str(round(gphUSTOm3s_proc,       8)))
			self.gphUSTOm3h_res.setText(str(round(gphUSTOm3h_proc,       8)))
			self.gphUSTOft3s_res.setText(str(round(gphUSTOft3s_proc,     8)))
			self.gphUSTOft3h_res.setText(str(round(gphUSTOft3h_proc,     8)))
			self.gphUSTOgpmUS_res.setText(str(round(gphUSTOgpmUS_proc,   8)))
			self.gphUSTOgphUS_res.setText(str(round(gphUSTOgphUS_proc,   8)))
			self.gphUSTObblhUS_res.setText(str(round(gphUSTObblhUS_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			
	def bblhUSTO_fun(self):
		try:
			bblhUSTOdm3s_proc   = float(self.bblhUSi_LinEd.text()) * 1e+03 / 22643.32
			bblhUSTOdm3h_proc   = float(self.bblhUSi_LinEd.text()) * 1e+03 / 22643.32 * 60
			bblhUSTOm3s_proc    = float(self.bblhUSi_LinEd.text()) * 1 / 22643.32
			bblhUSTOm3h_proc    = float(self.bblhUSi_LinEd.text()) * 1 / 22643.32 * 60
			bblhUSTOft3s_proc   = float(self.bblhUSi_LinEd.text()) * 500 / 89 / 3600
			bblhUSTOft3h_proc   = float(self.bblhUSi_LinEd.text()) * 500 / 89
			bblhUSTOgpmUS_proc  = float(self.bblhUSi_LinEd.text()) * 42 / 60
			bblhUSTOgphUS_proc  = float(self.bblhUSi_LinEd.text()) * 42
			bblhUSTObblhUS_proc = float(self.bblhUSi_LinEd.text()) * 1

			self.bblhUSTOdm3s_res.setText(str(round(bblhUSTOdm3s_proc,     8)))
			self.bblhUSTOdm3h_res.setText(str(round(bblhUSTOdm3h_proc,     8)))
			self.bblhUSTOm3s_res.setText(str(round(bblhUSTOm3s_proc,       8)))
			self.bblhUSTOm3h_res.setText(str(round(bblhUSTOm3h_proc,       8)))
			self.bblhUSTOft3s_res.setText(str(round(bblhUSTOft3s_proc,     8)))
			self.bblhUSTOft3h_res.setText(str(round(bblhUSTOft3h_proc,     8)))
			self.bblhUSTOgpmUS_res.setText(str(round(bblhUSTOgpmUS_proc,   8)))
			self.bblhUSTOgphUS_res.setText(str(round(bblhUSTOgphUS_proc,   8)))
			self.bblhUSTObblhUS_res.setText(str(round(bblhUSTObblhUS_proc, 8)))
		
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
