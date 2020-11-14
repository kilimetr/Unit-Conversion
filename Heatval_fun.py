# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Heatval_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		
		self.setWindowTitle("Heat Volumetric Flow Rate Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)
		
		blanklabel              = QtWidgets.QLabel()
		self.BTUft3i_LinEd      = QtWidgets.QLineEdit()
		self.BTUgalUKi_LinEd    = QtWidgets.QLineEdit()
		self.BTUgalUSi_LinEd    = QtWidgets.QLineEdit()
		self.kJm3i_LinEd	    = QtWidgets.QLineEdit()
		self.kWhm3i_LinEd	    = QtWidgets.QLineEdit()
		self.MJm3_kJdm3i_LinEd	= QtWidgets.QLineEdit()

		Label_list = [blanklabel, "BTU/ft\u00B3", "BTU/gal<sub>UK</sub>", "BTU/gal<sub>US</sub>", "kJ/m\u00B3", "kWh/m\u00B3", "MJ/m\u00B3 & kJ/dm\u00B3"]
		
		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		LinEd_list = [self.BTUft3i_LinEd, self.BTUgalUKi_LinEd, self.BTUgalUSi_LinEd, self.kJm3i_LinEd, self.kWhm3i_LinEd, self.MJm3_kJdm3i_LinEd]
		
		i = 1
		for item in LinEd_list:
			input_grid.addWidget(item, i, 0)
			i = i + 1

		input_group.setLayout(input_grid)

		self.BTUft3i_LinEd.returnPressed.connect(self.BTUft3TO_fun)
		self.BTUgalUKi_LinEd.returnPressed.connect(self.BTUgalUKTO_fun)
		self.BTUgalUSi_LinEd.returnPressed.connect(self.BTUgalUSTO_fun)
		self.kJm3i_LinEd.returnPressed.connect(self.kJm3TO_fun)
		self.kWhm3i_LinEd.returnPressed.connect(self.kWhm3TO_fun)
		self.MJm3_kJdm3i_LinEd.returnPressed.connect(self.MJm3_kJdm3TO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["BTU/ft\u00B3", "BTU/gal<sub>UK</sub>", "BTU/gal<sub>US</sub>", "kJ/m\u00B3", "kWh/m\u00B3", "MJ/m\u00B3 & kJ/dm\u00B3"]
		
		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.BTUft3TOBTUft3_res      = QtWidgets.QLabel("0", self)
		self.BTUft3TOBTUgalUK_res    = QtWidgets.QLabel("0", self)
		self.BTUft3TOBTUgalUS_res    = QtWidgets.QLabel("0", self)
		self.BTUft3TOkJm3_res        = QtWidgets.QLabel("0", self)
		self.BTUft3TOkWhm3_res       = QtWidgets.QLabel("0", self)
		self.BTUft3TOMJm3_kJdm3_res  = QtWidgets.QLabel("0", self)

		self.BTUgalUKTOBTUft3_res     = QtWidgets.QLabel("0", self)
		self.BTUgalUKTOBTUgalUK_res   = QtWidgets.QLabel("0", self)
		self.BTUgalUKTOBTUgalUS_res   = QtWidgets.QLabel("0", self)
		self.BTUgalUKTOkJm3_res       = QtWidgets.QLabel("0", self)
		self.BTUgalUKTOkWhm3_res      = QtWidgets.QLabel("0", self)
		self.BTUgalUKTOMJm3_kJdm3_res = QtWidgets.QLabel("0", self)

		self.BTUgalUSTOBTUft3_res     = QtWidgets.QLabel("0", self)
		self.BTUgalUSTOBTUgalUK_res   = QtWidgets.QLabel("0", self)
		self.BTUgalUSTOBTUgalUS_res   = QtWidgets.QLabel("0", self)
		self.BTUgalUSTOkJm3_res       = QtWidgets.QLabel("0", self)
		self.BTUgalUSTOkWhm3_res      = QtWidgets.QLabel("0", self)
		self.BTUgalUSTOMJm3_kJdm3_res = QtWidgets.QLabel("0", self)

		self.kJm3TOBTUft3_res     = QtWidgets.QLabel("0", self)
		self.kJm3TOBTUgalUK_res   = QtWidgets.QLabel("0", self)
		self.kJm3TOBTUgalUS_res   = QtWidgets.QLabel("0", self)
		self.kJm3TOkJm3_res       = QtWidgets.QLabel("0", self)
		self.kJm3TOkWhm3_res      = QtWidgets.QLabel("0", self)
		self.kJm3TOMJm3_kJdm3_res = QtWidgets.QLabel("0", self)

		self.kWhm3TOBTUft3_res     = QtWidgets.QLabel("0", self)
		self.kWhm3TOBTUgalUK_res   = QtWidgets.QLabel("0", self)
		self.kWhm3TOBTUgalUS_res   = QtWidgets.QLabel("0", self)
		self.kWhm3TOkJm3_res       = QtWidgets.QLabel("0", self)
		self.kWhm3TOkWhm3_res      = QtWidgets.QLabel("0", self)
		self.kWhm3TOMJm3_kJdm3_res = QtWidgets.QLabel("0", self)

		self.MJm3_kJdm3TOBTUft3_res     = QtWidgets.QLabel("0", self)
		self.MJm3_kJdm3TOBTUgalUK_res   = QtWidgets.QLabel("0", self)
		self.MJm3_kJdm3TOBTUgalUS_res   = QtWidgets.QLabel("0", self)
		self.MJm3_kJdm3TOkJm3_res       = QtWidgets.QLabel("0", self)
		self.MJm3_kJdm3TOkWhm3_res      = QtWidgets.QLabel("0", self)
		self.MJm3_kJdm3TOMJm3_kJdm3_res = QtWidgets.QLabel("0", self)

		BTUft3TO_Label = [self.BTUft3TOBTUft3_res, self.BTUft3TOBTUgalUK_res, self.BTUft3TOBTUgalUS_res, self.BTUft3TOkJm3_res, self.BTUft3TOkWhm3_res, 
						  self.BTUft3TOMJm3_kJdm3_res]

		BTUgalUKTO_Label = [self.BTUgalUKTOBTUft3_res, self.BTUgalUKTOBTUgalUK_res, self.BTUgalUKTOBTUgalUS_res, self.BTUgalUKTOkJm3_res, self.BTUgalUKTOkWhm3_res, 
							self.BTUgalUKTOMJm3_kJdm3_res]

		BTUgalUSTO_Label = [self.BTUgalUSTOBTUft3_res, self.BTUgalUSTOBTUgalUK_res, self.BTUgalUSTOBTUgalUS_res, self.BTUgalUSTOkJm3_res, self.BTUgalUSTOkWhm3_res, 
							self.BTUgalUSTOMJm3_kJdm3_res]

		kJm3TO_Label = [self.kJm3TOBTUft3_res, self.kJm3TOBTUgalUK_res, self.kJm3TOBTUgalUS_res, self.kJm3TOkJm3_res, self.kJm3TOkWhm3_res, 
						self.kJm3TOMJm3_kJdm3_res]

		kWhm3TO_Label = [self.kWhm3TOBTUft3_res, self.kWhm3TOBTUgalUK_res, self.kWhm3TOBTUgalUS_res, self.kWhm3TOkJm3_res, self.kWhm3TOkWhm3_res, 
						 self.kWhm3TOMJm3_kJdm3_res]

		kWhm3TO_Label = [self.kWhm3TOBTUft3_res, self.kWhm3TOBTUgalUK_res, self.kWhm3TOBTUgalUS_res, self.kWhm3TOkJm3_res, self.kWhm3TOkWhm3_res, 
						 self.kWhm3TOMJm3_kJdm3_res]

		MJm3_kJdm3TO_Label = [self.MJm3_kJdm3TOBTUft3_res, self.MJm3_kJdm3TOBTUgalUK_res, self.MJm3_kJdm3TOBTUgalUS_res, self.MJm3_kJdm3TOkJm3_res, 
							  self.MJm3_kJdm3TOkWhm3_res, self.MJm3_kJdm3TOMJm3_kJdm3_res]						 
		i = 0
		for item in BTUft3TO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in BTUgalUKTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		
		i = 0
		for item in BTUgalUSTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kJm3TO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kWhm3TO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in MJm3_kJdm3TO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def BTUft3TO_fun(self):
		try:
			BTUft3TOBTUft3_proc     = float(self.BTUft3i_LinEd.text()) * 1
			BTUft3TOBTUgalUK_proc   = float(self.BTUft3i_LinEd.text()) * 1.60544e-01
			BTUft3TOBTUgalUS_proc   = float(self.BTUft3i_LinEd.text()) * 1.336808e-01
			BTUft3TOkJm3_proc       = float(self.BTUft3i_LinEd.text()) * 3.725895e+01
			BTUft3TOkWhm3_proc      = float(self.BTUft3i_LinEd.text()) * 1.03497e-02
			BTUft3TOMJm3_kJdm3_proc = float(self.BTUft3i_LinEd.text()) * 3.72589e-02

			self.BTUft3TOBTUft3_res.setText(str(round(BTUft3TOBTUft3_proc,         8)))
			self.BTUft3TOBTUgalUK_res.setText(str(round(BTUft3TOBTUgalUK_proc,     8)))
			self.BTUft3TOBTUgalUS_res.setText(str(round(BTUft3TOBTUgalUS_proc,     8)))
			self.BTUft3TOkJm3_res.setText(str(round(BTUft3TOkJm3_proc,             8)))
			self.BTUft3TOkWhm3_res.setText(str(round(BTUft3TOkWhm3_proc,           8)))
			self.BTUft3TOMJm3_kJdm3_res.setText(str(round(BTUft3TOMJm3_kJdm3_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def BTUgalUKTO_fun(self):
		try:
			BTUgalUKTOBTUft3_proc    = float(self.BTUgalUKi_LinEd.text()) * 6.228823
			BTUgalUKTOBTUgalUK_proc  = float(self.BTUgalUKi_LinEd.text()) * 1
			BTUgalUKTOBTUgalUS_proc  = float(self.BTUgalUKi_LinEd.text()) * 8.326739e-01
			BTUgalUKTOkJm3_proc      = float(self.BTUgalUKi_LinEd.text()) * 2.320794e+02
			BTUgalUKTOkWhm3_proc     = float(self.BTUgalUKi_LinEd.text()) * 6.44665e-02
			BTUgalUKTOMJm3_kJm3_proc = float(self.BTUgalUKi_LinEd.text()) * 2.320794e-01

			self.BTUgalUKTOBTUft3_res.setText(str(round(BTUgalUKTOBTUft3_proc,        8)))
			self.BTUgalUKTOBTUgalUK_res.setText(str(round(BTUgalUKTOBTUgalUK_proc,    8)))
			self.BTUgalUKTOBTUgalUS_res.setText(str(round(BTUgalUKTOBTUgalUS_proc,    8)))
			self.BTUgalUKTOkJm3_res.setText(str(round(BTUgalUKTOkJm3_proc,            8)))
			self.BTUgalUKTOkWhm3_res.setText(str(round(BTUgalUKTOkWhm3_proc,          8)))
			self.BTUgalUKTOMJm3_kJdm3_res.setText(str(round(BTUgalUKTOMJm3_kJm3_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def BTUgalUSTO_fun(self):
		try:
			BTUgalUSTOBTUft3_proc     = float(self.BTUgalUSi_LinEd.text()) * 7.480507
			BTUgalUSTOBTUgalUK_proc   = float(self.BTUgalUSi_LinEd.text()) * 1.2009503
			BTUgalUSTOBTUgalUS_proc   = float(self.BTUgalUSi_LinEd.text()) * 1
			BTUgalUSTOkJm3_proc       = float(self.BTUgalUSi_LinEd.text()) * 2.7871584e+02
			BTUgalUSTOkWhm3_proc      = float(self.BTUgalUSi_LinEd.text()) * 7.74211e-02
			BTUgalUSTOMJm3_kJdm3_proc = float(self.BTUgalUSi_LinEd.text()) * 2.787158e-01

			self.BTUgalUSTOBTUft3_res.setText(str(round(BTUgalUSTOBTUft3_proc,         8)))
			self.BTUgalUSTOBTUgalUK_res.setText(str(round(BTUgalUSTOBTUgalUK_proc,     8)))
			self.BTUgalUSTOBTUgalUS_res.setText(str(round(BTUgalUSTOBTUgalUS_proc,     8)))
			self.BTUgalUSTOkJm3_res.setText(str(round(BTUgalUSTOkJm3_proc,             8)))
			self.BTUgalUSTOkWhm3_res.setText(str(round(BTUgalUSTOkWhm3_proc,           8)))
			self.BTUgalUSTOMJm3_kJdm3_res.setText(str(round(BTUgalUSTOMJm3_kJdm3_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def kJm3TO_fun(self):
		try:
			kJm3TOBTUft3_proc     = float(self.kJm3i_LinEd.text()) * 2.68392e-02
			kJm3TOBTUgalUK_proc   = float(self.kJm3i_LinEd.text()) * 4.3089e-03
			kJm3TOBTUgalUS_proc   = float(self.kJm3i_LinEd.text()) * 3.5879e-03
			kJm3TOkJm3_proc       = float(self.kJm3i_LinEd.text()) * 1
			kJm3TOkWhm3_proc      = float(self.kJm3i_LinEd.text()) * 2.778e-04
			kJm3TOMJm3_kJdm3_proc = float(self.kJm3i_LinEd.text()) * 1e-03

			self.kJm3TOBTUft3_res.setText(str(round(kJm3TOBTUft3_proc,         8)))
			self.kJm3TOBTUgalUK_res.setText(str(round(kJm3TOBTUgalUK_proc,     8)))
			self.kJm3TOBTUgalUS_res.setText(str(round(kJm3TOBTUgalUS_proc,     8)))
			self.kJm3TOkJm3_res.setText(str(round(kJm3TOkJm3_proc,             8)))
			self.kJm3TOkWhm3_res.setText(str(round(kJm3TOkWhm3_proc,           8)))
			self.kJm3TOMJm3_kJdm3_res.setText(str(round(kJm3TOMJm3_kJdm3_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def kWhm3TO_fun(self):
		try:
			kWhm3TOBTUft3_proc     = float(self.kWhm3i_LinEd.text()) * 9.662108e+01
			kWhm3TOBTUgalUK_proc   = float(self.kWhm3i_LinEd.text()) * 1.5511932e+01
			kWhm3TOBTUgalUS_proc   = float(self.kWhm3i_LinEd.text()) * 1.2916381e+01
			kWhm3TOkJm3_proc       = float(self.kWhm3i_LinEd.text()) * 3.6e+03
			kWhm3TOkWhm3_proc      = float(self.kWhm3i_LinEd.text()) * 1
			kWhm3TOMJm3_kJdm3_proc = float(self.kWhm3i_LinEd.text()) * 3.6

			self.kWhm3TOBTUft3_res.setText(str(round(kWhm3TOBTUft3_proc,         8)))
			self.kWhm3TOBTUgalUK_res.setText(str(round(kWhm3TOBTUgalUK_proc,     8)))
			self.kWhm3TOBTUgalUS_res.setText(str(round(kWhm3TOBTUgalUS_proc,     8)))
			self.kWhm3TOkJm3_res.setText(str(round(kWhm3TOkJm3_proc,             8)))
			self.kWhm3TOkWhm3_res.setText(str(round(kWhm3TOkWhm3_proc,           8)))
			self.kWhm3TOMJm3_kJdm3_res.setText(str(round(kWhm3TOMJm3_kJdm3_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def MJm3_kJdm3TO_fun(self):
		try:
			MJm3_kJdm3TOBTUft3_proc     = float(self.MJm3_kJdm3i_LinEd.text()) * 2.6839189e+01
			MJm3_kJdm3TOBTUgalUK_proc   = float(self.MJm3_kJdm3i_LinEd.text()) * 4.3088701
			MJm3_kJdm3TOBTUgalUS_proc   = float(self.MJm3_kJdm3i_LinEd.text()) * 3.5878837
			MJm3_kJdm3TOkJm3_proc       = float(self.MJm3_kJdm3i_LinEd.text()) * 1000
			MJm3_kJdm3TOkWhm3_proc      = float(self.MJm3_kJdm3i_LinEd.text()) * 2.777778e-01
			MJm3_kJdm3TOMJm3_kJdm3_proc = float(self.MJm3_kJdm3i_LinEd.text()) * 1

			self.MJm3_kJdm3TOBTUft3_res.setText(str(round(MJm3_kJdm3TOBTUft3_proc,         8)))
			self.MJm3_kJdm3TOBTUgalUK_res.setText(str(round(MJm3_kJdm3TOBTUgalUK_proc,     8)))
			self.MJm3_kJdm3TOBTUgalUS_res.setText(str(round(MJm3_kJdm3TOBTUgalUS_proc,     8)))
			self.MJm3_kJdm3TOkJm3_res.setText(str(round(MJm3_kJdm3TOkJm3_proc,             8)))
			self.MJm3_kJdm3TOkWhm3_res.setText(str(round(MJm3_kJdm3TOkWhm3_proc,           8)))
			self.MJm3_kJdm3TOMJm3_kJdm3_res.setText(str(round(MJm3_kJdm3TOMJm3_kJdm3_proc, 8)))
		
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
		