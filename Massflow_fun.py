# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Massflow_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Mass Flow Rate Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel       = QtWidgets.QLabel()
		self.gsi_LinEd   = QtWidgets.QLineEdit()
		self.gmini_LinEd = QtWidgets.QLineEdit()
		self.kgsi_LinEd  = QtWidgets.QLineEdit()
		self.kghi_LinEd  = QtWidgets.QLineEdit()
		self.kgdi_LinEd  = QtWidgets.QLineEdit()
		self.tonsi_LinEd = QtWidgets.QLineEdit()
		self.tonhi_LinEd = QtWidgets.QLineEdit()
		self.tondi_LinEd = QtWidgets.QLineEdit()
		self.lbsi_LinEd  = QtWidgets.QLineEdit()
		self.lbhi_LinEd  = QtWidgets.QLineEdit()
		self.lbdi_LinEd  = QtWidgets.QLineEdit()

		LinEd_list = [self.gsi_LinEd, self.gmini_LinEd, self.kgsi_LinEd, self.kghi_LinEd, self.kgdi_LinEd, self.tonsi_LinEd, self.tonhi_LinEd, self.tondi_LinEd, 
					  self.lbsi_LinEd, self.lbhi_LinEd, self.lbdi_LinEd]

		Label_list = [blanklabel, "g/sec", "g/min", "kg/sec", "kg/hour", "kg/day", "ton/sec", "ton/hour", "ton/day", "lb/sec", "lb/hour", "lb/day"]
		
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

		self.gsi_LinEd.returnPressed.connect(self.gsTO_fun)
		self.gmini_LinEd.returnPressed.connect(self.gminTO_fun)
		self.kgsi_LinEd.returnPressed.connect(self.kgsTO_fun)
		self.kghi_LinEd.returnPressed.connect(self.kghTO_fun)
		self.kgdi_LinEd.returnPressed.connect(self.kgdTO_fun)
		self.tonsi_LinEd.returnPressed.connect(self.tonsTO_fun)
		self.tonhi_LinEd.returnPressed.connect(self.tonhTO_fun)
		self.tondi_LinEd.returnPressed.connect(self.tondTO_fun)
		self.lbsi_LinEd.returnPressed.connect(self.lbsTO_fun)
		self.lbhi_LinEd.returnPressed.connect(self.lbhTO_fun)
		self.lbdi_LinEd.returnPressed.connect(self.lbdTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["g/sec", "g/min", "kg/sec", "kg/hour", "kg/day", "ton/sec", "ton/hour", "ton/day", "lb/sec", "lb/hour", "lb/day"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.gsTOgs_res   = QtWidgets.QLabel("0", self)
		self.gsTOgmin_res = QtWidgets.QLabel("0", self)
		self.gsTOkgs_res  = QtWidgets.QLabel("0", self)
		self.gsTOkgh_res  = QtWidgets.QLabel("0", self)
		self.gsTOkgd_res  = QtWidgets.QLabel("0", self)
		self.gsTOtons_res = QtWidgets.QLabel("0", self)
		self.gsTOtonh_res = QtWidgets.QLabel("0", self)
		self.gsTOtond_res = QtWidgets.QLabel("0", self)
		self.gsTOlbs_res  = QtWidgets.QLabel("0", self)
		self.gsTOlbh_res  = QtWidgets.QLabel("0", self)
		self.gsTOlbd_res  = QtWidgets.QLabel("0", self)

		self.gminTOgs_res   = QtWidgets.QLabel("0", self)
		self.gminTOgmin_res = QtWidgets.QLabel("0", self)
		self.gminTOkgs_res  = QtWidgets.QLabel("0", self)
		self.gminTOkgh_res  = QtWidgets.QLabel("0", self)
		self.gminTOkgd_res  = QtWidgets.QLabel("0", self)
		self.gminTOtons_res = QtWidgets.QLabel("0", self)
		self.gminTOtonh_res = QtWidgets.QLabel("0", self)
		self.gminTOtond_res = QtWidgets.QLabel("0", self)
		self.gminTOlbs_res  = QtWidgets.QLabel("0", self)
		self.gminTOlbh_res  = QtWidgets.QLabel("0", self)
		self.gminTOlbd_res  = QtWidgets.QLabel("0", self)

		self.kgsTOgs_res   = QtWidgets.QLabel("0", self)
		self.kgsTOgmin_res = QtWidgets.QLabel("0", self)
		self.kgsTOkgs_res  = QtWidgets.QLabel("0", self)
		self.kgsTOkgh_res  = QtWidgets.QLabel("0", self)
		self.kgsTOkgd_res  = QtWidgets.QLabel("0", self)
		self.kgsTOtons_res = QtWidgets.QLabel("0", self)
		self.kgsTOtonh_res = QtWidgets.QLabel("0", self)
		self.kgsTOtond_res = QtWidgets.QLabel("0", self)
		self.kgsTOlbs_res  = QtWidgets.QLabel("0", self)
		self.kgsTOlbh_res  = QtWidgets.QLabel("0", self)
		self.kgsTOlbd_res  = QtWidgets.QLabel("0", self)

		self.kghTOgs_res   = QtWidgets.QLabel("0", self)
		self.kghTOgmin_res = QtWidgets.QLabel("0", self)
		self.kghTOkgs_res  = QtWidgets.QLabel("0", self)
		self.kghTOkgh_res  = QtWidgets.QLabel("0", self)
		self.kghTOkgd_res  = QtWidgets.QLabel("0", self)
		self.kghTOtons_res = QtWidgets.QLabel("0", self)
		self.kghTOtonh_res = QtWidgets.QLabel("0", self)
		self.kghTOtond_res = QtWidgets.QLabel("0", self)
		self.kghTOlbs_res  = QtWidgets.QLabel("0", self)
		self.kghTOlbh_res  = QtWidgets.QLabel("0", self)
		self.kghTOlbd_res  = QtWidgets.QLabel("0", self)

		self.kgdTOgs_res   = QtWidgets.QLabel("0", self)
		self.kgdTOgmin_res = QtWidgets.QLabel("0", self)
		self.kgdTOkgs_res  = QtWidgets.QLabel("0", self)
		self.kgdTOkgh_res  = QtWidgets.QLabel("0", self)
		self.kgdTOkgd_res  = QtWidgets.QLabel("0", self)
		self.kgdTOtons_res = QtWidgets.QLabel("0", self)
		self.kgdTOtonh_res = QtWidgets.QLabel("0", self)
		self.kgdTOtond_res = QtWidgets.QLabel("0", self)
		self.kgdTOlbs_res  = QtWidgets.QLabel("0", self)
		self.kgdTOlbh_res  = QtWidgets.QLabel("0", self)
		self.kgdTOlbd_res  = QtWidgets.QLabel("0", self)

		self.tonsTOgs_res   = QtWidgets.QLabel("0", self)
		self.tonsTOgmin_res = QtWidgets.QLabel("0", self)
		self.tonsTOkgs_res  = QtWidgets.QLabel("0", self)
		self.tonsTOkgh_res  = QtWidgets.QLabel("0", self)
		self.tonsTOkgd_res  = QtWidgets.QLabel("0", self)
		self.tonsTOtons_res = QtWidgets.QLabel("0", self)
		self.tonsTOtonh_res = QtWidgets.QLabel("0", self)
		self.tonsTOtond_res = QtWidgets.QLabel("0", self)
		self.tonsTOlbs_res  = QtWidgets.QLabel("0", self)
		self.tonsTOlbh_res  = QtWidgets.QLabel("0", self)
		self.tonsTOlbd_res  = QtWidgets.QLabel("0", self)

		self.tonhTOgs_res   = QtWidgets.QLabel("0", self)
		self.tonhTOgmin_res = QtWidgets.QLabel("0", self)
		self.tonhTOkgs_res  = QtWidgets.QLabel("0", self)
		self.tonhTOkgh_res  = QtWidgets.QLabel("0", self)
		self.tonhTOkgd_res  = QtWidgets.QLabel("0", self)
		self.tonhTOtons_res = QtWidgets.QLabel("0", self)
		self.tonhTOtonh_res = QtWidgets.QLabel("0", self)
		self.tonhTOtond_res = QtWidgets.QLabel("0", self)
		self.tonhTOlbs_res  = QtWidgets.QLabel("0", self)
		self.tonhTOlbh_res  = QtWidgets.QLabel("0", self)
		self.tonhTOlbd_res  = QtWidgets.QLabel("0", self)

		self.tondTOgs_res   = QtWidgets.QLabel("0", self)
		self.tondTOgmin_res = QtWidgets.QLabel("0", self)
		self.tondTOkgs_res  = QtWidgets.QLabel("0", self)
		self.tondTOkgh_res  = QtWidgets.QLabel("0", self)
		self.tondTOkgd_res  = QtWidgets.QLabel("0", self)
		self.tondTOtons_res = QtWidgets.QLabel("0", self)
		self.tondTOtonh_res = QtWidgets.QLabel("0", self)
		self.tondTOtond_res = QtWidgets.QLabel("0", self)
		self.tondTOlbs_res  = QtWidgets.QLabel("0", self)
		self.tondTOlbh_res  = QtWidgets.QLabel("0", self)
		self.tondTOlbd_res  = QtWidgets.QLabel("0", self)

		self.lbsTOgs_res   = QtWidgets.QLabel("0", self)
		self.lbsTOgmin_res = QtWidgets.QLabel("0", self)
		self.lbsTOkgs_res  = QtWidgets.QLabel("0", self)
		self.lbsTOkgh_res  = QtWidgets.QLabel("0", self)
		self.lbsTOkgd_res  = QtWidgets.QLabel("0", self)
		self.lbsTOtons_res = QtWidgets.QLabel("0", self)
		self.lbsTOtonh_res = QtWidgets.QLabel("0", self)
		self.lbsTOtond_res = QtWidgets.QLabel("0", self)
		self.lbsTOlbs_res  = QtWidgets.QLabel("0", self)
		self.lbsTOlbh_res  = QtWidgets.QLabel("0", self)
		self.lbsTOlbd_res  = QtWidgets.QLabel("0", self)

		self.lbhTOgs_res   = QtWidgets.QLabel("0", self)
		self.lbhTOgmin_res = QtWidgets.QLabel("0", self)
		self.lbhTOkgs_res  = QtWidgets.QLabel("0", self)
		self.lbhTOkgh_res  = QtWidgets.QLabel("0", self)
		self.lbhTOkgd_res  = QtWidgets.QLabel("0", self)
		self.lbhTOtons_res = QtWidgets.QLabel("0", self)
		self.lbhTOtonh_res = QtWidgets.QLabel("0", self)
		self.lbhTOtond_res = QtWidgets.QLabel("0", self)
		self.lbhTOlbs_res  = QtWidgets.QLabel("0", self)
		self.lbhTOlbh_res  = QtWidgets.QLabel("0", self)
		self.lbhTOlbd_res  = QtWidgets.QLabel("0", self)

		self.lbdTOgs_res   = QtWidgets.QLabel("0", self)
		self.lbdTOgmin_res = QtWidgets.QLabel("0", self)
		self.lbdTOkgs_res  = QtWidgets.QLabel("0", self)
		self.lbdTOkgh_res  = QtWidgets.QLabel("0", self)
		self.lbdTOkgd_res  = QtWidgets.QLabel("0", self)
		self.lbdTOtons_res = QtWidgets.QLabel("0", self)
		self.lbdTOtonh_res = QtWidgets.QLabel("0", self)
		self.lbdTOtond_res = QtWidgets.QLabel("0", self)
		self.lbdTOlbs_res  = QtWidgets.QLabel("0", self)
		self.lbdTOlbh_res  = QtWidgets.QLabel("0", self)
		self.lbdTOlbd_res  = QtWidgets.QLabel("0", self)

		gsTO_Label = [self.gsTOgs_res, self.gsTOgmin_res, self.gsTOkgs_res, self.gsTOkgh_res, self.gsTOkgd_res, self.gsTOtons_res, self.gsTOtonh_res, 
						   self.gsTOtond_res, self.gsTOlbs_res, self.gsTOlbh_res, self.gsTOlbd_res]

		gminTO_Label = [self.gminTOgs_res, self.gminTOgmin_res, self.gminTOkgs_res, self.gminTOkgh_res, self.gminTOkgd_res, self.gminTOtons_res, self.gminTOtonh_res, 
						   self.gminTOtond_res, self.gminTOlbs_res, self.gminTOlbh_res, self.gminTOlbd_res]

		kgsTO_Label = [self.kgsTOgs_res, self.kgsTOgmin_res, self.kgsTOkgs_res, self.kgsTOkgh_res, self.kgsTOkgd_res, self.kgsTOtons_res, self.kgsTOtonh_res, 
						   self.kgsTOtond_res, self.kgsTOlbs_res, self.kgsTOlbh_res, self.kgsTOlbd_res]

		kghTO_Label = [self.kghTOgs_res, self.kghTOgmin_res, self.kghTOkgs_res, self.kghTOkgh_res, self.kghTOkgd_res, self.kghTOtons_res, self.kghTOtonh_res, 
						   self.kghTOtond_res, self.kghTOlbs_res, self.kghTOlbh_res, self.kghTOlbd_res]

		kgdTO_Label = [self.kgdTOgs_res, self.kgdTOgmin_res, self.kgdTOkgs_res, self.kgdTOkgh_res, self.kgdTOkgd_res, self.kgdTOtons_res, self.kgdTOtonh_res, 
						   self.kgdTOtond_res, self.kgdTOlbs_res, self.kgdTOlbh_res, self.kgdTOlbd_res]

		tonsTO_Label = [self.tonsTOgs_res, self.tonsTOgmin_res, self.tonsTOkgs_res, self.tonsTOkgh_res, self.tonsTOkgd_res, self.tonsTOtons_res, self.tonsTOtonh_res, 
						   self.tonsTOtond_res, self.tonsTOlbs_res, self.tonsTOlbh_res, self.tonsTOlbd_res]

		tonhTO_Label = [self.tonhTOgs_res, self.tonhTOgmin_res, self.tonhTOkgs_res, self.tonhTOkgh_res, self.tonhTOkgd_res, self.tonhTOtons_res, self.tonhTOtonh_res, 
						   self.tonhTOtond_res, self.tonhTOlbs_res, self.tonhTOlbh_res, self.tonhTOlbd_res]

		tondTO_Label = [self.tondTOgs_res, self.tondTOgmin_res, self.tondTOkgs_res, self.tondTOkgh_res, self.tondTOkgd_res, self.tondTOtons_res, self.tondTOtonh_res, 
						   self.tondTOtond_res, self.tondTOlbs_res, self.tondTOlbh_res, self.tondTOlbd_res]

		lbsTO_Label = [self.lbsTOgs_res, self.lbsTOgmin_res, self.lbsTOkgs_res, self.lbsTOkgh_res, self.lbsTOkgd_res, self.lbsTOtons_res, self.lbsTOtonh_res, 
						   self.lbsTOtond_res, self.lbsTOlbs_res, self.lbsTOlbh_res, self.lbsTOlbd_res]

		lbhTO_Label = [self.lbhTOgs_res, self.lbhTOgmin_res, self.lbhTOkgs_res, self.lbhTOkgh_res, self.lbhTOkgd_res, self.lbhTOtons_res, self.lbhTOtonh_res, 
						   self.lbhTOtond_res, self.lbhTOlbs_res, self.lbhTOlbh_res, self.lbhTOlbd_res]

		lbdTO_Label = [self.lbdTOgs_res, self.lbdTOgmin_res, self.lbdTOkgs_res, self.lbdTOkgh_res, self.lbdTOkgd_res, self.lbdTOtons_res, self.lbdTOtonh_res, 
						   self.lbdTOtond_res, self.lbdTOlbs_res, self.lbdTOlbh_res, self.lbdTOlbd_res]

		i = 0
		for item in gsTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in gminTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kgsTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kghTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in kgdTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in tonsTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in tonhTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in tondTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in lbsTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in lbhTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
		i = 0
		for item in lbdTO_Label:
			output_grid.addWidget(item, 11, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def gsTO_fun(self):
		try:
			gsTOgs_proc   = float(self.gsi_LinEd.text()) * 1
			gsTOgmin_proc = float(self.gsi_LinEd.text()) * 60
			gsTOkgs_proc  = float(self.gsi_LinEd.text()) * 1e-03
			gsTOkgh_proc  = float(self.gsi_LinEd.text()) * 1e-03 * 3600
			gsTOkgd_proc  = float(self.gsi_LinEd.text()) * 1e-03 * 3600 * 24
			gsTOtons_proc = float(self.gsi_LinEd.text()) * 1e-06
			gsTOtonh_proc = float(self.gsi_LinEd.text()) * 1e-06 * 3600
			gsTOtond_proc = float(self.gsi_LinEd.text()) * 1e-06 * 3600 * 24
			gsTOlbs_proc  = float(self.gsi_LinEd.text()) * 2.2046226217e-03
			gsTOlbh_proc  = float(self.gsi_LinEd.text()) * 2.2046226217e-03 * 3600
			gsTOlbd_proc  = float(self.gsi_LinEd.text()) * 2.2046226217e-03 * 3600 * 24

			self.gsTOgs_res.setText(str(round(gsTOgs_proc,     8)))
			self.gsTOgmin_res.setText(str(round(gsTOgmin_proc, 8)))
			self.gsTOkgs_res.setText(str(round(gsTOkgs_proc,   8)))
			self.gsTOkgh_res.setText(str(round(gsTOkgh_proc,   8)))
			self.gsTOkgd_res.setText(str(round(gsTOkgd_proc,   8)))
			self.gsTOtons_res.setText(str(round(gsTOtons_proc, 8)))
			self.gsTOtonh_res.setText(str(round(gsTOtonh_proc, 8)))
			self.gsTOtond_res.setText(str(round(gsTOtond_proc, 8)))
			self.gsTOlbs_res.setText(str(round(gsTOlbs_proc,   8)))
			self.gsTOlbh_res.setText(str(round(gsTOlbh_proc,   8)))
			self.gsTOlbd_res.setText(str(round(gsTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def gminTO_fun(self):
		try:
			gminTOgs_proc   = float(self.gmini_LinEd.text()) * 1     / 60
			gminTOgmin_proc = float(self.gmini_LinEd.text()) * 1
			gminTOkgs_proc  = float(self.gmini_LinEd.text()) * 1e-03 / 60
			gminTOkgh_proc  = float(self.gmini_LinEd.text()) * 1e-03 * 60
			gminTOkgd_proc  = float(self.gmini_LinEd.text()) * 1e-03 * 60 * 24
			gminTOtons_proc = float(self.gmini_LinEd.text()) * 1e-06 / 60
			gminTOtonh_proc = float(self.gmini_LinEd.text()) * 1e-06 * 60
			gminTOtond_proc = float(self.gmini_LinEd.text()) * 1e-06 * 60 * 24
			gminTOlbs_proc  = float(self.gmini_LinEd.text()) * 2.2046226217e-03 / 60
			gminTOlbh_proc  = float(self.gmini_LinEd.text()) * 2.2046226217e-03 * 60
			gminTOlbd_proc  = float(self.gmini_LinEd.text()) * 2.2046226217e-03 * 60 * 24

			self.gminTOgs_res.setText(str(round(gminTOgs_proc,     8)))
			self.gminTOgmin_res.setText(str(round(gminTOgmin_proc, 8)))
			self.gminTOkgs_res.setText(str(round(gminTOkgs_proc,   8)))
			self.gminTOkgh_res.setText(str(round(gminTOkgh_proc,   8)))
			self.gminTOkgd_res.setText(str(round(gminTOkgd_proc,   8)))
			self.gminTOtons_res.setText(str(round(gminTOtons_proc, 8)))
			self.gminTOtonh_res.setText(str(round(gminTOtonh_proc, 8)))
			self.gminTOtond_res.setText(str(round(gminTOtond_proc, 8)))
			self.gminTOlbs_res.setText(str(round(gminTOlbs_proc,   8)))
			self.gminTOlbh_res.setText(str(round(gminTOlbh_proc,   8)))
			self.gminTOlbd_res.setText(str(round(gminTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def kgsTO_fun(self):
		try:
			kgsTOgs_proc   = float(self.kgsi_LinEd.text()) * 1e+03
			kgsTOgmin_proc = float(self.kgsi_LinEd.text()) * 1e+03 * 60
			kgsTOkgs_proc  = float(self.kgsi_LinEd.text()) * 1
			kgsTOkgh_proc  = float(self.kgsi_LinEd.text()) * 1 * 3600
			kgsTOkgd_proc  = float(self.kgsi_LinEd.text()) * 1 * 3600 * 24
			kgsTOtons_proc = float(self.kgsi_LinEd.text()) * 1e-03
			kgsTOtonh_proc = float(self.kgsi_LinEd.text()) * 1e-03 * 3600
			kgsTOtond_proc = float(self.kgsi_LinEd.text()) * 1e-03 * 3600 * 24
			kgsTOlbs_proc  = float(self.kgsi_LinEd.text()) * 2.2046226217
			kgsTOlbh_proc  = float(self.kgsi_LinEd.text()) * 2.2046226217 * 3600
			kgsTOlbd_proc  = float(self.kgsi_LinEd.text()) * 2.2046226217 * 3600 * 24

			self.kgsTOgs_res.setText(str(round(kgsTOgs_proc,     8)))
			self.kgsTOgmin_res.setText(str(round(kgsTOgmin_proc, 8)))
			self.kgsTOkgs_res.setText(str(round(kgsTOkgs_proc,   8)))
			self.kgsTOkgh_res.setText(str(round(kgsTOkgh_proc,   8)))
			self.kgsTOkgd_res.setText(str(round(kgsTOkgd_proc,   8)))
			self.kgsTOtons_res.setText(str(round(kgsTOtons_proc, 8)))
			self.kgsTOtonh_res.setText(str(round(kgsTOtonh_proc, 8)))
			self.kgsTOtond_res.setText(str(round(kgsTOtond_proc, 8)))
			self.kgsTOlbs_res.setText(str(round(kgsTOlbs_proc,   8)))
			self.kgsTOlbh_res.setText(str(round(kgsTOlbh_proc,   8)))
			self.kgsTOlbd_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def kghTO_fun(self):
		try:
			kghTOgs_proc   = float(self.kghi_LinEd.text()) * 1e+03 / 3600
			kghTOgmin_proc = float(self.kghi_LinEd.text()) * 1e+03 / 60
			kghTOkgs_proc  = float(self.kghi_LinEd.text()) * 1     / 3600
			kghTOkgh_proc  = float(self.kghi_LinEd.text()) * 1
			kghTOkgd_proc  = float(self.kghi_LinEd.text()) * 1     * 24
			kghTOtons_proc = float(self.kghi_LinEd.text()) * 1e-03 / 3600
			kghTOtonh_proc = float(self.kghi_LinEd.text()) * 1e-03
			kghTOtond_proc = float(self.kghi_LinEd.text()) * 1e-03 * 24
			kghTOlbs_proc  = float(self.kghi_LinEd.text()) * 2.2046226217 / 3600
			kghTOlbh_proc  = float(self.kghi_LinEd.text()) * 2.2046226217
			kghTOlbd_proc  = float(self.kghi_LinEd.text()) * 2.2046226217 * 24

			self.kghTOgs_res.setText(str(round(kghTOgs_proc,     8)))
			self.kghTOgmin_res.setText(str(round(kghTOgmin_proc, 8)))
			self.kghTOkgs_res.setText(str(round(kghTOkgs_proc,   8)))
			self.kghTOkgh_res.setText(str(round(kghTOkgh_proc,   8)))
			self.kghTOkgd_res.setText(str(round(kghTOkgd_proc,   8)))
			self.kghTOtons_res.setText(str(round(kghTOtons_proc, 8)))
			self.kghTOtonh_res.setText(str(round(kghTOtonh_proc, 8)))
			self.kghTOtond_res.setText(str(round(kghTOtond_proc, 8)))
			self.kghTOlbs_res.setText(str(round(kghTOlbs_proc,   8)))
			self.kghTOlbh_res.setText(str(round(kghTOlbh_proc,   8)))
			self.kghTOlbd_res.setText(str(round(kghTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def kgdTO_fun(self):
		try:
			kgdTOgs_proc   = float(self.kgdi_LinEd.text()) * 1e+03 / 24 / 3600
			kgdTOgmin_proc = float(self.kgdi_LinEd.text()) * 1e+03 / 24 / 60
			kgdTOkgs_proc  = float(self.kgdi_LinEd.text()) * 1     / 24 / 3600
			kgdTOkgh_proc  = float(self.kgdi_LinEd.text()) * 1     / 24
			kgdTOkgd_proc  = float(self.kgdi_LinEd.text()) * 1
			kgdTOtons_proc = float(self.kgdi_LinEd.text()) * 1e-03 / 24 / 3600
			kgdTOtonh_proc = float(self.kgdi_LinEd.text()) * 1e-03 / 24
			kgdTOtond_proc = float(self.kgdi_LinEd.text()) * 1e-03
			kgdTOlbs_proc  = float(self.kgdi_LinEd.text()) * 2.2046226217 / 24 / 3600
			kgdTOlbh_proc  = float(self.kgdi_LinEd.text()) * 2.2046226217 / 24
			kgdTOlbd_proc  = float(self.kgdi_LinEd.text()) * 2.2046226217

			self.kgdTOgs_res.setText(str(round(kgdTOgs_proc,     8)))
			self.kgdTOgmin_res.setText(str(round(kgdTOgmin_proc, 8)))
			self.kgdTOkgs_res.setText(str(round(kgdTOkgs_proc,   8)))
			self.kgdTOkgh_res.setText(str(round(kgdTOkgh_proc,   8)))
			self.kgdTOkgd_res.setText(str(round(kgdTOkgd_proc,   8)))
			self.kgdTOtons_res.setText(str(round(kgdTOtons_proc, 8)))
			self.kgdTOtonh_res.setText(str(round(kgdTOtonh_proc, 8)))
			self.kgdTOtond_res.setText(str(round(kgdTOtond_proc, 8)))
			self.kgdTOlbs_res.setText(str(round(kgdTOlbs_proc,   8)))
			self.kgdTOlbh_res.setText(str(round(kgdTOlbh_proc,   8)))
			self.kgdTOlbd_res.setText(str(round(kgdTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def tonsTO_fun(self):
		try:
			tonsTOgs_proc   = float(self.tonsi_LinEd.text()) * 1e+06
			tonsTOgmin_proc = float(self.tonsi_LinEd.text()) * 1e+06 * 60
			tonsTOkgs_proc  = float(self.tonsi_LinEd.text()) * 1e+03
			tonsTOkgh_proc  = float(self.tonsi_LinEd.text()) * 1e+03 * 3600
			tonsTOkgd_proc  = float(self.tonsi_LinEd.text()) * 1e+03 * 3600 * 24
			tonsTOtons_proc = float(self.tonsi_LinEd.text()) * 1
			tonsTOtonh_proc = float(self.tonsi_LinEd.text()) * 1 * 3600
			tonsTOtond_proc = float(self.tonsi_LinEd.text()) * 1 * 3600 * 24
			tonsTOlbs_proc  = float(self.tonsi_LinEd.text()) * 2.2046226217e+03
			tonsTOlbh_proc  = float(self.tonsi_LinEd.text()) * 2.2046226217e+03 * 3600
			tonsTOlbd_proc  = float(self.tonsi_LinEd.text()) * 2.2046226217e+03 * 3600 * 24

			self.tonsTOgs_res.setText("-")
			self.tonsTOgmin_res.setText("-")
			self.tonsTOkgs_res.setText(str(round(tonsTOkgs_proc,   8)))
			self.tonsTOkgh_res.setText("-")
			self.tonsTOkgd_res.setText("-")
			self.tonsTOtons_res.setText(str(round(tonsTOtons_proc, 8)))
			self.tonsTOtonh_res.setText(str(round(tonsTOtonh_proc, 8)))
			self.tonsTOtond_res.setText(str(round(tonsTOtond_proc, 8)))
			self.tonsTOlbs_res.setText(str(round(tonsTOlbs_proc,   8)))
			self.tonsTOlbh_res.setText("-")
			self.tonsTOlbd_res.setText("-")
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def tonhTO_fun(self):
		try:
			tonhTOgs_proc   = float(self.tonhi_LinEd.text()) * 1e+06 / 3600
			tonhTOgmin_proc = float(self.tonhi_LinEd.text()) * 1e+06 / 60
			tonhTOkgs_proc  = float(self.tonhi_LinEd.text()) * 1e+03 / 3600
			tonhTOkgh_proc  = float(self.tonhi_LinEd.text()) * 1e+03
			tonhTOkgd_proc  = float(self.tonhi_LinEd.text()) * 1e+03 * 24
			tonhTOtons_proc = float(self.tonhi_LinEd.text()) * 1 / 3600
			tonhTOtonh_proc = float(self.tonhi_LinEd.text()) * 1
			tonhTOtond_proc = float(self.tonhi_LinEd.text()) * 1 * 24
			tonhTOlbs_proc  = float(self.tonhi_LinEd.text()) * 2.2046226217e+03 / 3600
			tonhTOlbh_proc  = float(self.tonhi_LinEd.text()) * 2.2046226217e+03
			tonhTOlbd_proc  = float(self.tonhi_LinEd.text()) * 2.2046226217e+03 * 24

			self.tonhTOgs_res.setText(str(round(tonhTOgs_proc,     8)))
			self.tonhTOgmin_res.setText(str(round(tonhTOgmin_proc, 8)))
			self.tonhTOkgs_res.setText(str(round(tonhTOkgs_proc,   8)))
			self.tonhTOkgh_res.setText(str(round(tonhTOkgh_proc,   8)))
			self.tonhTOkgd_res.setText(str(round(tonhTOkgd_proc,   8)))
			self.tonhTOtons_res.setText(str(round(tonhTOtons_proc, 8)))
			self.tonhTOtonh_res.setText(str(round(tonhTOtonh_proc, 8)))
			self.tonhTOtond_res.setText(str(round(tonhTOtond_proc, 8)))
			self.tonhTOlbs_res.setText(str(round(tonhTOlbs_proc,   8)))
			self.tonhTOlbh_res.setText(str(round(tonhTOlbh_proc,   8)))
			self.tonhTOlbd_res.setText(str(round(tonhTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def tondTO_fun(self):
		try:
			tondTOgs_proc   = float(self.tondi_LinEd.text()) * 1e+06 / 24 / 3600
			tondTOgmin_proc = float(self.tondi_LinEd.text()) * 1e+06 / 24 / 60
			tondTOkgs_proc  = float(self.tondi_LinEd.text()) * 1e+03 / 24 / 3600
			tondTOkgh_proc  = float(self.tondi_LinEd.text()) * 1e+03 / 24
			tondTOkgd_proc  = float(self.tondi_LinEd.text()) * 1e+03
			tondTOtons_proc = float(self.tondi_LinEd.text()) * 1 / 24 / 2600
			tondTOtonh_proc = float(self.tondi_LinEd.text()) * 1 / 24
			tondTOtond_proc = float(self.tondi_LinEd.text()) * 1
			tondTOlbs_proc  = float(self.tondi_LinEd.text()) * 2.2046226217e+03 / 24 / 3600
			tondTOlbh_proc  = float(self.tondi_LinEd.text()) * 2.2046226217e+03 / 24
			tondTOlbd_proc  = float(self.tondi_LinEd.text()) * 2.2046226217e+03

			self.tondTOgs_res.setText(str(round(tondTOgs_proc,     8)))
			self.tondTOgmin_res.setText(str(round(tondTOgmin_proc, 8)))
			self.tondTOkgs_res.setText(str(round(tondTOkgs_proc,   8)))
			self.tondTOkgh_res.setText(str(round(tondTOkgh_proc,   8)))
			self.tondTOkgd_res.setText(str(round(tondTOkgd_proc,   8)))
			self.tondTOtons_res.setText(str(round(tondTOtons_proc, 8)))
			self.tondTOtonh_res.setText(str(round(tondTOtonh_proc, 8)))
			self.tondTOtond_res.setText(str(round(tondTOtond_proc, 8)))
			self.tondTOlbs_res.setText(str(round(tondTOlbs_proc,   8)))
			self.tondTOlbh_res.setText(str(round(tondTOlbh_proc,   8)))
			self.tondTOlbd_res.setText(str(round(tondTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def lbsTO_fun(self):
		try:
			lbsTOgs_proc   = float(self.lbsi_LinEd.text()) * 453.59237002
			lbsTOgmin_proc = float(self.lbsi_LinEd.text()) * 453.59237002 * 60
			lbsTOkgs_proc  = float(self.lbsi_LinEd.text()) * 453.59237002e-03
			lbsTOkgh_proc  = float(self.lbsi_LinEd.text()) * 453.59237002e-03 * 3600
			lbsTOkgd_proc  = float(self.lbsi_LinEd.text()) * 453.59237002e-03 * 3600 * 24
			lbsTOtons_proc = float(self.lbsi_LinEd.text()) * 453.59237002e-06
			lbsTOtonh_proc = float(self.lbsi_LinEd.text()) * 453.59237002e-06 * 3600
			lbsTOtond_proc = float(self.lbsi_LinEd.text()) * 453.59237002e-06 * 3600 * 24
			lbsTOlbs_proc  = float(self.lbsi_LinEd.text()) * 1
			lbsTOlbh_proc  = float(self.lbsi_LinEd.text()) * 1 * 3600
			lbsTOlbd_proc  = float(self.lbsi_LinEd.text()) * 1 * 3600 * 24

			self.lbsTOgs_res.setText(str(round(lbsTOgs_proc,     8)))
			self.lbsTOgmin_res.setText(str(round(lbsTOgmin_proc, 8)))
			self.lbsTOkgs_res.setText(str(round(lbsTOkgs_proc,   8)))
			self.lbsTOkgh_res.setText(str(round(lbsTOkgh_proc,   8)))
			self.lbsTOkgd_res.setText(str(round(lbsTOkgd_proc,   8)))
			self.lbsTOtons_res.setText(str(round(lbsTOtons_proc, 8)))
			self.lbsTOtonh_res.setText(str(round(lbsTOtonh_proc, 8)))
			self.lbsTOtond_res.setText(str(round(lbsTOtond_proc, 8)))
			self.lbsTOlbs_res.setText(str(round(lbsTOlbs_proc,   8)))
			self.lbsTOlbh_res.setText(str(round(lbsTOlbh_proc,   8)))
			self.lbsTOlbd_res.setText(str(round(lbsTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def lbhTO_fun(self):
		try:
			lbhTOgs_proc   = float(self.lbhi_LinEd.text()) * 453.59237002 / 3600
			lbhTOgmin_proc = float(self.lbhi_LinEd.text()) * 453.59237002 / 60
			lbhTOkgs_proc  = float(self.lbhi_LinEd.text()) * 453.59237002e-03 / 3600
			lbhTOkgh_proc  = float(self.lbhi_LinEd.text()) * 453.59237002e-03
			lbhTOkgd_proc  = float(self.lbhi_LinEd.text()) * 453.59237002e-03 * 24
			lbhTOtons_proc = float(self.lbhi_LinEd.text()) * 453.59237002e-06 / 3600
			lbhTOtonh_proc = float(self.lbhi_LinEd.text()) * 453.59237002e-06
			lbhTOtond_proc = float(self.lbhi_LinEd.text()) * 453.59237002e-06 * 24
			lbhTOlbs_proc  = float(self.lbhi_LinEd.text()) / 3600
			lbhTOlbh_proc  = float(self.lbhi_LinEd.text()) * 1
			lbhTOlbd_proc  = float(self.lbhi_LinEd.text()) * 24

			self.lbhTOgs_res.setText(str(round(lbhTOgs_proc,     8)))
			self.lbhTOgmin_res.setText(str(round(lbhTOgmin_proc, 8)))
			self.lbhTOkgs_res.setText(str(round(lbhTOkgs_proc,   8)))
			self.lbhTOkgh_res.setText(str(round(lbhTOkgh_proc,   8)))
			self.lbhTOkgd_res.setText(str(round(lbhTOkgd_proc,   8)))
			self.lbhTOtons_res.setText(str(round(lbhTOtons_proc, 8)))
			self.lbhTOtonh_res.setText(str(round(lbhTOtonh_proc, 8)))
			self.lbhTOtond_res.setText(str(round(lbhTOtond_proc, 8)))
			self.lbhTOlbs_res.setText(str(round(lbhTOlbs_proc,   8)))
			self.lbhTOlbh_res.setText(str(round(lbhTOlbh_proc,   8)))
			self.lbhTOlbd_res.setText(str(round(lbhTOlbd_proc,   8)))
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()



	def lbdTO_fun(self):
		try:
			lbdTOgs_proc   = float(self.lbdi_LinEd.text()) * 453.59237002     / 24 / 3600
			lbdTOgmin_proc = float(self.lbdi_LinEd.text()) * 453.59237002     / 24 / 60
			lbdTOkgs_proc  = float(self.lbdi_LinEd.text()) * 453.59237002e-03 / 24 / 3600
			lbdTOkgh_proc  = float(self.lbdi_LinEd.text()) * 453.59237002e-03 / 24
			lbdTOkgd_proc  = float(self.lbdi_LinEd.text()) * 453.59237002e-03
			lbdTOtons_proc = float(self.lbdi_LinEd.text()) * 453.59237002e-06 / 24 / 3600
			lbdTOtonh_proc = float(self.lbdi_LinEd.text()) * 453.59237002e-06 / 24
			lbdTOtond_proc = float(self.lbdi_LinEd.text()) * 453.59237002e-06
			lbdTOlbs_proc  = float(self.lbdi_LinEd.text()) / 24 / 3600
			lbdTOlbh_proc  = float(self.lbdi_LinEd.text()) * 24
			lbdTOlbd_proc  = float(self.lbdi_LinEd.text()) * 1

			self.lbdTOgs_res.setText("-")
			self.lbdTOgmin_res.setText("-")
			self.lbdTOkgs_res.setText(str(round(lbdTOkgs_proc,   8)))
			self.lbdTOkgh_res.setText(str(round(lbdTOkgh_proc,   8)))
			self.lbdTOkgd_res.setText(str(round(lbdTOkgd_proc,   8)))
			self.lbdTOtons_res.setText(str(round(lbdTOtons_proc, 8)))
			self.lbdTOtonh_res.setText(str(round(lbdTOtonh_proc, 8)))
			self.lbdTOtond_res.setText(str(round(lbdTOtond_proc, 8)))
			self.lbdTOlbs_res.setText(str(round(lbdTOlbs_proc,   8)))
			self.lbdTOlbh_res.setText(str(round(lbdTOlbh_proc,   8)))
			self.lbdTOlbd_res.setText(str(round(lbdTOlbd_proc,   8)))
		
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
	