# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Dens_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Density Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel         = QtWidgets.QLabel()
		self.kgm3i_LinEd   = QtWidgets.QLineEdit()
		self.gcm3i_LinEd   = QtWidgets.QLineEdit()
		self.lbft3i_LinEd  = QtWidgets.QLineEdit()
		self.lbbbli_LinEd  = QtWidgets.QLineEdit()
		self.ggalUSi_LinEd = QtWidgets.QLineEdit()
		self.ggalUKi_LinEd = QtWidgets.QLineEdit()

		LinEd_list = [self.kgm3i_LinEd, self.gcm3i_LinEd, self.lbft3i_LinEd, self.lbbbli_LinEd, self.ggalUSi_LinEd, self.ggalUKi_LinEd]
		
		Label_list = [blanklabel, "kg/m\u00B3", "g/cm\u00B3", "lb/ft\u00B3", "lb/bbl", "g/gal<sub>US</sub>", "g/gal<sub>UK</sub>"]

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

		self.kgm3i_LinEd.returnPressed.connect(self.kgm3TO_fun)
		self.gcm3i_LinEd.returnPressed.connect(self.gcm3TO_fun)
		self.lbft3i_LinEd.returnPressed.connect(self.lbft3TO_fun)
		self.lbbbli_LinEd.returnPressed.connect(self.lbbblTO_fun)
		self.ggalUSi_LinEd.returnPressed.connect(self.ggalUSTO_fun)
		self.ggalUKi_LinEd.returnPressed.connect(self.ggalUKTO_fun)
		
		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10)) #, 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["kg/m\u00B3", "g/cm\u00B3", "lb/ft\u00B3", "lb/bbl", "g/gal<sub>US</sub>", "g/gal<sub>UK</sub>"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.kgm3TOkgm3_res   = QtWidgets.QLabel("0", self)
		self.kgm3TOgcm3_res   = QtWidgets.QLabel("0", self)
		self.kgm3TOlbft3_res  = QtWidgets.QLabel("0", self)
		self.kgm3TOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.kgm3TOggalUS_res = QtWidgets.QLabel("0", self)
		self.kgm3TOggalUK_res = QtWidgets.QLabel("0", self)

		self.gcm3TOkgm3_res   = QtWidgets.QLabel("0", self)
		self.gcm3TOgcm3_res   = QtWidgets.QLabel("0", self)
		self.gcm3TOlbft3_res  = QtWidgets.QLabel("0", self)
		self.gcm3TOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.gcm3TOggalUS_res = QtWidgets.QLabel("0", self)
		self.gcm3TOggalUK_res = QtWidgets.QLabel("0", self)

		self.lbft3TOkgm3_res   = QtWidgets.QLabel("0", self)
		self.lbft3TOgcm3_res   = QtWidgets.QLabel("0", self)
		self.lbft3TOlbft3_res  = QtWidgets.QLabel("0", self)
		self.lbft3TOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.lbft3TOggalUS_res = QtWidgets.QLabel("0", self)
		self.lbft3TOggalUK_res = QtWidgets.QLabel("0", self)

		self.lbbblTOkgm3_res   = QtWidgets.QLabel("0", self)
		self.lbbblTOgcm3_res   = QtWidgets.QLabel("0", self)
		self.lbbblTOlbft3_res  = QtWidgets.QLabel("0", self)
		self.lbbblTOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.lbbblTOggalUS_res = QtWidgets.QLabel("0", self)
		self.lbbblTOggalUK_res = QtWidgets.QLabel("0", self)

		self.ggalUSTOkgm3_res   = QtWidgets.QLabel("0", self)
		self.ggalUSTOgcm3_res   = QtWidgets.QLabel("0", self)
		self.ggalUSTOlbft3_res  = QtWidgets.QLabel("0", self)
		self.ggalUSTOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.ggalUSTOggalUS_res = QtWidgets.QLabel("0", self)
		self.ggalUSTOggalUK_res = QtWidgets.QLabel("0", self)

		self.ggalUKTOkgm3_res   = QtWidgets.QLabel("0", self)
		self.ggalUKTOgcm3_res   = QtWidgets.QLabel("0", self)
		self.ggalUKTOlbft3_res  = QtWidgets.QLabel("0", self)
		self.ggalUKTOlbbbl_res  = QtWidgets.QLabel("0", self)
		self.ggalUKTOggalUS_res = QtWidgets.QLabel("0", self)
		self.ggalUKTOggalUK_res = QtWidgets.QLabel("0", self)
		

		kgm3TO_Label = [self.kgm3TOkgm3_res, self.kgm3TOgcm3_res, self.kgm3TOlbft3_res, self.kgm3TOlbbbl_res, self.kgm3TOggalUS_res, self.kgm3TOggalUK_res]

		gcm3TO_Label = [self.gcm3TOkgm3_res, self.gcm3TOgcm3_res, self.gcm3TOlbft3_res, self.gcm3TOlbbbl_res, self.gcm3TOggalUS_res, self.gcm3TOggalUK_res]

		lbft3TO_Label = [self.lbft3TOkgm3_res, self.lbft3TOgcm3_res, self.lbft3TOlbft3_res, self.lbft3TOlbbbl_res, self.lbft3TOggalUS_res, 
						 self.lbft3TOggalUK_res]

		lbbblTO_Label = [self.lbbblTOkgm3_res, self.lbbblTOgcm3_res, self.lbbblTOlbft3_res, self.lbbblTOlbbbl_res, self.lbbblTOggalUS_res, self.lbbblTOggalUK_res]

		ggalUSTO_Label = [self.ggalUSTOkgm3_res, self.ggalUSTOgcm3_res, self.ggalUSTOlbft3_res, self.ggalUSTOlbbbl_res, self.ggalUSTOggalUS_res,
						  self.ggalUSTOggalUK_res]

		ggalUKTO_Label = [self.ggalUKTOkgm3_res, self.ggalUKTOgcm3_res, self.ggalUKTOlbft3_res, self.ggalUKTOlbbbl_res, self.ggalUKTOggalUS_res,
						  self.ggalUKTOggalUK_res]

		i = 0
		for item in kgm3TO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in gcm3TO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in lbft3TO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in lbbblTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ggalUSTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ggalUKTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1


		output_group.setLayout(output_grid)

		return output_group
		

	def kgm3TO_fun(self):
		try:
			kgm3TOkgm3_proc   = float(self.kgm3i_LinEd.text()) * 1
			kgm3TOgcm3_proc   = float(self.kgm3i_LinEd.text()) * 1e-03
			kgm3TOlbft3_proc  = float(self.kgm3i_LinEd.text()) * 6.2428e-02
			kgm3TOlbbbl_proc  = float(self.kgm3i_LinEd.text()) * 3.50507e-01
			kgm3TOggalUS_proc = float(self.kgm3i_LinEd.text()) * 3.785413
			kgm3TOggalUK_proc = float(self.kgm3i_LinEd.text()) * 4.546091

			self.kgm3TOkgm3_res.setText(str(round(kgm3TOkgm3_proc,     8)))
			self.kgm3TOgcm3_res.setText(str(round(kgm3TOgcm3_proc,     8)))
			self.kgm3TOlbft3_res.setText(str(round(kgm3TOlbft3_proc,   8)))
			self.kgm3TOlbbbl_res.setText(str(round(kgm3TOlbbbl_proc,   8)))
			self.kgm3TOggalUS_res.setText(str(round(kgm3TOggalUS_proc, 8)))
			self.kgm3TOggalUK_res.setText(str(round(kgm3TOggalUK_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def gcm3TO_fun(self):
		try:
			gcm3TOkgm3_proc   = float(self.gcm3i_LinEd.text()) * 1e+03
			gcm3TOgcm3_proc   = float(self.gcm3i_LinEd.text()) * 1
			gcm3TOlbft3_proc  = float(self.gcm3i_LinEd.text()) * 6.2428e+01
			gcm3TOlbbbl_proc  = float(self.gcm3i_LinEd.text()) * 3.50507e+02
			gcm3TOggalUS_proc = float(self.gcm3i_LinEd.text()) * 3.785413e+03
			gcm3TOggalUK_proc = float(self.gcm3i_LinEd.text()) * 4.546091e+03

			self.gcm3TOkgm3_res.setText(str(round(gcm3TOkgm3_proc,     8)))
			self.gcm3TOgcm3_res.setText(str(round(gcm3TOgcm3_proc,     8)))
			self.gcm3TOlbft3_res.setText(str(round(gcm3TOlbft3_proc,   8)))
			self.gcm3TOlbbbl_res.setText(str(round(gcm3TOlbbbl_proc,   8)))
			self.gcm3TOggalUS_res.setText(str(round(gcm3TOggalUS_proc, 8)))
			self.gcm3TOggalUK_res.setText(str(round(gcm3TOggalUK_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def lbft3TO_fun(self):
		try:
			lbft3TOkgm3_proc   = float(self.lbft3i_LinEd.text()) * 16.018464
			lbft3TOgcm3_proc   = float(self.lbft3i_LinEd.text()) * 16.018464e-03
			lbft3TOlbft3_proc  = float(self.lbft3i_LinEd.text()) * 1
			lbft3TOlbbbl_proc  = float(self.lbft3i_LinEd.text()) * 5.6145838
			lbft3TOggalUS_proc = float(self.lbft3i_LinEd.text()) * 60.636504
			lbft3TOggalUK_proc = float(self.lbft3i_LinEd.text()) * 72.821397

			self.lbft3TOkgm3_res.setText(str(round(lbft3TOkgm3_proc,     8)))
			self.lbft3TOgcm3_res.setText(str(round(lbft3TOgcm3_proc,     8)))
			self.lbft3TOlbft3_res.setText(str(round(lbft3TOlbft3_proc,   8)))
			self.lbft3TOlbbbl_res.setText(str(round(lbft3TOlbbbl_proc,   8)))
			self.lbft3TOggalUS_res.setText(str(round(lbft3TOggalUS_proc, 8)))
			self.lbft3TOggalUK_res.setText(str(round(lbft3TOggalUK_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def lbbblTO_fun(self):
		try:
			lbbblTOkgm3_proc   = float(self.lbbbli_LinEd.text()) * 2.8530101
			lbbblTOgcm3_proc   = float(self.lbbbli_LinEd.text()) * 2.8530101e-03
			lbbblTOlbft3_proc  = float(self.lbbbli_LinEd.text()) * 0.1781076
			lbbblTOlbbbl_proc  = float(self.lbbbli_LinEd.text()) * 1
			lbbblTOggalUS_proc = float(self.lbbbli_LinEd.text()) * 10.799821
			lbbblTOggalUK_proc = float(self.lbbbli_LinEd.text()) * 12.970043

			self.lbbblTOkgm3_res.setText(str(round(lbbblTOkgm3_proc,     8)))
			self.lbbblTOgcm3_res.setText(str(round(lbbblTOgcm3_proc,     8)))
			self.lbbblTOlbft3_res.setText(str(round(lbbblTOlbft3_proc,   8)))
			self.lbbblTOlbbbl_res.setText(str(round(lbbblTOlbbbl_proc,   8)))
			self.lbbblTOggalUS_res.setText(str(round(lbbblTOggalUS_proc, 8)))
			self.lbbblTOggalUK_res.setText(str(round(lbbblTOggalUK_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ggalUSTO_fun(self):
		try:
			ggalUSTOkgm3_proc   = float(self.ggalUSi_LinEd.text()) * 2.64172e-01
			ggalUSTOgcm3_proc   = float(self.ggalUSi_LinEd.text()) * 2.64172e-04
			ggalUSTOlbft3_proc  = float(self.ggalUSi_LinEd.text()) * 1.64917e-02
			ggalUSTOlbbbl_proc  = float(self.ggalUSi_LinEd.text()) * 9.25941e-02
			ggalUSTOggalUS_proc = float(self.ggalUSi_LinEd.text()) * 1
			ggalUSTOggalUK_proc = float(self.ggalUSi_LinEd.text()) * 1.2009498

			self.ggalUSTOkgm3_res.setText(str(round(ggalUSTOkgm3_proc,     8)))
			self.ggalUSTOgcm3_res.setText(str(round(ggalUSTOgcm3_proc,     8)))
			self.ggalUSTOlbft3_res.setText(str(round(ggalUSTOlbft3_proc,   8)))
			self.ggalUSTOlbbbl_res.setText(str(round(ggalUSTOlbbbl_proc,   8)))
			self.ggalUSTOggalUS_res.setText(str(round(ggalUSTOggalUS_proc, 8)))
			self.ggalUSTOggalUK_res.setText(str(round(ggalUSTOggalUK_proc, 8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ggalUKTO_fun(self):
		try:
			ggalUKTOkgm3_proc   = float(self.ggalUKi_LinEd.text()) * 2.199692e-01
			ggalUKTOgcm3_proc   = float(self.ggalUKi_LinEd.text()) * 2.199692e-04
			ggalUKTOlbft3_proc  = float(self.ggalUKi_LinEd.text()) * 1.37322e-02
			ggalUKTOlbbbl_proc  = float(self.ggalUKi_LinEd.text()) * 7.71007e-02
			ggalUKTOggalUS_proc = float(self.ggalUKi_LinEd.text()) * 8.326743e-01
			ggalUKTOggalUK_proc = float(self.ggalUKi_LinEd.text()) * 1

			self.ggalUKTOkgm3_res.setText(str(round(ggalUKTOkgm3_proc,     8)))
			self.ggalUKTOgcm3_res.setText(str(round(ggalUKTOgcm3_proc,     8)))
			self.ggalUKTOlbft3_res.setText(str(round(ggalUKTOlbft3_proc,   8)))
			self.ggalUKTOlbbbl_res.setText(str(round(ggalUKTOlbbbl_proc,   8)))
			self.ggalUKTOggalUS_res.setText(str(round(ggalUKTOggalUS_proc, 8)))
			self.ggalUKTOggalUK_res.setText(str(round(ggalUKTOggalUK_proc, 8)))
		
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
