# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Area_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Area Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()
		
	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel        = QtWidgets.QLabel()
		self.m2i_LinEd    = QtWidgets.QLineEdit()
		self.cm2i_LinEd   = QtWidgets.QLineEdit()
		self.mm2i_LinEd   = QtWidgets.QLineEdit()
		self.ai_LinEd	  = QtWidgets.QLineEdit()
		self.hai_LinEd	  = QtWidgets.QLineEdit()
		self.in2i_LinEd	  = QtWidgets.QLineEdit()
		self.ft2i_LinEd	  = QtWidgets.QLineEdit()
		self.yd2i_LinEd   = QtWidgets.QLineEdit()
		self.acri_LinEd   = QtWidgets.QLineEdit()
		self.mi2STi_LinEd = QtWidgets.QLineEdit()

		LinEd_list = [self.m2i_LinEd, self.cm2i_LinEd, self.mm2i_LinEd, self.ai_LinEd, self.hai_LinEd, self.in2i_LinEd, self.ft2i_LinEd, self.yd2i_LinEd,
					  self.acri_LinEd, self.mi2STi_LinEd]
		
		Label_list = [blanklabel, "m\u00B2", "cm\u00B2", "mm\u00B2", "a", "ha", "in\u00B2", "ft\u00B2", "yard\u00B2", "acr", "mile\u00B2<sub>statute</sub>"]

		i = 1
		for item in LinEd_list:
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
		self.mm2i_LinEd.returnPressed.connect(self.mm2TO_fun)
		self.ai_LinEd.returnPressed.connect(self.aTO_fun)
		self.hai_LinEd.returnPressed.connect(self.haTO_fun)
		self.in2i_LinEd.returnPressed.connect(self.in2TO_fun)
		self.ft2i_LinEd.returnPressed.connect(self.ft2TO_fun)
		self.yd2i_LinEd.returnPressed.connect(self.yd2TO_fun)
		self.acri_LinEd.returnPressed.connect(self.acrTO_fun)
		self.mi2STi_LinEd.returnPressed.connect(self.mi2STTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["m\u00B2", "cm\u00B2", "mm\u00B2", "a", "ha", "in\u00B2", "ft\u00B2", "yard\u00B2", "acr", "mile\u00B2<sub>statute</sub>"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.m2TOm2_res    = QtWidgets.QLabel("0", self)
		self.m2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.m2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.m2TOa_res     = QtWidgets.QLabel("0", self)
		self.m2TOha_res    = QtWidgets.QLabel("0", self)
		self.m2TOin2_res   = QtWidgets.QLabel("0", self)
		self.m2TOft2_res   = QtWidgets.QLabel("0", self)
		self.m2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.m2TOacr_res   = QtWidgets.QLabel("0", self)
		self.m2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.cm2TOm2_res    = QtWidgets.QLabel("0", self)
		self.cm2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.cm2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.cm2TOa_res     = QtWidgets.QLabel("0", self)
		self.cm2TOha_res    = QtWidgets.QLabel("0", self)
		self.cm2TOin2_res   = QtWidgets.QLabel("0", self)
		self.cm2TOft2_res   = QtWidgets.QLabel("0", self)
		self.cm2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.cm2TOacr_res   = QtWidgets.QLabel("0", self)
		self.cm2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.mm2TOm2_res    = QtWidgets.QLabel("0", self)
		self.mm2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.mm2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.mm2TOa_res     = QtWidgets.QLabel("0", self)
		self.mm2TOha_res    = QtWidgets.QLabel("0", self)
		self.mm2TOin2_res   = QtWidgets.QLabel("0", self)
		self.mm2TOft2_res   = QtWidgets.QLabel("0", self)
		self.mm2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.mm2TOacr_res   = QtWidgets.QLabel("0", self)
		self.mm2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.aTOm2_res    = QtWidgets.QLabel("0", self)
		self.aTOcm2_res   = QtWidgets.QLabel("0", self)
		self.aTOmm2_res   = QtWidgets.QLabel("0", self)
		self.aTOa_res     = QtWidgets.QLabel("0", self)
		self.aTOha_res    = QtWidgets.QLabel("0", self)
		self.aTOin2_res   = QtWidgets.QLabel("0", self)
		self.aTOft2_res   = QtWidgets.QLabel("0", self)
		self.aTOyd2_res   = QtWidgets.QLabel("0", self)
		self.aTOacr_res   = QtWidgets.QLabel("0", self)
		self.aTOmi2ST_res = QtWidgets.QLabel("0", self)

		self.haTOm2_res    = QtWidgets.QLabel("0", self)
		self.haTOcm2_res   = QtWidgets.QLabel("0", self)
		self.haTOmm2_res   = QtWidgets.QLabel("0", self)
		self.haTOa_res     = QtWidgets.QLabel("0", self)
		self.haTOha_res    = QtWidgets.QLabel("0", self)
		self.haTOin2_res   = QtWidgets.QLabel("0", self)
		self.haTOft2_res   = QtWidgets.QLabel("0", self)
		self.haTOyd2_res   = QtWidgets.QLabel("0", self)
		self.haTOacr_res   = QtWidgets.QLabel("0", self)
		self.haTOmi2ST_res = QtWidgets.QLabel("0", self)

		self.in2TOm2_res    = QtWidgets.QLabel("0", self)
		self.in2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.in2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.in2TOa_res     = QtWidgets.QLabel("0", self)
		self.in2TOha_res    = QtWidgets.QLabel("0", self)
		self.in2TOin2_res   = QtWidgets.QLabel("0", self)
		self.in2TOft2_res   = QtWidgets.QLabel("0", self)
		self.in2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.in2TOacr_res   = QtWidgets.QLabel("0", self)
		self.in2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.ft2TOm2_res    = QtWidgets.QLabel("0", self)
		self.ft2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.ft2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.ft2TOa_res     = QtWidgets.QLabel("0", self)
		self.ft2TOha_res    = QtWidgets.QLabel("0", self)
		self.ft2TOin2_res   = QtWidgets.QLabel("0", self)
		self.ft2TOft2_res   = QtWidgets.QLabel("0", self)
		self.ft2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.ft2TOacr_res   = QtWidgets.QLabel("0", self)
		self.ft2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.yd2TOm2_res    = QtWidgets.QLabel("0", self)
		self.yd2TOcm2_res   = QtWidgets.QLabel("0", self)
		self.yd2TOmm2_res   = QtWidgets.QLabel("0", self)
		self.yd2TOa_res     = QtWidgets.QLabel("0", self)
		self.yd2TOha_res    = QtWidgets.QLabel("0", self)
		self.yd2TOin2_res   = QtWidgets.QLabel("0", self)
		self.yd2TOft2_res   = QtWidgets.QLabel("0", self)
		self.yd2TOyd2_res   = QtWidgets.QLabel("0", self)
		self.yd2TOacr_res   = QtWidgets.QLabel("0", self)
		self.yd2TOmi2ST_res = QtWidgets.QLabel("0", self)

		self.acrTOm2_res    = QtWidgets.QLabel("0", self)
		self.acrTOcm2_res   = QtWidgets.QLabel("0", self)
		self.acrTOmm2_res   = QtWidgets.QLabel("0", self)
		self.acrTOa_res     = QtWidgets.QLabel("0", self)
		self.acrTOha_res    = QtWidgets.QLabel("0", self)
		self.acrTOin2_res   = QtWidgets.QLabel("0", self)
		self.acrTOft2_res   = QtWidgets.QLabel("0", self)
		self.acrTOyd2_res   = QtWidgets.QLabel("0", self)
		self.acrTOacr_res   = QtWidgets.QLabel("0", self)
		self.acrTOmi2ST_res = QtWidgets.QLabel("0", self)

		self.mi2STTOm2_res    = QtWidgets.QLabel("0", self)
		self.mi2STTOcm2_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOmm2_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOa_res     = QtWidgets.QLabel("0", self)
		self.mi2STTOha_res    = QtWidgets.QLabel("0", self)
		self.mi2STTOin2_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOft2_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOyd2_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOacr_res   = QtWidgets.QLabel("0", self)
		self.mi2STTOmi2ST_res = QtWidgets.QLabel("0", self)

		m2TO_Label = [self.m2TOm2_res, self.m2TOcm2_res, self.m2TOmm2_res, self.m2TOa_res, self.m2TOha_res, self.m2TOin2_res, self.m2TOft2_res, self.m2TOyd2_res,
					  self.m2TOacr_res, self.m2TOmi2ST_res]

		cm2TO_Label = [self.cm2TOm2_res, self.cm2TOcm2_res, self.cm2TOmm2_res, self.cm2TOa_res, self.cm2TOha_res, self.cm2TOin2_res, self.cm2TOft2_res, self.cm2TOyd2_res,
					   self.cm2TOacr_res, self.cm2TOmi2ST_res]

		mm2TO_Label = [self.mm2TOm2_res, self.mm2TOcm2_res, self.mm2TOmm2_res, self.mm2TOa_res, self.mm2TOha_res, self.mm2TOin2_res, self.mm2TOft2_res, self.mm2TOyd2_res,
					   self.mm2TOacr_res, self.mm2TOmi2ST_res]

		aTO_Label = [self.aTOm2_res, self.aTOcm2_res, self.aTOmm2_res, self.aTOa_res, self.aTOha_res, self.aTOin2_res, self.aTOft2_res, self.aTOyd2_res,
					 self.aTOacr_res, self.aTOmi2ST_res]

		haTO_Label = [self.haTOm2_res, self.haTOcm2_res, self.haTOmm2_res, self.haTOa_res, self.haTOha_res, self.haTOin2_res, self.haTOft2_res, self.haTOyd2_res,
					  self.haTOacr_res, self.haTOmi2ST_res]

		in2TO_Label = [self.in2TOm2_res, self.in2TOcm2_res, self.in2TOmm2_res, self.in2TOa_res, self.in2TOha_res, self.in2TOin2_res, self.in2TOft2_res, self.in2TOyd2_res,
					   self.in2TOacr_res, self.in2TOmi2ST_res]
		ft2TO_Label = [self.ft2TOm2_res, self.ft2TOcm2_res, self.ft2TOmm2_res, self.ft2TOa_res, self.ft2TOha_res, self.ft2TOin2_res, self.ft2TOft2_res, self.ft2TOyd2_res,
					   self.ft2TOacr_res, self.ft2TOmi2ST_res]

		yd2TO_Label = [self.yd2TOm2_res, self.yd2TOcm2_res, self.yd2TOmm2_res, self.yd2TOa_res, self.yd2TOha_res, self.yd2TOin2_res, self.yd2TOft2_res, self.yd2TOyd2_res,
					   self.yd2TOacr_res, self.yd2TOmi2ST_res]

		acrTO_Label = [self.acrTOm2_res, self.acrTOcm2_res, self.acrTOmm2_res, self.acrTOa_res, self.acrTOha_res, self.acrTOin2_res, self.acrTOft2_res, self.acrTOyd2_res,
					   self.acrTOacr_res, self.acrTOmi2ST_res]

		mi2STTO_Label = [self.mi2STTOm2_res, self.mi2STTOcm2_res, self.mi2STTOmm2_res, self.mi2STTOa_res, self.mi2STTOha_res, self.mi2STTOin2_res, self.mi2STTOft2_res, 
						 self.mi2STTOyd2_res, self.mi2STTOacr_res, self.mi2STTOmi2ST_res]

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

		i = 0
		for item in mm2TO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in aTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in haTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in in2TO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ft2TO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in yd2TO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in acrTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in mi2STTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1


		output_group.setLayout(output_grid)

		return output_group

	def m2TO_fun(self):
		try:
			m2TOm2_proc    = float(self.m2i_LinEd.text()) * 1
			m2TOcm2_proc   = float(self.m2i_LinEd.text()) * 1e+04
			m2TOmm2_proc   = float(self.m2i_LinEd.text()) * 1e+06
			m2TOa_proc     = float(self.m2i_LinEd.text()) * 1e-02
			m2TOha_proc    = float(self.m2i_LinEd.text()) * 1e-04
			m2TOin2_proc   = float(self.m2i_LinEd.text()) * 1.5500031e+03
			m2TOft2_proc   = float(self.m2i_LinEd.text()) * 1.0763910e+01
			m2TOyd2_proc   = float(self.m2i_LinEd.text()) * 1.19599
			m2TOacr_proc   = float(self.m2i_LinEd.text()) * 2.471054e-04
			m2TOmi2ST_proc = float(self.m2i_LinEd.text()) * 3.861022e-07

			self.m2TOm2_res.setText(str(round(m2TOm2_proc,       8)))
			self.m2TOcm2_res.setText(str(round(m2TOcm2_proc,     8)))
			self.m2TOmm2_res.setText(str(round(m2TOmm2_proc,     8)))
			self.m2TOa_res.setText(str(round(m2TOa_proc,         8)))
			self.m2TOha_res.setText(str(round(m2TOha_proc,       8)))
			self.m2TOin2_res.setText(str(round(m2TOin2_proc,     8)))
			self.m2TOft2_res.setText(str(round(m2TOft2_proc,     8)))
			self.m2TOyd2_res.setText(str(round(m2TOyd2_proc,     8)))
			self.m2TOacr_res.setText(str(round(m2TOacr_proc,     8)))
			self.m2TOmi2ST_res.setText(str(round(m2TOmi2ST_proc, 8)))
		
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
			cm2TOmm2_proc   = float(self.cm2i_LinEd.text()) * 1e+02
			cm2TOa_proc     = float(self.cm2i_LinEd.text()) * 1e-06
			# cm2TOha_proc    = float(self.cm2i_LinEd.text()) * 1e-08
			cm2TOin2_proc   = float(self.cm2i_LinEd.text()) * 1.5500031e-01
			cm2TOft2_proc   = float(self.cm2i_LinEd.text()) * 1.0763910e-03
			cm2TOyd2_proc   = float(self.cm2i_LinEd.text()) * 1.19599e-04
			# cm2TOacr_proc  = float(self.cm2i_LinEd.text()) * 2.471054e-08
			# cm2TOmi2ST_proc = float(self.cm2i_LinEd.text()) * 3.861022e-11

			self.cm2TOm2_res.setText(str(cm2TOm2_proc))
			self.cm2TOcm2_res.setText(str(cm2TOcm2_proc))
			self.cm2TOmm2_res.setText(str(cm2TOmm2_proc))
			self.cm2TOa_res.setText(str(round(cm2TOa_proc,     8)))
			self.cm2TOha_res.setText("-")
			self.cm2TOin2_res.setText(str(round(cm2TOin2_proc, 8)))
			self.cm2TOft2_res.setText(str(round(cm2TOft2_proc, 8)))
			self.cm2TOyd2_res.setText(str(round(cm2TOyd2_proc, 8)))
			self.cm2TOacr_res.setText("-")
			self.cm2TOmi2ST_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
			


	def mm2TO_fun(self):
		try:
			mm2TOm2_proc    = float(self.mm2i_LinEd.text()) * 1e-06
			mm2TOcm2_proc   = float(self.mm2i_LinEd.text()) * 1e-02
			mm2TOmm2_proc   = float(self.mm2i_LinEd.text()) * 1
			# mm2TOa_proc     = float(self.mm2i_LinEd.text()) * 1e-08
			# mm2TOha_proc    = float(self.mm2i_LinEd.text()) * 1e-10
			mm2TOin2_proc   = float(self.mm2i_LinEd.text()) * 1.5500031e-03
			mm2TOft2_proc   = float(self.mm2i_LinEd.text()) * 1.0763910e-05
			mm2TOyd2_proc   = float(self.mm2i_LinEd.text()) * 1.1959900e-06
			# mm2TOacr_proc  = float(self.mm2i_LinEd.text()) * 2.47054e-10
			# mm2TOmi2ST_proc = float(self.mm2i_LinEd.text()) * 3.861022e-13

			self.mm2TOm2_res.setText(str(round(mm2TOm2_proc,   8)))
			self.mm2TOcm2_res.setText(str(round(mm2TOcm2_proc, 8)))
			self.mm2TOmm2_res.setText(str(round(mm2TOmm2_proc, 8)))
			self.mm2TOa_res.setText("-")
			self.mm2TOha_res.setText("-")
			self.mm2TOin2_res.setText(str(round(mm2TOin2_proc, 8)))
			self.mm2TOft2_res.setText(str(round(mm2TOft2_proc, 8)))
			self.mm2TOyd2_res.setText(str(round(mm2TOyd2_proc, 8)))
			self.mm2TOacr_res.setText("-")
			self.mm2TOmi2ST_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def aTO_fun(self):
		try:
			aTOm2_proc    = float(self.ai_LinEd.text()) * 1e+02
			# aTOcm2_proc   = float(self.ai_LinEd.text()) * 1e+06
			# aTOmm2_proc   = float(self.ai_LinEd.text()) * 1e+08
			aTOa_proc     = float(self.ai_LinEd.text()) * 1
			aTOha_proc    = float(self.ai_LinEd.text()) * 1e-02
			aTOin2_proc   = float(self.ai_LinEd.text()) * 1.5500032e+05
			aTOft2_proc   = float(self.ai_LinEd.text()) * 1.0763910e+03
			aTOyd2_proc   = float(self.ai_LinEd.text()) * 1.1959900e+02
			aTOacr_proc   = float(self.ai_LinEd.text()) * 2.4710540e-02
			aTOmi2ST_proc = float(self.ai_LinEd.text()) * 3.8610220e-05

			self.aTOm2_res.setText(str(round(aTOm2_proc,   8)))
			self.aTOcm2_res.setText("-")
			self.aTOmm2_res.setText("-")
			self.aTOa_res.setText(str(round(aTOa_proc,     8)))
			self.aTOha_res.setText(str(round(aTOha_proc,   8)))
			self.aTOin2_res.setText(str(round(aTOin2_proc, 8)))
			self.aTOft2_res.setText(str(round(aTOft2_proc, 8)))
			self.aTOyd2_res.setText(str(round(aTOyd2_proc, 8)))
			self.aTOacr_res.setText(str(round(aTOacr_proc, 8)))
			self.aTOmi2ST_res.setText(str(round(aTOmi2ST_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def haTO_fun(self):
		try:
			haTOm2_proc    = float(self.hai_LinEd.text()) * 1e+04
			# haTOcm2_proc   = float(self.hai_LinEd.text()) * 1e+08
			# haTOmm2_proc   = float(self.hai_LinEd.text()) * 1e+10
			haTOa_proc     = float(self.hai_LinEd.text()) * 1e+02
			haTOha_proc    = float(self.hai_LinEd.text()) * 1
			# haTOin2_proc   = float(self.hai_LinEd.text()) * 1.5500031e+07
			haTOft2_proc   = float(self.hai_LinEd.text()) * 1.076391e+05
			haTOyd2_proc   = float(self.hai_LinEd.text()) * 1.195990e+04
			haTOacr_proc   = float(self.hai_LinEd.text()) * 2.471054
			haTOmi2ST_proc = float(self.hai_LinEd.text()) * 3.861022e-03

			self.haTOm2_res.setText(str(round(haTOm2_proc,       8)))
			self.haTOcm2_res.setText("-")
			self.haTOmm2_res.setText("-")
			self.haTOa_res.setText(str(round(haTOa_proc,         8)))
			self.haTOha_res.setText(str(round(haTOha_proc,       8)))
			self.haTOin2_res.setText("-")
			self.haTOft2_res.setText(str(round(haTOft2_proc,     8)))
			self.haTOyd2_res.setText(str(round(haTOyd2_proc,     8)))
			self.haTOacr_res.setText(str(round(haTOacr_proc,     8)))
			self.haTOmi2ST_res.setText(str(round(haTOmi2ST_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def in2TO_fun(self):
		try:
			in2TOm2_proc    = float(self.in2i_LinEd.text()) * 6.4516e-04
			in2TOcm2_proc   = float(self.in2i_LinEd.text()) * 6.4516
			in2TOmm2_proc   = float(self.in2i_LinEd.text()) * 6.4516e+02
			in2TOa_proc     = float(self.in2i_LinEd.text()) * 6.4516e-06
			# in2TOha_proc    = float(self.in2i_LinEd.text()) * 6.4616e-08
			in2TOin2_proc   = float(self.in2i_LinEd.text()) * 1
			in2TOft2_proc   = float(self.in2i_LinEd.text()) * 6.944444e-03
			in2TOyd2_proc   = float(self.in2i_LinEd.text()) * 7.716049e-04
			# in2TOacr_proc   = float(self.in2i_LinEd.text()) * 1.594225e-07
			# in2TOmi2ST_proc = float(self.in2i_LinEd.text()) * 2.490977e-10

			self.in2TOm2_res.setText(str(round(in2TOm2_proc,   8)))
			self.in2TOcm2_res.setText(str(round(in2TOcm2_proc, 8)))
			self.in2TOmm2_res.setText(str(round(in2TOmm2_proc, 8)))
			self.in2TOa_res.setText(str(round(in2TOa_proc,     8)))
			self.in2TOha_res.setText("-")
			self.in2TOin2_res.setText(str(round(in2TOin2_proc, 8)))
			self.in2TOft2_res.setText(str(round(in2TOft2_proc, 8)))
			self.in2TOyd2_res.setText(str(round(in2TOyd2_proc, 8)))
			self.in2TOacr_res.setText("-")
			self.in2TOmi2ST_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ft2TO_fun(self):
		try:
			ft2TOm2_proc    = float(self.ft2i_LinEd.text()) * 9.290304e-02
			ft2TOcm2_proc   = float(self.ft2i_LinEd.text()) * 9.290304e+02
			ft2TOmm2_proc   = float(self.ft2i_LinEd.text()) * 9.290304e+04
			ft2TOa_proc     = float(self.ft2i_LinEd.text()) * 9.290304e-04
			ft2TOha_proc    = float(self.ft2i_LinEd.text()) * 9.290304e-06
			ft2TOin2_proc   = float(self.ft2i_LinEd.text()) * 144
			ft2TOft2_proc   = float(self.ft2i_LinEd.text()) * 1
			ft2TOyd2_proc   = float(self.ft2i_LinEd.text()) * 1.111111e-01
			ft2TOacr_proc   = float(self.ft2i_LinEd.text()) * 2.295684e-05
			# ft2TOmi2ST_proc = float(self.ft2i_LinEd.text()) * 3.587006e-08

			self.ft2TOm2_res.setText(str(round(ft2TOm2_proc,   8)))
			self.ft2TOcm2_res.setText(str(round(ft2TOcm2_proc, 8)))
			self.ft2TOmm2_res.setText(str(round(ft2TOmm2_proc, 8)))
			self.ft2TOa_res.setText(str(round(ft2TOa_proc,     8)))
			self.ft2TOha_res.setText(str(round(ft2TOha_proc,   8)))
			self.ft2TOin2_res.setText(str(round(ft2TOin2_proc, 8)))
			self.ft2TOft2_res.setText(str(round(ft2TOft2_proc, 8)))
			self.ft2TOyd2_res.setText(str(round(ft2TOyd2_proc, 8)))
			self.ft2TOacr_res.setText(str(round(ft2TOacr_proc, 8)))
			self.ft2TOmi2ST_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def yd2TO_fun(self):
		try:
			yd2TOm2_proc    = float(self.yd2i_LinEd.text()) * 8.361274e-01
			yd2TOcm2_proc   = float(self.yd2i_LinEd.text()) * 8.361274e+03
			yd2TOmm2_proc   = float(self.yd2i_LinEd.text()) * 8.361274e+05
			yd2TOa_proc     = float(self.yd2i_LinEd.text()) * 8.361274e-03
			yd2TOha_proc    = float(self.yd2i_LinEd.text()) * 8.361274e-05
			yd2TOin2_proc   = float(self.yd2i_LinEd.text()) * 1.296e+03
			yd2TOft2_proc   = float(self.yd2i_LinEd.text()) * 9
			yd2TOyd2_proc   = float(self.yd2i_LinEd.text()) * 1
			yd2TOacr_proc   = float(self.yd2i_LinEd.text()) * 2.066116e-04
			# yd2TOmi2ST_proc = float(self.yd2i_LinEd.text()) * 3.228306e-07

			self.yd2TOm2_res.setText(str(round(yd2TOm2_proc,   8)))
			self.yd2TOcm2_res.setText(str(round(yd2TOcm2_proc, 8)))
			self.ft2TOmm2_res.setText(str(round(yd2TOmm2_proc, 8)))
			self.yd2TOa_res.setText(str(round(yd2TOa_proc,     8)))
			self.yd2TOha_res.setText(str(round(yd2TOha_proc,   8)))
			self.yd2TOin2_res.setText(str(round(yd2TOin2_proc, 8)))
			self.yd2TOft2_res.setText(str(round(yd2TOft2_proc, 8)))
			self.yd2TOyd2_res.setText(str(round(yd2TOyd2_proc, 8)))
			self.yd2TOacr_res.setText(str(round(yd2TOacr_proc, 8)))
			self.yd2TOmi2ST_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def acrTO_fun(self):
		try:
			acrTOm2_proc    = float(self.acri_LinEd.text()) * 4.046856e+03
			acrTOcm2_proc   = float(self.acri_LinEd.text()) * 4.046856e+07
			acrTOmm2_proc   = float(self.acri_LinEd.text()) * 4.046856e+09
			acrTOa_proc     = float(self.acri_LinEd.text()) * 4.046856e+01
			acrTOha_proc    = float(self.acri_LinEd.text()) * 4.046856e-01
			acrTOin2_proc   = float(self.acri_LinEd.text()) * 6.272640e+06
			acrTOft2_proc   = float(self.acri_LinEd.text()) * 4.356000e+04
			acrTOyd2_proc   = float(self.acri_LinEd.text()) * 4.830000e+03
			acrTOacr_proc   = float(self.acri_LinEd.text()) * 1
			acrTOmi2ST_proc = float(self.acri_LinEd.text()) * 1.562500e-03

			self.acrTOm2_res.setText(str(round(acrTOm2_proc,       8)))
			self.acrTOcm2_res.setText("-")
			self.acrTOmm2_res.setText("-")
			self.acrTOa_res.setText(str(round(acrTOa_proc,         8)))
			self.acrTOha_res.setText(str(round(acrTOha_proc,       8)))
			self.acrTOin2_res.setText(str(round(acrTOin2_proc,     8)))
			self.acrTOft2_res.setText(str(round(acrTOft2_proc,     8)))
			self.acrTOyd2_res.setText(str(round(acrTOyd2_proc,     8)))
			self.acrTOacr_res.setText(str(round(acrTOacr_proc,     8)))
			self.acrTOmi2ST_res.setText(str(round(acrTOmi2ST_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def mi2STTO_fun(self):
		try:
			mi2STTOm2_proc    = float(self.mi2STi_LinEd.text()) * 2.589988e+06
			# mi2STTOcm2_proc   = float(self.mi2STi_LinEd.text()) * 2.589988e+10
			# mi2STTOmm2_proc   = float(self.mi2STi_LinEd.text()) * 2.589988e+12
			mi2STTOa_proc     = float(self.mi2STi_LinEd.text()) * 2.589988e+04
			mi2STTOha_proc    = float(self.mi2STi_LinEd.text()) * 2.589988e+02
			# mi2STTOin2_proc   = float(self.mi2STi_LinEd.text()) * 4.0144896e+09
			mi2STTOft2_proc   = float(self.mi2STi_LinEd.text()) * 2.7878400e+07
			mi2STTOyd2_proc   = float(self.mi2STi_LinEd.text()) * 3.0976000e+06
			mi2STTOacr_proc   = float(self.mi2STi_LinEd.text()) * 6.4e+02
			mi2STTOmi2ST_proc = float(self.mi2STi_LinEd.text()) * 1

			self.mi2STTOm2_res.setText(str(round(mi2STTOm2_proc,       8)))
			self.mi2STTOcm2_res.setText("-")
			self.mi2STTOmm2_res.setText("-")
			self.mi2STTOa_res.setText(str(round(mi2STTOa_proc,         8)))
			self.mi2STTOha_res.setText(str(round(mi2STTOha_proc,       8)))
			self.mi2STTOin2_res.setText("-")
			self.mi2STTOft2_res.setText(str(round(mi2STTOft2_proc,     8)))
			self.mi2STTOyd2_res.setText(str(round(mi2STTOyd2_proc,     8)))
			self.mi2STTOacr_res.setText(str(round(mi2STTOacr_proc,     8)))
			self.mi2STTOmi2ST_res.setText(str(round(mi2STTOmi2ST_proc, 8)))
		
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
