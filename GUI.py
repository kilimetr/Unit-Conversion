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
		self.heatval_pb     = QtWidgets.QPushButton("Heat Volumetric Flow Rate",         self)
		self.dens_pb        = QtWidgets.QPushButton("Density",                           self)
		self.heatfldens_pb  = QtWidgets.QPushButton("Density of Heat Flow Rate",         self)
		self.specdens_pb    = QtWidgets.QPushButton("Specific Density & API Conversion", self)
		self.energy_pb      = QtWidgets.QPushButton("Energy",                            self)
		self.force_pb       = QtWidgets.QPushButton("Force",                             self)
		self.heatcond_pb    = QtWidgets.QPushButton("Heat Conductivity",                 self)
		self.heatres_pb     = QtWidgets.QPushButton("Heat Resistance",                   self)
		self.heattrans_pb   = QtWidgets.QPushButton("Heat Transfer",                     self)
		self.length_pb      = QtWidgets.QPushButton("Length",                            self)
		self.magind_pb      = QtWidgets.QPushButton("Magnetic Induction",                self)
		self.magint_pb      = QtWidgets.QPushButton("Magnetic Intensity",                self)
		self.mass_pb        = QtWidgets.QPushButton("Mass",                              self)
		self.massflow_pb    = QtWidgets.QPushButton("Mass Flow Rate",                    self)

		vbox1 = QtWidgets.QVBoxLayout()
		vbox1.addWidget(self.area_pb)
		vbox1.addWidget(self.heatval_pb)
		vbox1.addWidget(self.dens_pb)
		vbox1.addWidget(self.heatfldens_pb)
		vbox1.addWidget(self.specdens_pb)
		vbox1.addWidget(self.energy_pb)
		vbox1.addWidget(self.force_pb)
		vbox1.addWidget(self.heatcond_pb)
		vbox1.addWidget(self.heatres_pb)
		vbox1.addWidget(self.heattrans_pb)
		vbox1.addWidget(self.length_pb)
		vbox1.addWidget(self.magind_pb)
		vbox1.addWidget(self.magint_pb)
		vbox1.addWidget(self.mass_pb)
		vbox1.addWidget(self.massflow_pb)
		vbox1.addStretch()
		groupBox_1.setLayout(vbox1)

		self.area_pb.clicked.connect(self.area_win)
		self.heatval_pb.clicked.connect(self.heatval_win)
		self.dens_pb.clicked.connect(self.dens_win)
		self.heatfldens_pb.clicked.connect(self.heatfldens_win)
		self.specdens_pb.clicked.connect(self.specdens_win)
		self.energy_pb.clicked.connect(self.energy_win)
		self.force_pb.clicked.connect(self.force_win)
		self.heatcond_pb.clicked.connect(self.heatcond_win)
		self.heatres_pb.clicked.connect(self.heatres_win)
		self.heattrans_pb.clicked.connect(self.heattrans_win)
		self.length_pb.clicked.connect(self.length_win)
		self.magind_pb.clicked.connect(self.magind_win)
		self.magint_pb.clicked.connect(self.magint_win)
		self.mass_pb.clicked.connect(self.mass_win)
		self.massflow_pb.clicked.connect(self.massflow_win)


		return groupBox_1

	def createGroup_2(self):
		groupBox_2 = QtWidgets.QGroupBox()

		self.massfrac_pb    = QtWidgets.QPushButton("Mass Fraction",                     self)
		self.powheatfl_pb   = QtWidgets.QPushButton("Power & Heat Flow Rate",            self)
		self.pressstres_pb  = QtWidgets.QPushButton("Pressure & Stress",                 self)
		self.pressabsg_pb   = QtWidgets.QPushButton("Pressure Conversion abs-gauge",     self)
		self.pressdrl_pb    = QtWidgets.QPushButton("Pressure Drop per Length",          self)
		self.specener_pb    = QtWidgets.QPushButton("Specific Energy",                   self)
		self.specheatcap_pb = QtWidgets.QPushButton("Specific Heat Capacity",            self)
		self.surftens_pb    = QtWidgets.QPushButton("Surface Tension",                   self)
		self.temp_pb        = QtWidgets.QPushButton("Temperature",                       self)
		self.dynvis_pb      = QtWidgets.QPushButton("Dynamic Viscosity",                 self)
		self.kinvis_pb      = QtWidgets.QPushButton("Kinematic Viscosity",               self)
		self.veloc_pb       = QtWidgets.QPushButton("Velocity",                          self)
		self.vol_pb         = QtWidgets.QPushButton("Volume",                            self)
		self.volflow_pb     = QtWidgets.QPushButton("Volumetric Flow Rate",              self)
		self.weight_pb      = QtWidgets.QPushButton("Weight",                            self)

		vbox2 = QtWidgets.QVBoxLayout()
		vbox2.addWidget(self.massfrac_pb)
		vbox2.addWidget(self.powheatfl_pb)
		vbox2.addWidget(self.pressstres_pb)
		vbox2.addWidget(self.pressabsg_pb)
		vbox2.addWidget(self.pressdrl_pb)
		vbox2.addWidget(self.specener_pb)
		vbox2.addWidget(self.specheatcap_pb)
		vbox2.addWidget(self.surftens_pb)
		vbox2.addWidget(self.temp_pb)
		vbox2.addWidget(self.dynvis_pb)
		vbox2.addWidget(self.kinvis_pb)
		vbox2.addWidget(self.veloc_pb)
		vbox2.addWidget(self.vol_pb)
		vbox2.addWidget(self.volflow_pb)
		vbox2.addWidget(self.weight_pb)
		vbox2.addStretch()
		groupBox_2.setLayout(vbox2)

		self.massfrac_pb.clicked.connect(self.massfrac_win)
		self.powheatfl_pb.clicked.connect(self.powheatfl_win)
		self.pressstres_pb.clicked.connect(self.pressstres_win)
		self.pressabsg_pb.clicked.connect(self.pressabsg_win)
		self.pressdrl_pb.clicked.connect(self.pressdrl_win)
		self.specener_pb.clicked.connect(self.specener_win)
		self.specheatcap_pb.clicked.connect(self.specheatcap_win)
		self.surftens_pb.clicked.connect(self.surftens_win)
		self.temp_pb.clicked.connect(self.temp_win)
		self.dynvis_pb.clicked.connect(self.dynvis_win)
		self.kinvis_pb.clicked.connect(self.kinvis_win)
		self.veloc_pb.clicked.connect(self.veloc_win)
		self.vol_pb.clicked.connect(self.vol_win)
		self.volflow_pb.clicked.connect(self.volflow_win)
		self.weight_pb.clicked.connect(self.weight_win)

		return groupBox_2

	def main_window(self):
		grid1 = QtWidgets.QGridLayout()
		grid1.addWidget(self.createGroup_1(), 0, 0)
		grid1.addWidget(self.createGroup_2(), 0, 1)
		self.setLayout(grid1)
		self.show()

	def area_win(self):
		self.area_win2 = Area_Win()
		self.area_win2.show()

	def heatval_win(self):
		self.heatval_win2 = Heatval_Win()
		self.heatval_win2.show()

	def dens_win(self):
		self.dens_win2 = Dens_Win()
		self.dens_win2.show()

	def heatfldens_win(self):
		self.heatfldens_win2 = Heatfldens_Win()
		self.heatfldens_win2.show()

	def specdens_win(self):
		self.specdens_win2 = Specdens_Win()
		self.specdens_win2.show()

	def energy_win(self):
		self.energy_win2 = Energy_Win()
		self.energy_win2.show()

	def force_win(self):
		self.force_win2 = Force_Win()
		self.force_win2.show()

	def heatcond_win(self):
		self.heatcond_win2 = Heatcond_Win()
		self.heatcond_win2.show()

	def heatres_win(self):
		self.heatres_win2 = Heatres_Win()
		self.heatres_win2.show()

	def heattrans_win(self):
		self.heattrans_win2 = Heattrans_Win()
		self.heattrans_win2.show()

	def length_win(self):
		self.length_win2 = Length_Win()
		self.length_win2.show()

	def magind_win(self):
		self.magind_win2 = Magind_Win()
		self.magind_win2.show()

	def magint_win(self):
		self.magint_win2 = Magint_Win()
		self.magint_win2.show()

	def mass_win(self):
		self.mass_win2 = Mass_Win()
		self.mass_win2.show()

	def massflow_win(self):
		self.massflow_win2 = Massflow_Win()
		self.massflow_win2.show()

	def massfrac_win(self):
		self.massfrac_win2 = Massfrac_Win()
		self.massfrac_win2.show()

	def powheatfl_win(self):
		self.powheatfl_win2 = Powheatfl_Win()
		self.powheatfl_win2.show()

	def pressstres_win(self):
		self.pressstres_win2 = Pressstres_Win()
		self.pressstres_win2.show()

	def pressabsg_win(self):
		self.pressabsg_win2 = Pressabsg_Win()
		self.pressabsg_win2.show()

	def pressdrl_win(self):
		self.pressdrl_win2 = Pressdrl_Win()
		self.pressdrl_win2.show()

	def specener_win(self):
		self.specener_win2 = Specener_Win()
		self.specener_win2.show()

	def specheatcap_win(self):
		self.specheatcap_win2 = Specheatcap_Win()
		self.specheatcap_win2.show()

	def surftens_win(self):
		self.surftens_win2 = Surftens_Win()
		self.surftens_win2.show()

	def temp_win(self):
		self.temp_win2 = Temp_Win()
		self.temp_win2.show()

	def dynvis_win(self):
		self.dynvis_win2 = Dynvis_Win()
		self.dynvis_win2.show()

	def kinvis_win(self):
		self.kinvis_win2 = Kinvis_Win()
		self.kinvis_win2.show()

	def veloc_win(self):
		self.veloc_win2 = Veloc_Win()
		self.veloc_win2.show()

	def vol_win(self):
		self.vol_win2 = Vol_Win()
		self.vol_win2.show()

	def volflow_win(self):
		self.volflow_win2 = Volflow_Win()
		self.volflow_win2.show()

	def weight_win(self):
		self.weight_win2 = Weight_Win()
		self.weight_win2.show()



class Area_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Area Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
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
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

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

		self.m2TO_Label = [self.m2TOm2_res, self.m2TOcm2_res, self.m2TOmm2_res, self.m2TOa_res, self.m2TOha_res, self.m2TOin2_res, self.m2TOft2_res, self.m2TOyd2_res,
					  self.m2TOacr_res, self.m2TOmi2ST_res]
		i = 0
		for item in self.m2TO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		cm2TO_Label = [self.cm2TOm2_res, self.cm2TOcm2_res, self.cm2TOmm2_res, self.cm2TOa_res, self.cm2TOha_res, self.cm2TOin2_res, self.cm2TOft2_res, self.cm2TOyd2_res,
					   self.cm2TOacr_res, self.cm2TOmi2ST_res]
		i = 0
		for item in cm2TO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		mm2TO_Label = [self.mm2TOm2_res, self.mm2TOcm2_res, self.mm2TOmm2_res, self.mm2TOa_res, self.mm2TOha_res, self.mm2TOin2_res, self.mm2TOft2_res, self.mm2TOyd2_res,
					   self.mm2TOacr_res, self.mm2TOmi2ST_res]
		i = 0
		for item in mm2TO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		aTO_Label = [self.aTOm2_res, self.aTOcm2_res, self.aTOmm2_res, self.aTOa_res, self.aTOha_res, self.aTOin2_res, self.aTOft2_res, self.aTOyd2_res,
					   self.aTOacr_res, self.aTOmi2ST_res]
		i = 0
		for item in aTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		haTO_Label = [self.haTOm2_res, self.haTOcm2_res, self.haTOmm2_res, self.haTOa_res, self.haTOha_res, self.haTOin2_res, self.haTOft2_res, self.haTOyd2_res,
					  self.haTOacr_res, self.haTOmi2ST_res]
		i = 0
		for item in haTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		in2TO_Label = [self.in2TOm2_res, self.in2TOcm2_res, self.in2TOmm2_res, self.in2TOa_res, self.in2TOha_res, self.in2TOin2_res, self.in2TOft2_res, self.in2TOyd2_res,
					   self.in2TOacr_res, self.in2TOmi2ST_res]
		i = 0
		for item in in2TO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		ft2TO_Label = [self.ft2TOm2_res, self.ft2TOcm2_res, self.ft2TOmm2_res, self.ft2TOa_res, self.ft2TOha_res, self.ft2TOin2_res, self.ft2TOft2_res, self.ft2TOyd2_res,
					   self.ft2TOacr_res, self.ft2TOmi2ST_res]
		i = 0
		for item in ft2TO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		yd2TO_Label = [self.yd2TOm2_res, self.yd2TOcm2_res, self.yd2TOmm2_res, self.yd2TOa_res, self.yd2TOha_res, self.yd2TOin2_res, self.yd2TOft2_res, self.yd2TOyd2_res,
					   self.yd2TOacr_res, self.yd2TOmi2ST_res]
		i = 0
		for item in yd2TO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		acrTO_Label = [self.acrTOm2_res, self.acrTOcm2_res, self.acrTOmm2_res, self.acrTOa_res, self.acrTOha_res, self.acrTOin2_res, self.acrTOft2_res, self.acrTOyd2_res,
					   self.acrTOacr_res, self.acrTOmi2ST_res]
		i = 0
		for item in acrTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		mi2STTO_Label = [self.mi2STTOm2_res, self.mi2STTOcm2_res, self.mi2STTOmm2_res, self.mi2STTOa_res, self.mi2STTOha_res, self.mi2STTOin2_res, self.mi2STTOft2_res, 
						 self.mi2STTOyd2_res, self.mi2STTOacr_res, self.mi2STTOmi2ST_res]
		i = 0
		for item in mi2STTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1


		output_group.setLayout(output_grid)

		return output_group

	def m2TO_fun(self):
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

		# for item in self.m2TO_Label:
		# 	item.setText(str(m2TOm2_proc))
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

	def cm2TO_fun(self):
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

	def mm2TO_fun(self):
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

	def aTO_fun(self):
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

	def haTO_fun(self):
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

	def in2TO_fun(self):
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

	def ft2TO_fun(self):
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

	def yd2TO_fun(self):
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

	def acrTO_fun(self):
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

	def mi2STTO_fun(self):
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

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		# if self.createGroup_input() == QtWidgets.QLabel():
			# pass

		# self.widget = widget("", *args, **kw)
		# if widget == QtWidgets.QLabel():
			# self.widget.setTextInteractionFlags(Qt.TextSelectableByMouse)

		self.setLayout(main_layout)
		self.show()
	


class Heatval_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heat Volumetric Flow Rate Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
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
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

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

		self.BTUft3TO_Label = [self.BTUft3TOBTUft3_res, self.BTUft3TOBTUgalUK_res, self.BTUft3TOBTUgalUS_res, self.BTUft3TOkJm3_res, self.BTUft3TOkWhm3_res, 
							   self.BTUft3TOMJm3_kJdm3_res]
		i = 0
		for item in self.BTUft3TO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		self.BTUgalUKTO_Label = [self.BTUgalUKTOBTUft3_res, self.BTUgalUKTOBTUgalUK_res, self.BTUgalUKTOBTUgalUS_res, self.BTUgalUKTOkJm3_res, self.BTUgalUKTOkWhm3_res, 
							   self.BTUgalUKTOMJm3_kJdm3_res]
		i = 0
		for item in self.BTUgalUKTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		self.BTUgalUSTO_Label = [self.BTUgalUSTOBTUft3_res, self.BTUgalUSTOBTUgalUK_res, self.BTUgalUSTOBTUgalUS_res, self.BTUgalUSTOkJm3_res, self.BTUgalUSTOkWhm3_res, 
							   self.BTUgalUSTOMJm3_kJdm3_res]
		i = 0
		for item in self.BTUgalUSTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		self.kJm3TO_Label = [self.kJm3TOBTUft3_res, self.kJm3TOBTUgalUK_res, self.kJm3TOBTUgalUS_res, self.kJm3TOkJm3_res, self.kJm3TOkWhm3_res, 
							  self.kJm3TOMJm3_kJdm3_res]
		i = 0
		for item in self.kJm3TO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1


		self.kWhm3TO_Label = [self.kWhm3TOBTUft3_res, self.kWhm3TOBTUgalUK_res, self.kWhm3TOBTUgalUS_res, self.kWhm3TOkJm3_res, self.kWhm3TOkWhm3_res, 
							   self.kWhm3TOMJm3_kJdm3_res]
		i = 0
		for item in self.kWhm3TO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		self.MJm3_kJdm3TO_Label = [self.MJm3_kJdm3TOBTUft3_res, self.MJm3_kJdm3TOBTUgalUK_res, self.MJm3_kJdm3TOBTUgalUS_res, self.MJm3_kJdm3TOkJm3_res, 
								   self.MJm3_kJdm3TOkWhm3_res, self.MJm3_kJdm3TOMJm3_kJdm3_res]
		i = 0
		for item in self.MJm3_kJdm3TO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def BTUft3TO_fun(self):
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

	def BTUgalUKTO_fun(self):
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

	def BTUgalUSTO_fun(self):
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

	def kJm3TO_fun(self):
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

	def kWhm3TO_fun(self):
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

	def MJm3_kJdm3TO_fun(self):
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

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()


class Dens_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Dens_Win")



class Heatfldens_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatfldens_Win")



class Specdens_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Specdens_Win")



class Energy_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Energy Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel          = QtWidgets.QLabel()
		self.Ji_LinEd       = QtWidgets.QLineEdit()
		self.kJi_LinEd      = QtWidgets.QLineEdit()
		self.kWhi_LinEd     = QtWidgets.QLineEdit()
		self.BTUITi_LinEd   = QtWidgets.QLineEdit()
		self.BTUmeani_LinEd = QtWidgets.QLineEdit()
		self.calITi_LinEd   = QtWidgets.QLineEdit()
		self.calTHi_LinEd   = QtWidgets.QLineEdit()
		self.hphri_LinEd    = QtWidgets.QLineEdit()
		self.ftlbfi_LinEd   = QtWidgets.QLineEdit()
		self.ftpdli_LinEd   = QtWidgets.QLineEdit()

		Label_list = [blanklabel, "J", "kJ", "kWh", "BTU<sub>internat</sub>", "BTU<sub>mean</sub>", "cal<sub>internat</sub>", "cal<sub>thermal</sub>", "hp-hr", 
					  "ft-lbf", "ft-pdl"]

		LinEd_list = [self.Ji_LinEd, self.kJi_LinEd, self.kWhi_LinEd, self.BTUITi_LinEd, self.BTUmeani_LinEd, self.calITi_LinEd, self.calTHi_LinEd, self.hphri_LinEd,
					  self.ftlbfi_LinEd, self.ftpdli_LinEd]

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

		self.Ji_LinEd.returnPressed.connect(self.JTO_fun)
		self.kJi_LinEd.returnPressed.connect(self.kJTO_fun)
		self.kWhi_LinEd.returnPressed.connect(self.kWhTO_fun)
		self.BTUITi_LinEd.returnPressed.connect(self.BTUITTO_fun)
		self.BTUmeani_LinEd.returnPressed.connect(self.BTUmeanTO_fun)
		self.calITi_LinEd.returnPressed.connect(self.calITTO_fun)
		self.calTHi_LinEd.returnPressed.connect(self.calTHTO_fun)
		self.hphri_LinEd.returnPressed.connect(self.hphrTO_fun)
		self.ftlbfi_LinEd.returnPressed.connect(self.ftlbfTO_fun)
		self.ftpdli_LinEd.returnPressed.connect(self.ftpdlTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["J", "kJ", "kWh", "BTU<sub>internat</sub>", "BTU<sub>mean</sub>", "cal<sub>internat</sub>", "cal<sub>thermal</sub>", "hp-hr", "ft-lbf", "ft-pdl"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.JTOJ_res       = QtWidgets.QLabel("0", self)
		self.JTOkJ_res      = QtWidgets.QLabel("0", self)
		self.JTOkWh_res     = QtWidgets.QLabel("0", self)
		self.JTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.JTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.JTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.JTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.JTOhphr_res    = QtWidgets.QLabel("0", self)
		self.JTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.JTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.kJTOJ_res       = QtWidgets.QLabel("0", self)
		self.kJTOkJ_res      = QtWidgets.QLabel("0", self)
		self.kJTOkWh_res     = QtWidgets.QLabel("0", self)
		self.kJTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.kJTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.kJTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.kJTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.kJTOhphr_res    = QtWidgets.QLabel("0", self)
		self.kJTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.kJTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.kWhTOJ_res       = QtWidgets.QLabel("0", self)
		self.kWhTOkJ_res      = QtWidgets.QLabel("0", self)
		self.kWhTOkWh_res     = QtWidgets.QLabel("0", self)
		self.kWhTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.kWhTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.kWhTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.kWhTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.kWhTOhphr_res    = QtWidgets.QLabel("0", self)
		self.kWhTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.kWhTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.BTUITTOJ_res       = QtWidgets.QLabel("0", self)
		self.BTUITTOkJ_res      = QtWidgets.QLabel("0", self)
		self.BTUITTOkWh_res     = QtWidgets.QLabel("0", self)
		self.BTUITTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.BTUITTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.BTUITTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.BTUITTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.BTUITTOhphr_res    = QtWidgets.QLabel("0", self)
		self.BTUITTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.BTUITTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.BTUmeanTOJ_res       = QtWidgets.QLabel("0", self)
		self.BTUmeanTOkJ_res      = QtWidgets.QLabel("0", self)
		self.BTUmeanTOkWh_res     = QtWidgets.QLabel("0", self)
		self.BTUmeanTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.BTUmeanTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.BTUmeanTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.BTUmeanTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.BTUmeanTOhphr_res    = QtWidgets.QLabel("0", self)
		self.BTUmeanTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.BTUmeanTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.calITTOJ_res       = QtWidgets.QLabel("0", self)
		self.calITTOkJ_res      = QtWidgets.QLabel("0", self)
		self.calITTOkWh_res     = QtWidgets.QLabel("0", self)
		self.calITTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.calITTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.calITTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.calITTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.calITTOhphr_res    = QtWidgets.QLabel("0", self)
		self.calITTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.calITTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.calTHTOJ_res       = QtWidgets.QLabel("0", self)
		self.calTHTOkJ_res      = QtWidgets.QLabel("0", self)
		self.calTHTOkWh_res     = QtWidgets.QLabel("0", self)
		self.calTHTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.calTHTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.calTHTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.calTHTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.calTHTOhphr_res    = QtWidgets.QLabel("0", self)
		self.calTHTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.calTHTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.hphrTOJ_res       = QtWidgets.QLabel("0", self)
		self.hphrTOkJ_res      = QtWidgets.QLabel("0", self)
		self.hphrTOkWh_res     = QtWidgets.QLabel("0", self)
		self.hphrTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.hphrTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.hphrTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.hphrTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.hphrTOhphr_res    = QtWidgets.QLabel("0", self)
		self.hphrTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.hphrTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.ftlbfTOJ_res       = QtWidgets.QLabel("0", self)
		self.ftlbfTOkJ_res      = QtWidgets.QLabel("0", self)
		self.ftlbfTOkWh_res     = QtWidgets.QLabel("0", self)
		self.ftlbfTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.ftlbfTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.ftlbfTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.ftlbfTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.ftlbfTOhphr_res    = QtWidgets.QLabel("0", self)
		self.ftlbfTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.ftlbfTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.ftpdlTOJ_res       = QtWidgets.QLabel("0", self)
		self.ftpdlTOkJ_res      = QtWidgets.QLabel("0", self)
		self.ftpdlTOkWh_res     = QtWidgets.QLabel("0", self)
		self.ftpdlTOBTUIT_res   = QtWidgets.QLabel("0", self)
		self.ftpdlTOBTUmean_res = QtWidgets.QLabel("0", self)
		self.ftpdlTOcalIT_res   = QtWidgets.QLabel("0", self)
		self.ftpdlTOcalTH_res   = QtWidgets.QLabel("0", self)
		self.ftpdlTOhphr_res    = QtWidgets.QLabel("0", self)
		self.ftpdlTOftlbf_res   = QtWidgets.QLabel("0", self)
		self.ftpdlTOftpdl_res   = QtWidgets.QLabel("0", self)

		self.JTO_Label = [self.JTOJ_res, self.JTOkJ_res, self.JTOkWh_res, self.JTOBTUIT_res, self.JTOBTUmean_res, self.JTOcalIT_res, self.JTOcalTH_res,
						  self.JTOhphr_res, self.JTOftlbf_res, self.JTOftpdl_res]

		self.kJTO_Label = [self.kJTOJ_res, self.kJTOkJ_res, self.kJTOkWh_res, self.kJTOBTUIT_res, self.kJTOBTUmean_res, self.kJTOcalIT_res, self.kJTOcalTH_res,
						   self.kJTOhphr_res, self.kJTOftlbf_res, self.kJTOftpdl_res]

		self.kWhTO_Label = [self.kWhTOJ_res, self.kWhTOkJ_res, self.kWhTOkWh_res, self.kWhTOBTUIT_res, self.kWhTOBTUmean_res, self.kWhTOcalIT_res, self.kWhTOcalTH_res,
						    self.kWhTOhphr_res, self.kWhTOftlbf_res, self.kWhTOftpdl_res]

		self.BTUITTO_Label = [self.BTUITTOJ_res, self.BTUITTOkJ_res, self.BTUITTOkWh_res, self.BTUITTOBTUIT_res, self.BTUITTOBTUmean_res, self.BTUITTOcalIT_res, 
							  self.BTUITTOcalTH_res, self.BTUITTOhphr_res, self.BTUITTOftlbf_res, self.BTUITTOftpdl_res]

		self.BTUmeanTO_Label = [self.BTUmeanTOJ_res, self.BTUmeanTOkJ_res, self.BTUmeanTOkWh_res, self.BTUmeanTOBTUIT_res, self.BTUmeanTOBTUmean_res, 
								self.BTUmeanTOcalIT_res, self.BTUmeanTOcalTH_res, self.BTUmeanTOhphr_res, self.BTUmeanTOftlbf_res, self.BTUmeanTOftpdl_res]

		self.calITTO_Label = [self.calITTOJ_res, self.calITTOkJ_res, self.calITTOkWh_res, self.calITTOBTUIT_res, self.calITTOBTUmean_res, self.calITTOcalIT_res, 
							  self.calITTOcalTH_res, self.calITTOhphr_res, self.calITTOftlbf_res, self.calITTOftpdl_res]

		self.calTHTO_Label = [self.calTHTOJ_res, self.calTHTOkJ_res, self.calTHTOkWh_res, self.calTHTOBTUIT_res, self.calTHTOBTUmean_res, self.calTHTOcalIT_res, 
							  self.calTHTOcalTH_res, self.calTHTOhphr_res, self.calTHTOftlbf_res, self.calTHTOftpdl_res]

		self.hphrTO_Label = [self.hphrTOJ_res, self.hphrTOkJ_res, self.hphrTOkWh_res, self.hphrTOBTUIT_res, self.hphrTOBTUmean_res, self.hphrTOcalIT_res, 
							 self.hphrTOcalTH_res, self.hphrTOhphr_res, self.hphrTOftlbf_res, self.hphrTOftpdl_res]

		self.ftlbfTO_Label = [self.ftlbfTOJ_res, self.ftlbfTOkJ_res, self.ftlbfTOkWh_res, self.ftlbfTOBTUIT_res, self.ftlbfTOBTUmean_res, self.ftlbfTOcalIT_res, 
							  self.ftlbfTOcalTH_res, self.ftlbfTOhphr_res, self.ftlbfTOftlbf_res, self.ftlbfTOftpdl_res]

		self.ftpdlTO_Label = [self.ftpdlTOJ_res, self.ftpdlTOkJ_res, self.ftpdlTOkWh_res, self.ftpdlTOBTUIT_res, self.ftpdlTOBTUmean_res, self.ftpdlTOcalIT_res, 
							  self.ftpdlTOcalTH_res, self.ftpdlTOhphr_res, self.ftpdlTOftlbf_res, self.ftpdlTOftpdl_res]

		i = 0
		for item in self.JTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.kJTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.kWhTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.BTUITTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.BTUmeanTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.calITTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.calTHTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.hphrTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.ftlbfTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.ftpdlTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def JTO_fun(self):
		JTOJ_proc       = float(self.Ji_LinEd.text()) * 1
		JTOkJ_proc      = float(self.Ji_LinEd.text()) * 1e-03
		JTOkWh_proc     = float(self.Ji_LinEd.text()) * 2.777778e-07
		JTOBTUIT_proc   = float(self.Ji_LinEd.text()) * 9.478171e-04
		JTOBTUmean_proc = float(self.Ji_LinEd.text()) * 9.470860e-04
		JTOcalIT_proc   = float(self.Ji_LinEd.text()) * 2.388459e-01
		JTOcalTH_proc   = float(self.Ji_LinEd.text()) * 2.390060e-01
		JTOhphr_proc    = float(self.Ji_LinEd.text()) * 3.725061e-07
		JTOftlbf_proc   = float(self.Ji_LinEd.text()) * 7.375621e-01
		JTOftpdl_proc   = float(self.Ji_LinEd.text()) * 2.373035e+01

		self.JTOJ_res.setText(str(round(JTOJ_proc,             8)))
		self.JTOkJ_res.setText(str(round(JTOkJ_proc,           8)))
		self.JTOkWh_res.setText(str(round(JTOkWh_proc,         8)))
		self.JTOBTUIT_res.setText(str(round(JTOBTUIT_proc,     8)))
		self.JTOBTUmean_res.setText(str(round(JTOBTUmean_proc, 8)))
		self.JTOcalIT_res.setText(str(round(JTOcalIT_proc,     8)))
		self.JTOcalTH_res.setText(str(round(JTOcalTH_proc,     8)))
		self.JTOhphr_res.setText(str(round(JTOhphr_proc,       8)))
		self.JTOftlbf_res.setText(str(round(JTOftlbf_proc,     8)))
		self.JTOftpdl_res.setText(str(round(JTOftpdl_proc,     8)))

	def kJTO_fun(self):
		kJTOJ_proc       = float(self.kJi_LinEd.text()) * 1e+03
		kJTOkJ_proc      = float(self.kJi_LinEd.text()) * 1
		kJTOkWh_proc     = float(self.kJi_LinEd.text()) * 2.777778e-04
		kJTOBTUIT_proc   = float(self.kJi_LinEd.text()) * 9.478171e-01
		kJTOBTUmean_proc = float(self.kJi_LinEd.text()) * 9.470860e-01
		kJTOcalIT_proc   = float(self.kJi_LinEd.text()) * 2.388459e+02
		kJTOcalTH_proc   = float(self.kJi_LinEd.text()) * 2.390060e+02
		kJTOhphr_proc    = float(self.kJi_LinEd.text()) * 3.725061e-04
		kJTOftlbf_proc   = float(self.kJi_LinEd.text()) * 7.375621e+02
		kJTOftpdl_proc   = float(self.kJi_LinEd.text()) * 2.373035e+04

		self.kJTOJ_res.setText(str(round(kJTOJ_proc,             8)))
		self.kJTOkJ_res.setText(str(round(kJTOkJ_proc,           8)))
		self.kJTOkWh_res.setText(str(round(kJTOkWh_proc,         8)))
		self.kJTOBTUIT_res.setText(str(round(kJTOBTUIT_proc,     8)))
		self.kJTOBTUmean_res.setText(str(round(kJTOBTUmean_proc, 8)))
		self.kJTOcalIT_res.setText(str(round(kJTOcalIT_proc,     8)))
		self.kJTOcalTH_res.setText(str(round(kJTOcalTH_proc,     8)))
		self.kJTOhphr_res.setText(str(round(kJTOhphr_proc,       8)))
		self.kJTOftlbf_res.setText(str(round(kJTOftlbf_proc,     8)))
		self.kJTOftpdl_res.setText(str(round(kJTOftpdl_proc,     8)))

	def kWhTO_fun(self):
		kWhTOJ_proc       = float(self.kWhi_LinEd.text()) * 3.6e+6
		kWhTOkJ_proc      = float(self.kWhi_LinEd.text()) * 3.6e+03
		kWhTOkWh_proc     = float(self.kWhi_LinEd.text()) * 1
		kWhTOBTUIT_proc   = float(self.kWhi_LinEd.text()) * 3.412142e+03
		kWhTOBTUmean_proc = float(self.kWhi_LinEd.text()) * 3.409511e+03
		kWhTOcalIT_proc   = float(self.kWhi_LinEd.text()) * 8.598452e+5
		kWhTOcalTH_proc   = float(self.kWhi_LinEd.text()) * 8.598452e+5 * 1.0006692160611856
		kWhTOhphr_proc    = float(self.kWhi_LinEd.text()) * 1.341022
		kWhTOftlbf_proc   = float(self.kWhi_LinEd.text()) * 2.65522373748e+06
		kWhTOftpdl_proc   = float(self.kWhi_LinEd.text()) * 8.542929764555995e+07

		self.kWhTOJ_res.setText(str(round(kWhTOJ_proc,             8)))
		self.kWhTOkJ_res.setText(str(round(kWhTOkJ_proc,           8)))
		self.kWhTOkWh_res.setText(str(round(kWhTOkWh_proc,         8)))
		self.kWhTOBTUIT_res.setText(str(round(kWhTOBTUIT_proc,     8)))
		self.kWhTOBTUmean_res.setText(str(round(kWhTOBTUmean_proc, 8)))
		self.kWhTOcalIT_res.setText(str(round(kWhTOcalIT_proc,     8)))
		self.kWhTOcalTH_res.setText(str(round(kWhTOcalTH_proc,     8)))
		self.kWhTOhphr_res.setText(str(round(kWhTOhphr_proc,       8)))
		self.kWhTOftlbf_res.setText(str(round(kWhTOftlbf_proc,     8)))
		self.kWhTOftpdl_res.setText(str(round(kWhTOftpdl_proc,     8)))

	def BTUITTO_fun(self):
		BTUITTOJ_proc       = float(self.BTUITi_LinEd.text()) * 1.055056e+03
		BTUITTOkJ_proc      = float(self.BTUITi_LinEd.text()) * 1.055056
		BTUITTOkWh_proc     = float(self.BTUITi_LinEd.text()) * 2.930711e-04
		BTUITTOBTUIT_proc   = float(self.BTUITi_LinEd.text()) * 1
		BTUITTOBTUmean_proc = float(self.BTUITi_LinEd.text()) * 0.999229072
		BTUITTOcalIT_proc   = float(self.BTUITi_LinEd.text()) * 2.519958e+02
		BTUITTOcalTH_proc   = float(self.BTUITi_LinEd.text()) * 2.519958e+02 * 1.0006692160611856
		BTUITTOhphr_proc    = float(self.BTUITi_LinEd.text()) * 3.930148e-04
		BTUITTOftlbf_proc   = float(self.BTUITi_LinEd.text()) * 7.781692e+02
		BTUITTOftpdl_proc   = float(self.BTUITi_LinEd.text()) * 2.5036855685e+04

		self.BTUITTOJ_res.setText(str(round(BTUITTOJ_proc,             8)))
		self.BTUITTOkJ_res.setText(str(round(BTUITTOkJ_proc,           8)))
		self.BTUITTOkWh_res.setText(str(round(BTUITTOkWh_proc,         8)))
		self.BTUITTOBTUIT_res.setText(str(round(BTUITTOBTUIT_proc,     8)))
		self.BTUITTOBTUmean_res.setText(str(round(BTUITTOBTUmean_proc, 8)))
		self.BTUITTOcalIT_res.setText(str(round(BTUITTOcalIT_proc,     8)))
		self.BTUITTOcalTH_res.setText(str(round(BTUITTOcalTH_proc,     8)))
		self.BTUITTOhphr_res.setText(str(round(BTUITTOhphr_proc,       8)))
		self.BTUITTOftlbf_res.setText(str(round(BTUITTOftlbf_proc,     8)))
		self.BTUITTOftpdl_res.setText(str(round(BTUITTOftpdl_proc,     8)))

	def BTUmeanTO_fun(self):
		BTUmeanTOJ_proc       = float(self.BTUmeani_LinEd.text()) * 1.05587e+03
		BTUmeanTOkJ_proc      = float(self.BTUmeani_LinEd.text()) * 1.05587
		BTUmeanTOkWh_proc     = float(self.BTUmeani_LinEd.text()) * 1055.87 / 3600000
		BTUmeanTOBTUIT_proc   = float(self.BTUmeani_LinEd.text()) * 1055.87 / 1005.056
		BTUmeanTOBTUmean_proc = float(self.BTUmeani_LinEd.text()) * 1
		BTUmeanTOcalIT_proc   = float(self.BTUmeani_LinEd.text()) * 1055.87 / 4.1868
		BTUmeanTOcalTH_proc   = float(self.BTUmeani_LinEd.text()) * 1055.87 / 4.184
		BTUmeanTOhphr_proc    = float(self.BTUmeani_LinEd.text()) * 1055.87 / (745.6999*3600)
		BTUmeanTOftlbf_proc   = float(self.BTUmeani_LinEd.text()) * 1055.87 / 1005.056 * 7.781692e+02
		BTUmeanTOftpdl_proc   = float(self.BTUmeani_LinEd.text()) * 1055.87 / 1005.056 * 2.5036855685e+04

		self.BTUmeanTOJ_res.setText(str(round(BTUmeanTOJ_proc,             8)))
		self.BTUmeanTOkJ_res.setText(str(round(BTUmeanTOkJ_proc,           8)))
		self.BTUmeanTOkWh_res.setText(str(round(BTUmeanTOkWh_proc,         8)))
		self.BTUmeanTOBTUIT_res.setText(str(round(BTUmeanTOBTUIT_proc,     8)))
		self.BTUmeanTOBTUmean_res.setText(str(round(BTUmeanTOBTUmean_proc, 8)))
		self.BTUmeanTOcalIT_res.setText(str(round(BTUmeanTOcalIT_proc,     8)))
		self.BTUmeanTOcalTH_res.setText(str(round(BTUmeanTOcalTH_proc,     8)))
		self.BTUmeanTOhphr_res.setText(str(round(BTUmeanTOhphr_proc,       8)))
		self.BTUmeanTOftlbf_res.setText(str(round(BTUmeanTOftlbf_proc,     8)))
		self.BTUmeanTOftpdl_res.setText(str(round(BTUmeanTOftpdl_proc,     8)))

	def calITTO_fun(self):
		calITTOJ_proc       = float(self.calITi_LinEd.text()) * 4.1868
		calITTOkJ_proc      = float(self.calITi_LinEd.text()) * 4.1868e-03
		calITTOkWh_proc     = float(self.calITi_LinEd.text()) * 1.163e-06
		calITTOBTUIT_proc   = float(self.calITi_LinEd.text()) * 3.968321e-03
		calITTOBTUmean_proc = float(self.calITi_LinEd.text()) * 1055.87 / 4.1868
		calITTOcalIT_proc   = float(self.calITi_LinEd.text()) * 1
		calITTOcalTH_proc   = float(self.calITi_LinEd.text()) * 1.0006692160611856
		calITTOhphr_proc    = float(self.calITi_LinEd.text()) * 1.559609e-06
		calITTOftlbf_proc   = float(self.calITi_LinEd.text()) * 3.0880252066892404
		calITTOftpdl_proc   = float(self.calITi_LinEd.text()) * 99.35427316178622

		self.calITTOJ_res.setText(str(round(calITTOJ_proc,             8)))
		self.calITTOkJ_res.setText(str(round(calITTOkJ_proc,           8)))
		self.calITTOkWh_res.setText(str(round(calITTOkWh_proc,         8)))
		self.calITTOBTUIT_res.setText(str(round(calITTOBTUIT_proc,     8)))
		self.calITTOBTUmean_res.setText(str(round(calITTOBTUmean_proc, 8)))
		self.calITTOcalIT_res.setText(str(round(calITTOcalIT_proc,     8)))
		self.calITTOcalTH_res.setText(str(round(calITTOcalTH_proc,     8)))
		self.calITTOhphr_res.setText(str(round(calITTOhphr_proc,       8)))
		self.calITTOftlbf_res.setText(str(round(calITTOftlbf_proc,     8)))
		self.calITTOftpdl_res.setText(str(round(calITTOftpdl_proc,     8)))

	def calTHTO_fun(self):
		calTHTOJ_proc       = float(self.calTHi_LinEd.text()) * 4.184
		calTHTOkJ_proc      = float(self.calTHi_LinEd.text()) * 4.184e-03
		calTHTOkWh_proc     = float(self.calTHi_LinEd.text()) * 0.0000011622222222
		calTHTOBTUIT_proc   = float(self.calTHi_LinEd.text()) * 0.0039656668313
		calTHTOBTUmean_proc = float(self.calTHi_LinEd.text()) * 4.184 / 1055.87
		calTHTOcalIT_proc   = float(self.calTHi_LinEd.text()) * 0.9993312314894429
		calTHTOcalTH_proc   = float(self.calTHi_LinEd.text()) * 1
		calTHTOhphr_proc    = float(self.calTHi_LinEd.text()) * 0.0000015585656734888427
		calTHTOftlbf_proc   = float(self.calTHi_LinEd.text()) * 3.0859600326712
		calTHTOftpdl_proc   = float(self.calTHi_LinEd.text()) * 99.28782815250634

		self.calTHTOJ_res.setText(str(round(calTHTOJ_proc,             8)))
		self.calTHTOkJ_res.setText(str(round(calTHTOkJ_proc,           8)))
		self.calTHTOkWh_res.setText(str(round(calTHTOkWh_proc,         8)))
		self.calTHTOBTUIT_res.setText(str(round(calTHTOBTUIT_proc,     8)))
		self.calTHTOBTUmean_res.setText(str(round(calTHTOBTUmean_proc, 8)))
		self.calTHTOcalIT_res.setText(str(round(calTHTOcalIT_proc,     8)))
		self.calTHTOcalTH_res.setText(str(round(calTHTOcalTH_proc,     8)))
		self.calTHTOhphr_res.setText(str(round(calTHTOhphr_proc,       8)))
		self.calTHTOftlbf_res.setText(str(round(calTHTOftlbf_proc,     8)))
		self.calTHTOftpdl_res.setText(str(round(calTHTOftpdl_proc,     8)))

	def hphrTO_fun(self):
		hphrTOJ_proc       = float(self.hphri_LinEd.text()) * 2.68452e+06
		hphrTOkJ_proc      = float(self.hphri_LinEd.text()) * 2.68452e+03
		hphrTOkWh_proc     = float(self.hphri_LinEd.text()) * 0.7456999
		hphrTOBTUIT_proc   = float(self.hphri_LinEd.text()) * 2.544434e+03
		hphrTOBTUmean_proc = float(self.hphri_LinEd.text()) * 745.6999 * 3600 / 1055.87
		hphrTOcalIT_proc   = float(self.hphri_LinEd.text()) * 6.411865e+05
		hphrTOcalTH_proc   = float(self.hphri_LinEd.text()) * 6.416155680892831e+05
		hphrTOhphr_proc    = float(self.hphri_LinEd.text()) * 1
		hphrTOftlbf_proc   = float(self.hphri_LinEd.text()) * 1.9799999994631547e+06
		hphrTOftpdl_proc   = float(self.hphri_LinEd.text()) * 6.3704616264e+07

		self.hphrTOJ_res.setText(str(round(hphrTOJ_proc,             8)))
		self.hphrTOkJ_res.setText(str(round(hphrTOkJ_proc,           8)))
		self.hphrTOkWh_res.setText(str(round(hphrTOkWh_proc,         8)))
		self.hphrTOBTUIT_res.setText(str(round(hphrTOBTUIT_proc,     8)))
		self.hphrTOBTUmean_res.setText(str(round(hphrTOBTUmean_proc, 8)))
		self.hphrTOcalIT_res.setText(str(round(hphrTOcalIT_proc,     8)))
		self.hphrTOcalTH_res.setText(str(round(hphrTOcalTH_proc,     8)))
		self.hphrTOhphr_res.setText(str(round(hphrTOhphr_proc,       8)))
		self.hphrTOftlbf_res.setText(str(round(hphrTOftlbf_proc,     8)))
		self.hphrTOftpdl_res.setText(str(round(hphrTOftpdl_proc,     8)))

	def ftlbfTO_fun(self):
		ftlbfTOJ_proc       = float(self.ftlbfi_LinEd.text()) * 1.355818
		ftlbfTOkJ_proc      = float(self.ftlbfi_LinEd.text()) * 1.355818e-03
		ftlbfTOkWh_proc     = float(self.ftlbfi_LinEd.text()) * 3.766161e-07
		ftlbfTOBTUIT_proc   = float(self.ftlbfi_LinEd.text()) * 1.285068e-03
		ftlbfTOBTUmean_proc = float(self.ftlbfi_LinEd.text()) * 0.3048 * 4.448222 / 1055.87
		ftlbfTOcalIT_proc   = float(self.ftlbfi_LinEd.text()) * 3.238316e-01
		ftlbfTOcalTH_proc   = float(self.ftlbfi_LinEd.text()) * 0.3240482667996196
		ftlbfTOhphr_proc    = float(self.ftlbfi_LinEd.text()) * 5.050505e-07
		ftlbfTOftlbf_proc   = float(self.ftlbfi_LinEd.text()) * 1
		ftlbfTOftpdl_proc   = float(self.ftlbfi_LinEd.text()) * 32.174048627

		self.ftlbfTOJ_res.setText(str(round(ftlbfTOJ_proc,             8)))
		self.ftlbfTOkJ_res.setText(str(round(ftlbfTOkJ_proc,           8)))
		self.ftlbfTOkWh_res.setText(str(round(ftlbfTOkWh_proc,         8)))
		self.ftlbfTOBTUIT_res.setText(str(round(ftlbfTOBTUIT_proc,     8)))
		self.ftlbfTOBTUmean_res.setText(str(round(ftlbfTOBTUmean_proc, 8)))
		self.ftlbfTOcalIT_res.setText(str(round(ftlbfTOcalIT_proc,     8)))
		self.ftlbfTOcalTH_res.setText(str(round(ftlbfTOcalTH_proc,     8)))
		self.ftlbfTOhphr_res.setText(str(round(ftlbfTOhphr_proc,       8)))
		self.ftlbfTOftlbf_res.setText(str(round(ftlbfTOftlbf_proc,     8)))
		self.ftlbfTOftpdl_res.setText(str(round(ftlbfTOftpdl_proc,     8)))

	def ftpdlTO_fun(self):
		ftpdlTOJ_proc       = float(self.ftpdli_LinEd.text()) * 0.0421401099999223
		ftpdlTOkJ_proc      = float(self.ftpdli_LinEd.text()) * 0.0421401099999223e+03
		ftpdlTOkWh_proc     = float(self.ftpdli_LinEd.text()) * 1.1705586111e-08
		ftpdlTOBTUIT_proc   = float(self.ftpdli_LinEd.text()) * 3.9941117709812745e-05
		ftpdlTOBTUmean_proc = float(self.ftpdli_LinEd.text()) * 0.3048 * 0.138255 / 1055.87
		ftpdlTOcalIT_proc   = float(self.ftpdli_LinEd.text()) * 1.0064992356912751e-02
		ftpdlTOcalTH_proc   = float(self.ftpdli_LinEd.text()) * 1.0071728011e-02
		ftpdlTOhphr_proc    = float(self.ftpdli_LinEd.text()) * 1.5697449551e-08
		ftpdlTOftlbf_proc   = float(self.ftpdli_LinEd.text()) * 3.1080950103e-02
		ftpdlTOftpdl_proc   = float(self.ftpdli_LinEd.text()) * 1

		self.ftpdlTOJ_res.setText(str(round(ftpdlTOJ_proc,             8)))
		self.ftpdlTOkJ_res.setText(str(round(ftpdlTOkJ_proc,           8)))
		self.ftpdlTOkWh_res.setText(str(round(ftpdlTOkWh_proc,         8)))
		self.ftpdlTOBTUIT_res.setText(str(round(ftpdlTOBTUIT_proc,     8)))
		self.ftpdlTOBTUmean_res.setText(str(round(ftpdlTOBTUmean_proc, 8)))
		self.ftpdlTOcalIT_res.setText(str(round(ftpdlTOcalIT_proc,     8)))
		self.ftpdlTOcalTH_res.setText(str(round(ftpdlTOcalTH_proc,     8)))
		self.ftpdlTOhphr_res.setText(str(round(ftpdlTOhphr_proc,       8)))
		self.ftpdlTOftlbf_res.setText(str(round(ftpdlTOftlbf_proc,     8)))
		self.ftpdlTOftpdl_res.setText(str(round(ftpdlTOftpdl_proc,     8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Force_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Force_Win")



class Heatcond_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatcond_Win")



class Heatres_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatres_Win")



class Heattrans_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heattrans_Win")



class Length_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Length Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel       = QtWidgets.QLabel()
		self.mi_LinEd    = QtWidgets.QLineEdit()
		self.cmi_LinEd   = QtWidgets.QLineEdit()
		self.mmi_LinEd   = QtWidgets.QLineEdit()
		self.umi_LinEd   = QtWidgets.QLineEdit()
		self.angsi_LinEd = QtWidgets.QLineEdit()
		self.nmi_LinEd   = QtWidgets.QLineEdit()
		self.kmi_LinEd   = QtWidgets.QLineEdit()
		self.ini_LinEd	 = QtWidgets.QLineEdit()
		self.fti_LinEd	 = QtWidgets.QLineEdit()
		self.ydi_LinEd   = QtWidgets.QLineEdit()
		self.miSTi_LinEd = QtWidgets.QLineEdit()
		self.miNVi_LinEd = QtWidgets.QLineEdit()

		LinEd_list = [self.mi_LinEd, self.cmi_LinEd, self.mmi_LinEd, self.umi_LinEd, self.angsi_LinEd, self.nmi_LinEd, self.kmi_LinEd, self.ini_LinEd, self.fti_LinEd,
					  self.ydi_LinEd, self.miSTi_LinEd, self.miNVi_LinEd]

		Label_list = [blanklabel, "m", "cm", "mm", "\u03BCm & micron", "Å", "nm", "km", "in", "ft", "yard", "mile<sub>statute</sub>", "mile<sub>navy</sub>"]

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

		self.mi_LinEd.returnPressed.connect(self.mTO_fun)
		self.cmi_LinEd.returnPressed.connect(self.cmTO_fun)
		self.mmi_LinEd.returnPressed.connect(self.mmTO_fun)
		self.umi_LinEd.returnPressed.connect(self.umTO_fun)
		self.angsi_LinEd.returnPressed.connect(self.angsTO_fun)
		self.nmi_LinEd.returnPressed.connect(self.nmTO_fun)
		self.kmi_LinEd.returnPressed.connect(self.kmTO_fun)
		self.ini_LinEd.returnPressed.connect(self.inTO_fun)
		self.fti_LinEd.returnPressed.connect(self.ftTO_fun)
		self.ydi_LinEd.returnPressed.connect(self.ydTO_fun)
		self.miSTi_LinEd.returnPressed.connect(self.miSTTO_fun)
		self.miNVi_LinEd.returnPressed.connect(self.miNVTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()
		
		Label_list = ["m", "cm", "mm", "\u03BCm & micron", "Å", "nm", "km", "in", "ft", "yard", "mile<sub>statute</sub>", "mile<sub>navy</sub>"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.mTOm_res    = QtWidgets.QLabel("0", self)
		self.mTOcm_res   = QtWidgets.QLabel("0", self)
		self.mTOmm_res   = QtWidgets.QLabel("0", self)
		self.mTOum_res   = QtWidgets.QLabel("0", self)
		self.mTOangs_res = QtWidgets.QLabel("0", self)
		self.mTOnm_res   = QtWidgets.QLabel("0", self)
		self.mTOkm_res   = QtWidgets.QLabel("0", self)
		self.mTOin_res   = QtWidgets.QLabel("0", self)
		self.mTOft_res   = QtWidgets.QLabel("0", self)
		self.mTOyd_res   = QtWidgets.QLabel("0", self)
		self.mTOmiST_res = QtWidgets.QLabel("0", self)
		self.mTOmiNV_res = QtWidgets.QLabel("0", self)

		self.cmTOm_res    = QtWidgets.QLabel("0", self)
		self.cmTOcm_res   = QtWidgets.QLabel("0", self)
		self.cmTOmm_res   = QtWidgets.QLabel("0", self)
		self.cmTOum_res   = QtWidgets.QLabel("0", self)
		self.cmTOangs_res = QtWidgets.QLabel("0", self)
		self.cmTOnm_res   = QtWidgets.QLabel("0", self)
		self.cmTOkm_res   = QtWidgets.QLabel("0", self)
		self.cmTOin_res   = QtWidgets.QLabel("0", self)
		self.cmTOft_res   = QtWidgets.QLabel("0", self)
		self.cmTOyd_res   = QtWidgets.QLabel("0", self)
		self.cmTOmiST_res = QtWidgets.QLabel("0", self)
		self.cmTOmiNV_res = QtWidgets.QLabel("0", self)

		self.mmTOm_res    = QtWidgets.QLabel("0", self)
		self.mmTOcm_res   = QtWidgets.QLabel("0", self)
		self.mmTOmm_res   = QtWidgets.QLabel("0", self)
		self.mmTOum_res   = QtWidgets.QLabel("0", self)
		self.mmTOangs_res = QtWidgets.QLabel("0", self)
		self.mmTOnm_res   = QtWidgets.QLabel("0", self)
		self.mmTOkm_res   = QtWidgets.QLabel("0", self)
		self.mmTOin_res   = QtWidgets.QLabel("0", self)
		self.mmTOft_res   = QtWidgets.QLabel("0", self)
		self.mmTOyd_res   = QtWidgets.QLabel("0", self)
		self.mmTOmiST_res = QtWidgets.QLabel("0", self)
		self.mmTOmiNV_res = QtWidgets.QLabel("0", self)

		self.umTOm_res    = QtWidgets.QLabel("0", self)
		self.umTOcm_res   = QtWidgets.QLabel("0", self)
		self.umTOmm_res   = QtWidgets.QLabel("0", self)
		self.umTOum_res   = QtWidgets.QLabel("0", self)
		self.umTOangs_res = QtWidgets.QLabel("0", self)
		self.umTOnm_res   = QtWidgets.QLabel("0", self)
		self.umTOkm_res   = QtWidgets.QLabel("0", self)
		self.umTOin_res   = QtWidgets.QLabel("0", self)
		self.umTOft_res   = QtWidgets.QLabel("0", self)
		self.umTOyd_res   = QtWidgets.QLabel("0", self)
		self.umTOmiST_res = QtWidgets.QLabel("0", self)
		self.umTOmiNV_res = QtWidgets.QLabel("0", self)

		self.angsTOm_res    = QtWidgets.QLabel("0", self)
		self.angsTOcm_res   = QtWidgets.QLabel("0", self)
		self.angsTOmm_res   = QtWidgets.QLabel("0", self)
		self.angsTOum_res   = QtWidgets.QLabel("0", self)
		self.angsTOangs_res = QtWidgets.QLabel("0", self)
		self.angsTOnm_res   = QtWidgets.QLabel("0", self)
		self.angsTOkm_res   = QtWidgets.QLabel("0", self)
		self.angsTOin_res   = QtWidgets.QLabel("0", self)
		self.angsTOft_res   = QtWidgets.QLabel("0", self)
		self.angsTOyd_res   = QtWidgets.QLabel("0", self)
		self.angsTOmiST_res = QtWidgets.QLabel("0", self)
		self.angsTOmiNV_res = QtWidgets.QLabel("0", self)

		self.nmTOm_res    = QtWidgets.QLabel("0", self)
		self.nmTOcm_res   = QtWidgets.QLabel("0", self)
		self.nmTOmm_res   = QtWidgets.QLabel("0", self)
		self.nmTOum_res   = QtWidgets.QLabel("0", self)
		self.nmTOangs_res = QtWidgets.QLabel("0", self)
		self.nmTOnm_res   = QtWidgets.QLabel("0", self)
		self.nmTOkm_res   = QtWidgets.QLabel("0", self)
		self.nmTOin_res   = QtWidgets.QLabel("0", self)
		self.nmTOft_res   = QtWidgets.QLabel("0", self)
		self.nmTOyd_res   = QtWidgets.QLabel("0", self)
		self.nmTOmiST_res = QtWidgets.QLabel("0", self)
		self.nmTOmiNV_res = QtWidgets.QLabel("0", self)

		self.kmTOm_res    = QtWidgets.QLabel("0", self)
		self.kmTOcm_res   = QtWidgets.QLabel("0", self)
		self.kmTOmm_res   = QtWidgets.QLabel("0", self)
		self.kmTOum_res   = QtWidgets.QLabel("0", self)
		self.kmTOangs_res = QtWidgets.QLabel("0", self)
		self.kmTOnm_res   = QtWidgets.QLabel("0", self)
		self.kmTOkm_res   = QtWidgets.QLabel("0", self)
		self.kmTOin_res   = QtWidgets.QLabel("0", self)
		self.kmTOft_res   = QtWidgets.QLabel("0", self)
		self.kmTOyd_res   = QtWidgets.QLabel("0", self)
		self.kmTOmiST_res = QtWidgets.QLabel("0", self)
		self.kmTOmiNV_res = QtWidgets.QLabel("0", self)

		self.inTOm_res    = QtWidgets.QLabel("0", self)
		self.inTOcm_res   = QtWidgets.QLabel("0", self)
		self.inTOmm_res   = QtWidgets.QLabel("0", self)
		self.inTOum_res   = QtWidgets.QLabel("0", self)
		self.inTOangs_res = QtWidgets.QLabel("0", self)
		self.inTOnm_res   = QtWidgets.QLabel("0", self)
		self.inTOkm_res   = QtWidgets.QLabel("0", self)
		self.inTOin_res   = QtWidgets.QLabel("0", self)
		self.inTOft_res   = QtWidgets.QLabel("0", self)
		self.inTOyd_res   = QtWidgets.QLabel("0", self)
		self.inTOmiST_res = QtWidgets.QLabel("0", self)
		self.inTOmiNV_res = QtWidgets.QLabel("0", self)

		self.ftTOm_res    = QtWidgets.QLabel("0", self)
		self.ftTOcm_res   = QtWidgets.QLabel("0", self)
		self.ftTOmm_res   = QtWidgets.QLabel("0", self)
		self.ftTOum_res   = QtWidgets.QLabel("0", self)
		self.ftTOangs_res = QtWidgets.QLabel("0", self)
		self.ftTOnm_res   = QtWidgets.QLabel("0", self)
		self.ftTOkm_res   = QtWidgets.QLabel("0", self)
		self.ftTOin_res   = QtWidgets.QLabel("0", self)
		self.ftTOft_res   = QtWidgets.QLabel("0", self)
		self.ftTOyd_res   = QtWidgets.QLabel("0", self)
		self.ftTOmiST_res = QtWidgets.QLabel("0", self)
		self.ftTOmiNV_res = QtWidgets.QLabel("0", self)

		self.ydTOm_res    = QtWidgets.QLabel("0", self)
		self.ydTOcm_res   = QtWidgets.QLabel("0", self)
		self.ydTOmm_res   = QtWidgets.QLabel("0", self)
		self.ydTOum_res   = QtWidgets.QLabel("0", self)
		self.ydTOangs_res = QtWidgets.QLabel("0", self)
		self.ydTOnm_res   = QtWidgets.QLabel("0", self)
		self.ydTOkm_res   = QtWidgets.QLabel("0", self)
		self.ydTOin_res   = QtWidgets.QLabel("0", self)
		self.ydTOft_res   = QtWidgets.QLabel("0", self)
		self.ydTOyd_res   = QtWidgets.QLabel("0", self)
		self.ydTOmiST_res = QtWidgets.QLabel("0", self)
		self.ydTOmiNV_res = QtWidgets.QLabel("0", self)

		self.miSTTOm_res    = QtWidgets.QLabel("0", self)
		self.miSTTOcm_res   = QtWidgets.QLabel("0", self)
		self.miSTTOmm_res   = QtWidgets.QLabel("0", self)
		self.miSTTOum_res   = QtWidgets.QLabel("0", self)
		self.miSTTOangs_res = QtWidgets.QLabel("0", self)
		self.miSTTOnm_res   = QtWidgets.QLabel("0", self)
		self.miSTTOkm_res   = QtWidgets.QLabel("0", self)
		self.miSTTOin_res   = QtWidgets.QLabel("0", self)
		self.miSTTOft_res   = QtWidgets.QLabel("0", self)
		self.miSTTOyd_res   = QtWidgets.QLabel("0", self)
		self.miSTTOmiST_res = QtWidgets.QLabel("0", self)
		self.miSTTOmiNV_res = QtWidgets.QLabel("0", self)

		self.miNVTOm_res    = QtWidgets.QLabel("0", self)
		self.miNVTOcm_res   = QtWidgets.QLabel("0", self)
		self.miNVTOmm_res   = QtWidgets.QLabel("0", self)
		self.miNVTOum_res   = QtWidgets.QLabel("0", self)
		self.miNVTOangs_res = QtWidgets.QLabel("0", self)
		self.miNVTOnm_res   = QtWidgets.QLabel("0", self)
		self.miNVTOkm_res   = QtWidgets.QLabel("0", self)
		self.miNVTOin_res   = QtWidgets.QLabel("0", self)
		self.miNVTOft_res   = QtWidgets.QLabel("0", self)
		self.miNVTOyd_res   = QtWidgets.QLabel("0", self)
		self.miNVTOmiST_res = QtWidgets.QLabel("0", self)
		self.miNVTOmiNV_res = QtWidgets.QLabel("0", self)

		self.mTO_Label = [self.mTOm_res, self.mTOcm_res, self.mTOmm_res, self.mTOum_res, self.mTOangs_res, self.mTOnm_res, self.mTOkm_res, self.mTOin_res, self.mTOft_res,
						  self.mTOyd_res, self.mTOmiST_res, self.mTOmiNV_res]

		self.cmTO_Label = [self.cmTOm_res, self.cmTOcm_res, self.cmTOmm_res, self.cmTOum_res, self.cmTOangs_res, self.cmTOnm_res, self.cmTOkm_res, self.cmTOin_res, 
						   self.cmTOft_res, self.cmTOyd_res, self.cmTOmiST_res, self.cmTOmiNV_res]

		self.mmTO_Label = [self.mmTOm_res, self.mmTOcm_res, self.mmTOmm_res, self.mmTOum_res, self.mmTOangs_res, self.mmTOnm_res, self.mmTOkm_res, self.mmTOin_res, 
						   self.mmTOft_res, self.mmTOyd_res, self.mmTOmiST_res, self.mmTOmiNV_res]

		self.umTO_Label = [self.umTOm_res, self.umTOcm_res, self.umTOmm_res, self.umTOum_res, self.umTOangs_res, self.umTOnm_res, self.umTOkm_res, self.umTOin_res, 
						   self.umTOft_res, self.umTOyd_res, self.umTOmiST_res, self.umTOmiNV_res]

		self.angsTO_Label = [self.angsTOm_res, self.angsTOcm_res, self.angsTOmm_res, self.angsTOum_res, self.angsTOangs_res, self.angsTOnm_res, self.angsTOkm_res, 
							 self.angsTOin_res, self.angsTOft_res, self.angsTOyd_res, self.angsTOmiST_res, self.angsTOmiNV_res]

		self.nmTO_Label = [self.nmTOm_res, self.nmTOcm_res, self.nmTOmm_res, self.nmTOum_res, self.nmTOangs_res, self.nmTOnm_res, self.nmTOkm_res, self.nmTOin_res, 
						   self.nmTOft_res, self.nmTOyd_res, self.nmTOmiST_res, self.nmTOmiNV_res]

		self.kmTO_Label = [self.kmTOm_res, self.kmTOcm_res, self.kmTOmm_res, self.kmTOum_res, self.kmTOangs_res, self.kmTOnm_res, self.kmTOkm_res, self.kmTOin_res, 
						   self.kmTOft_res, self.kmTOyd_res, self.kmTOmiST_res, self.kmTOmiNV_res]

		self.inTO_Label = [self.inTOm_res, self.inTOcm_res, self.inTOmm_res, self.inTOum_res, self.inTOangs_res, self.inTOnm_res, self.inTOkm_res, self.inTOin_res, 
						   self.inTOft_res, self.inTOyd_res, self.inTOmiST_res, self.inTOmiNV_res]

		self.ftTO_Label = [self.ftTOm_res, self.ftTOcm_res, self.ftTOmm_res, self.ftTOum_res, self.ftTOangs_res, self.ftTOnm_res, self.ftTOkm_res, self.ftTOin_res, 
						   self.ftTOft_res, self.ftTOyd_res, self.ftTOmiST_res, self.ftTOmiNV_res]

		self.ydTO_Label = [self.ydTOm_res, self.ydTOcm_res, self.ydTOmm_res, self.ydTOum_res, self.ydTOangs_res, self.ydTOnm_res, self.ydTOkm_res, self.ydTOin_res, 
						   self.ydTOft_res, self.ydTOyd_res, self.ydTOmiST_res, self.ydTOmiNV_res]

		self.miSTTO_Label = [self.miSTTOm_res, self.miSTTOcm_res, self.miSTTOmm_res, self.miSTTOum_res, self.miSTTOangs_res, self.miSTTOnm_res, self.miSTTOkm_res, 
							 self.miSTTOin_res, self.miSTTOft_res, self.miSTTOyd_res, self.miSTTOmiST_res, self.miSTTOmiNV_res]

		self.miNVTO_Label = [self.miNVTOm_res, self.miNVTOcm_res, self.miNVTOmm_res, self.miNVTOum_res, self.miNVTOangs_res, self.miNVTOnm_res, self.miNVTOkm_res, 
							 self.miNVTOin_res, self.miNVTOft_res, self.miNVTOyd_res, self.miNVTOmiST_res, self.miNVTOmiNV_res]

		i = 0
		for item in self.mTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.cmTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.mmTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.umTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.angsTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.nmTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.kmTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.inTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.ftTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.ydTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.miSTTO_Label:
			output_grid.addWidget(item, 11, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.miNVTO_Label:
			output_grid.addWidget(item, 12, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def mTO_fun(self):
		mTOm_proc    = float(self.mi_LinEd.text()) * 1
		mTOcm_proc   = float(self.mi_LinEd.text()) * 1e+02
		mTOmm_proc   = float(self.mi_LinEd.text()) * 1e+03
		mTOum_proc   = float(self.mi_LinEd.text()) * 1e+06
		# mTOangs_proc = float(self.mi_LinEd.text()) * 1e+08
		# mTOnm_proc   = float(self.mi_LinEd.text()) * 1e+09
		mTOkm_proc   = float(self.mi_LinEd.text()) * 1e-03
		mTOin_proc   = float(self.mi_LinEd.text()) * 3.937008e+01
		mTOft_proc   = float(self.mi_LinEd.text()) * 3.280840
		mTOyd_proc   = float(self.mi_LinEd.text()) * 1.093613
		mTOmiST_proc = float(self.mi_LinEd.text()) * 6.213712e-04
		mTOmiNV_proc = float(self.mi_LinEd.text()) * 5.399568e-04

		self.mTOm_res.setText(str(round(mTOm_proc,       8)))
		self.mTOcm_res.setText(str(round(mTOcm_proc,     8)))
		self.mTOmm_res.setText(str(round(mTOmm_proc,     8)))
		self.mTOum_res.setText(str(round(mTOum_proc,     8)))
		self.mTOangs_res.setText("-")
		self.mTOnm_res.setText("-")
		self.mTOkm_res.setText(str(round(mTOkm_proc,     8)))
		self.mTOin_res.setText(str(round(mTOin_proc,     8)))
		self.mTOft_res.setText(str(round(mTOft_proc,     8)))
		self.mTOyd_res.setText(str(round(mTOyd_proc,     8)))
		self.mTOmiST_res.setText(str(round(mTOmiST_proc, 8)))
		self.mTOmiNV_res.setText(str(round(mTOmiNV_proc, 8)))

	def cmTO_fun(self):
		cmTOm_proc    = float(self.cmi_LinEd.text()) * 1e-02
		cmTOcm_proc   = float(self.cmi_LinEd.text()) * 1
		cmTOmm_proc   = float(self.cmi_LinEd.text()) * 1e+01
		cmTOum_proc   = float(self.cmi_LinEd.text()) * 1e+04
		cmTOangs_proc = float(self.cmi_LinEd.text()) * 1e+06
		# cmTOnm_proc   = float(self.cmi_LinEd.text()) * 1e+07
		cmTOkm_proc   = float(self.cmi_LinEd.text()) * 1e-05
		cmTOin_proc   = float(self.cmi_LinEd.text()) * 3.937008e-01
		cmTOft_proc   = float(self.cmi_LinEd.text()) * 3.280840e-02
		cmTOyd_proc   = float(self.cmi_LinEd.text()) * 1.093613e-02
		cmTOmiST_proc = float(self.cmi_LinEd.text()) * 6.213712e-06
		cmTOmiNV_proc = float(self.cmi_LinEd.text()) * 5.399568e-06

		self.cmTOm_res.setText(str(round(cmTOm_proc,       8)))
		self.cmTOcm_res.setText(str(round(cmTOcm_proc,     8)))
		self.cmTOmm_res.setText(str(round(cmTOmm_proc,     8)))
		self.cmTOum_res.setText(str(round(cmTOum_proc,     8)))
		self.cmTOangs_res.setText(str(round(cmTOangs_proc, 8)))
		self.cmTOnm_res.setText("-")
		self.cmTOkm_res.setText(str(round(cmTOkm_proc,     8)))
		self.cmTOin_res.setText(str(round(cmTOin_proc,     8)))
		self.cmTOft_res.setText(str(round(cmTOft_proc,     8)))
		self.cmTOyd_res.setText(str(round(cmTOyd_proc,     8)))
		self.cmTOmiST_res.setText(str(round(cmTOmiST_proc, 8)))
		self.cmTOmiNV_res.setText(str(round(cmTOmiNV_proc, 8)))

	def mmTO_fun(self):
		mmTOm_proc    = float(self.mmi_LinEd.text()) * 1e-03
		mmTOcm_proc   = float(self.mmi_LinEd.text()) * 1e+01
		mmTOmm_proc   = float(self.mmi_LinEd.text()) * 1
		mmTOum_proc   = float(self.mmi_LinEd.text()) * 1e+03
		mmTOangs_proc = float(self.mmi_LinEd.text()) * 1e+05
		mmTOnm_proc   = float(self.mmi_LinEd.text()) * 1e+06
		mmTOkm_proc   = float(self.mmi_LinEd.text()) * 1e-06
		mmTOin_proc   = float(self.mmi_LinEd.text()) * 3.937008e-02
		mmTOft_proc   = float(self.mmi_LinEd.text()) * 3.280840e-03
		mmTOyd_proc   = float(self.mmi_LinEd.text()) * 1.093613e-03
		# mmTOmiST_proc = float(self.mmi_LinEd.text()) * 6.213712e-07
		# mmTOmiNV_proc = float(self.mmi_LinEd.text()) * 5.399568e-07

		self.mmTOm_res.setText(str(round(mmTOm_proc,       8)))
		self.mmTOcm_res.setText(str(round(mmTOcm_proc,     8)))
		self.mmTOmm_res.setText(str(round(mmTOmm_proc,     8)))
		self.mmTOum_res.setText(str(round(mmTOum_proc,     8)))
		self.mmTOangs_res.setText(str(round(mmTOangs_proc, 8)))
		self.mmTOnm_res.setText(str(round(mmTOnm_proc,     8)))
		self.mmTOkm_res.setText(str(round(mmTOkm_proc,     8)))
		self.mmTOin_res.setText(str(round(mmTOin_proc,     8)))
		self.mmTOft_res.setText(str(round(mmTOft_proc,     8)))
		self.mmTOyd_res.setText(str(round(mmTOyd_proc,     8)))
		self.mmTOmiST_res.setText("-")
		self.mmTOmiNV_res.setText("-")


	def umTO_fun(self):
		umTOm_proc    = float(self.umi_LinEd.text()) * 1e-06
		umTOcm_proc   = float(self.umi_LinEd.text()) * 1e-05
		umTOmm_proc   = float(self.umi_LinEd.text()) * 1e-03
		umTOum_proc   = float(self.umi_LinEd.text()) * 1
		umTOangs_proc = float(self.umi_LinEd.text()) * 1e-02
		umTOnm_proc   = float(self.umi_LinEd.text()) * 1e+03
		# umTOkm_proc   = float(self.umi_LinEd.text()) * 1e-09
		umTOin_proc   = float(self.umi_LinEd.text()) * 3.937008e-05
		umTOft_proc   = float(self.umi_LinEd.text()) * 3.280840e-06
		umTOyd_proc   = float(self.umi_LinEd.text()) * 1.093613e-06
		# umTOmiST_proc = float(self.umi_LinEd.text()) * 6.213712e-10
		# umTOmiNV_proc = float(self.umi_LinEd.text()) * 5.399568e-10

		self.umTOm_res.setText(str(round(umTOm_proc,       8)))
		self.umTOcm_res.setText(str(round(umTOcm_proc,     8)))
		self.umTOmm_res.setText(str(round(umTOmm_proc,     8)))
		self.umTOum_res.setText(str(round(umTOum_proc,     8)))
		self.umTOangs_res.setText(str(round(umTOangs_proc, 8)))
		self.umTOnm_res.setText(str(round(umTOnm_proc,     8)))
		self.umTOkm_res.setText("-")
		self.umTOin_res.setText(str(round(umTOin_proc,     8)))
		self.umTOft_res.setText(str(round(umTOft_proc,     8)))
		self.umTOyd_res.setText(str(round(umTOyd_proc,     8)))
		self.umTOmiST_res.setText("-")
		self.umTOmiNV_res.setText("-")

	def angsTO_fun(self):
		# angsTOm_proc    = float(self.angsi_LinEd.text()) * 1e-08
		# angsTOcm_proc   = float(self.angsi_LinEd.text()) * 1e-06
		angsTOmm_proc   = float(self.angsi_LinEd.text()) * 1e-05
		angsTOum_proc   = float(self.angsi_LinEd.text()) * 1e-02
		angsTOangs_proc = float(self.angsi_LinEd.text()) * 1
		angsTOnm_proc   = float(self.angsi_LinEd.text()) * 1e+01
		# angsTOkm_proc   = float(self.angsi_LinEd.text()) * 1e-11
		# angsTOin_proc   = float(self.angsi_LinEd.text()) * 3.937008e-07
		# angsTOft_proc   = float(self.angsi_LinEd.text()) * 3.280840e-08
		# angsTOyd_proc   = float(self.angsi_LinEd.text()) * 1.093613e-08
		# angsTOmiST_proc = float(self.angsi_LinEd.text()) * 6.213712e-12
		# angsTOmiNV_proc = float(self.angsi_LinEd.text()) * 5.399568e-12

		self.angsTOm_res.setText("-")
		self.angsTOcm_res.setText("-")
		self.angsTOmm_res.setText(str(round(angsTOmm_proc,     8)))
		self.angsTOum_res.setText(str(round(angsTOum_proc,     8)))
		self.angsTOangs_res.setText(str(round(angsTOangs_proc, 8)))
		self.angsTOnm_res.setText(str(round(angsTOnm_proc,     8)))
		self.angsTOkm_res.setText("-")
		self.angsTOin_res.setText("-")
		self.angsTOft_res.setText("-")
		self.angsTOyd_res.setText("-")
		self.angsTOmiST_res.setText("-")
		self.angsTOmiNV_res.setText("-")

	def nmTO_fun(self):
		# nmTOm_proc    = float(self.nmi_LinEd.text()) * 1e-09
		# nmTOcm_proc   = float(self.nmi_LinEd.text()) * 1e-07
		nmTOmm_proc   = float(self.nmi_LinEd.text()) * 1e-06
		nmTOum_proc   = float(self.nmi_LinEd.text()) * 1e-03
		nmTOangs_proc = float(self.nmi_LinEd.text()) * 1e+01
		nmTOnm_proc   = float(self.nmi_LinEd.text()) * 1
		# nmTOkm_proc   = float(self.nmi_LinEd.text()) * 1e-12
		# nmTOin_proc   = float(self.nmi_LinEd.text()) * 3.937008e-08
		# nmTOft_proc   = float(self.nmi_LinEd.text()) * 3.280840e-09
		# nmTOyd_proc   = float(self.nmi_LinEd.text()) * 1.093613e-10
		# nmTOmiST_proc = float(self.nmi_LinEd.text()) * 6.213712e-13
		# nmTOmiNV_proc = float(self.nmi_LinEd.text()) * 5.399568e-13

		self.nmTOm_res.setText("-")
		self.nmTOcm_res.setText("-")
		self.nmTOmm_res.setText(str(round(nmTOmm_proc,     8)))
		self.nmTOum_res.setText(str(round(nmTOum_proc,     8)))
		self.nmTOangs_res.setText(str(round(nmTOangs_proc, 8)))
		self.nmTOnm_res.setText(str(round(nmTOnm_proc,     8)))
		self.nmTOkm_res.setText("-")
		self.nmTOin_res.setText("-")
		self.nmTOft_res.setText("-")
		self.nmTOyd_res.setText("-")
		self.nmTOmiST_res.setText("-")
		self.nmTOmiNV_res.setText("-")

	def kmTO_fun(self):
		kmTOm_proc    = float(self.kmi_LinEd.text()) * 1e-03
		kmTOcm_proc   = float(self.kmi_LinEd.text()) * 1e-05
		kmTOmm_proc   = float(self.kmi_LinEd.text()) * 1e-06
		# kmTOum_proc   = float(self.kmi_LinEd.text()) * 1e-09
		# kmTOangs_proc = float(self.kmi_LinEd.text()) * 1e-011
		# kmTOnm_proc   = float(self.kmi_LinEd.text()) * 1e-012
		kmTOkm_proc   = float(self.kmi_LinEd.text()) * 1
		kmTOin_proc   = float(self.kmi_LinEd.text()) * 3.937008e-02
		kmTOft_proc   = float(self.kmi_LinEd.text()) * 3.280840e-03
		kmTOyd_proc   = float(self.kmi_LinEd.text()) * 1.093613e-03
		kmTOmiST_proc = float(self.kmi_LinEd.text()) * 6.213712e-01
		kmTOmiNV_proc = float(self.kmi_LinEd.text()) * 5.399568e-01

		self.kmTOm_res.setText(str(round(kmTOm_proc,       8)))
		self.kmTOcm_res.setText(str(round(kmTOcm_proc,     8)))
		self.kmTOmm_res.setText(str(round(kmTOmm_proc,     8)))
		self.kmTOum_res.setText("-")
		self.kmTOangs_res.setText("-")
		self.kmTOnm_res.setText("-")
		self.kmTOkm_res.setText(str(round(kmTOkm_proc,     8)))
		self.kmTOin_res.setText(str(round(kmTOin_proc,     8)))
		self.kmTOft_res.setText(str(round(kmTOft_proc,     8)))
		self.kmTOyd_res.setText(str(round(kmTOyd_proc,     8)))
		self.kmTOmiST_res.setText(str(round(kmTOmiST_proc, 8)))
		self.kmTOmiNV_res.setText(str(round(kmTOmiNV_proc, 8)))

	def inTO_fun(self):
		inTOm_proc    = float(self.ini_LinEd.text()) * 2.54e-02
		inTOcm_proc   = float(self.ini_LinEd.text()) * 2.54
		inTOmm_proc   = float(self.ini_LinEd.text()) * 2.54e+01
		inTOum_proc   = float(self.ini_LinEd.text()) * 2.54e+04
		inTOangs_proc = float(self.ini_LinEd.text()) * 2.54e+06
		# inTOnm_proc   = float(self.ini_LinEd.text()) * 2.54e+07
		inTOkm_proc   = float(self.ini_LinEd.text()) * 2.54e-05
		inTOin_proc   = float(self.ini_LinEd.text()) * 1
		inTOft_proc   = float(self.ini_LinEd.text()) * 8.3333333e-02
		inTOyd_proc   = float(self.ini_LinEd.text()) * 2.7777780e-02
		inTOmiST_proc = float(self.ini_LinEd.text()) * 1.5782830e-05
		inTOmiNV_proc = float(self.ini_LinEd.text()) * 1.3714903e-05

		self.inTOm_res.setText(str(round(inTOm_proc,       8)))
		self.inTOcm_res.setText(str(round(inTOcm_proc,     8)))
		self.inTOmm_res.setText(str(round(inTOmm_proc,     8)))
		self.inTOum_res.setText(str(round(inTOum_proc,     8)))
		self.inTOangs_res.setText(str(round(inTOangs_proc, 8)))
		self.inTOnm_res.setText("-")
		self.inTOkm_res.setText(str(round(inTOkm_proc,     8)))
		self.inTOin_res.setText(str(round(inTOin_proc,     8)))
		self.inTOft_res.setText(str(round(inTOft_proc,     8)))
		self.inTOyd_res.setText(str(round(inTOyd_proc,     8)))
		self.inTOmiST_res.setText(str(round(inTOmiST_proc, 8)))
		self.inTOmiNV_res.setText(str(round(inTOmiNV_proc, 8)))

	def ftTO_fun(self):
		ftTOm_proc    = float(self.fti_LinEd.text()) * 3.048e-01
		ftTOcm_proc   = float(self.fti_LinEd.text()) * 3.048e+01
		ftTOmm_proc   = float(self.fti_LinEd.text()) * 3.048e+02
		ftTOum_proc   = float(self.fti_LinEd.text()) * 3.048e+05
		# ftTOangs_proc = float(self.fti_LinEd.text()) * 3.048e+07
		# ftTOnm_proc   = float(self.fti_LinEd.text()) * 3.048e+08
		ftTOkm_proc   = float(self.fti_LinEd.text()) * 3.048e-04
		ftTOin_proc   = float(self.fti_LinEd.text()) * 12
		ftTOft_proc   = float(self.fti_LinEd.text()) * 1
		ftTOyd_proc   = float(self.fti_LinEd.text()) * 3.333333e-01
		ftTOmiST_proc = float(self.fti_LinEd.text()) * 1.893939e-04
		ftTOmiNV_proc = float(self.fti_LinEd.text()) * 1.645788e-04

		self.ftTOm_res.setText(str(round(ftTOm_proc,       8)))
		self.ftTOcm_res.setText(str(round(ftTOcm_proc,     8)))
		self.ftTOmm_res.setText(str(round(ftTOmm_proc,     8)))
		self.ftTOum_res.setText(str(round(ftTOum_proc,     8)))
		self.ftTOangs_res.setText("-")
		self.ftTOnm_res.setText("-")
		self.ftTOkm_res.setText(str(round(ftTOkm_proc,     8)))
		self.ftTOin_res.setText(str(round(ftTOin_proc,     8)))
		self.ftTOft_res.setText(str(round(ftTOft_proc,     8)))
		self.ftTOyd_res.setText(str(round(ftTOyd_proc,     8)))
		self.ftTOmiST_res.setText(str(round(ftTOmiST_proc, 8)))
		self.ftTOmiNV_res.setText(str(round(ftTOmiNV_proc, 8)))

	def ydTO_fun(self):
		ydTOm_proc    = float(self.ydi_LinEd.text()) * 9.144e-01
		ydTOcm_proc   = float(self.ydi_LinEd.text()) * 9.144e+01
		ydTOmm_proc   = float(self.ydi_LinEd.text()) * 9.144e+02
		ydTOum_proc   = float(self.ydi_LinEd.text()) * 9.144e+05
		# ydTOangs_proc = float(self.ydi_LinEd.text()) * 9.144e+07
		# ydTOnm_proc   = float(self.ydi_LinEd.text()) * 9.144e+08
		ydTOkm_proc   = float(self.ydi_LinEd.text()) * 9.144e-04
		ydTOin_proc   = float(self.ydi_LinEd.text()) * 36
		ydTOft_proc   = float(self.ydi_LinEd.text()) * 3
		ydTOyd_proc   = float(self.ydi_LinEd.text()) * 1
		ydTOmiST_proc = float(self.ydi_LinEd.text()) * 5.681818e-04
		ydTOmiNV_proc = float(self.ydi_LinEd.text()) * 4.937365e-04

		self.ydTOm_res.setText(str(round(ydTOm_proc,       8)))
		self.ydTOcm_res.setText(str(round(ydTOcm_proc,     8)))
		self.ydTOmm_res.setText(str(round(ydTOmm_proc,     8)))
		self.ydTOum_res.setText(str(round(ydTOum_proc,     8)))
		self.ydTOangs_res.setText("-")
		self.ydTOnm_res.setText("-")
		self.ydTOkm_res.setText(str(round(ydTOkm_proc,     8)))
		self.ydTOin_res.setText(str(round(ydTOin_proc,     8)))
		self.ydTOft_res.setText(str(round(ydTOft_proc,     8)))
		self.ydTOyd_res.setText(str(round(ydTOyd_proc,     8)))
		self.ydTOmiST_res.setText(str(round(ydTOmiST_proc, 8)))
		self.ydTOmiNV_res.setText(str(round(ydTOmiNV_proc, 8)))

	def miSTTO_fun(self):
		miSTTOm_proc    = float(self.miSTi_LinEd.text()) * 1.609344e+03
		miSTTOcm_proc   = float(self.miSTi_LinEd.text()) * 1.609344e+05
		miSTTOmm_proc   = float(self.miSTi_LinEd.text()) * 1.609344e+06
		# miSTTOum_proc   = float(self.miSTi_LinEd.text()) * 1.609344e+09
		# miSTTOangs_proc = float(self.miSTi_LinEd.text()) * 1.609344e+11
		# miSTTOnm_proc   = float(self.miSTi_LinEd.text()) * 1.609344e+12
		miSTTOkm_proc   = float(self.miSTi_LinEd.text()) * 1.609344
		miSTTOin_proc   = float(self.miSTi_LinEd.text()) * 6.336e+04
		miSTTOft_proc   = float(self.miSTi_LinEd.text()) * 5.280e+03
		miSTTOyd_proc   = float(self.miSTi_LinEd.text()) * 1.760e+03
		miSTTOmiST_proc = float(self.miSTi_LinEd.text()) * 1
		miSTTOmiNV_proc = float(self.miSTi_LinEd.text()) * 8.689762e-01

		self.miSTTOm_res.setText(str(round(miSTTOm_proc,       8)))
		self.miSTTOcm_res.setText(str(round(miSTTOcm_proc,     8)))
		self.miSTTOmm_res.setText(str(round(miSTTOmm_proc,     8)))
		self.miSTTOum_res.setText("-")
		self.miSTTOangs_res.setText("-")
		self.miSTTOnm_res.setText("-")
		self.miSTTOkm_res.setText(str(round(miSTTOkm_proc,     8)))
		self.miSTTOin_res.setText(str(round(miSTTOin_proc,     8)))
		self.miSTTOft_res.setText(str(round(miSTTOft_proc,     8)))
		self.miSTTOyd_res.setText(str(round(miSTTOyd_proc,     8)))
		self.miSTTOmiST_res.setText(str(round(miSTTOmiST_proc, 8)))
		self.miSTTOmiNV_res.setText(str(round(miSTTOmiNV_proc, 8)))

	def miNVTO_fun(self):
		miNVTOm_proc    = float(self.miNVi_LinEd.text()) * 1.852e+03
		miNVTOcm_proc   = float(self.miNVi_LinEd.text()) * 1.852e+05
		miNVTOmm_proc   = float(self.miNVi_LinEd.text()) * 1.852e+06
		# miNVTOum_proc   = float(self.miNVi_LinEd.text()) * 1.852e+09
		# miNVTOangs_proc = float(self.miNVi_LinEd.text()) * 1.852e+11
		# miNVTOnm_proc   = float(self.miNVi_LinEd.text()) * 1.852e+12
		miNVTOkm_proc   = float(self.miNVi_LinEd.text()) * 1.852
		miNVTOin_proc   = float(self.miNVi_LinEd.text()) * 7.29133858e+04
		miNVTOft_proc   = float(self.miNVi_LinEd.text()) * 6.07611549e+03
		miNVTOyd_proc   = float(self.miNVi_LinEd.text()) * 2.02537183e+03
		miNVTOmiST_proc = float(self.miNVi_LinEd.text()) * 1.15077945
		miNVTOmiNV_proc = float(self.miNVi_LinEd.text()) * 1

		self.miNVTOm_res.setText(str(round(miNVTOm_proc,       8)))
		self.miNVTOcm_res.setText(str(round(miNVTOcm_proc,     8)))
		self.miNVTOmm_res.setText(str(round(miNVTOmm_proc,     8)))
		self.miNVTOum_res.setText("-")
		self.miNVTOangs_res.setText("-")
		self.miNVTOnm_res.setText("-")
		self.miNVTOkm_res.setText(str(round(miNVTOkm_proc,     8)))
		self.miNVTOin_res.setText(str(round(miNVTOin_proc,     8)))
		self.miNVTOft_res.setText(str(round(miNVTOft_proc,     8)))
		self.miNVTOyd_res.setText(str(round(miNVTOyd_proc,     8)))
		self.miNVTOmiST_res.setText(str(round(miNVTOmiST_proc, 8)))
		self.miNVTOmiNV_res.setText(str(round(miNVTOmiNV_proc, 8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		# if self.createGroup_input() == QtWidgets.QLabel():
			# pass

		# self.widget = widget("", *args, **kw)
		# if widget == QtWidgets.QLabel():
			# self.widget.setTextInteractionFlags(Qt.TextSelectableByMouse)

		self.setLayout(main_layout)
		self.show()



class Magind_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Magind_Win")

class Magint_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Magint_Win")


class Mass_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Mass Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel           = QtWidgets.QLabel()
		self.kgi_LinEd       = QtWidgets.QLineEdit()
		self.mtoni_LinEd     = QtWidgets.QLineEdit()
		self.ouncei_LinEd    = QtWidgets.QLineEdit()
		self.poundi_LinEd    = QtWidgets.QLineEdit()
		self.shorttoni_LinEd = QtWidgets.QLineEdit()
		self.longtoni_LinEd  = QtWidgets.QLineEdit()

		LinEd_list = [self.kgi_LinEd, self.mtoni_LinEd, self.ouncei_LinEd, self.poundi_LinEd, self.shorttoni_LinEd, self.longtoni_LinEd]

		Label_list = [blanklabel, "kg", "metric ton", "ounce", "pound", "short ton", "long ton"]
		
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

		self.kgi_LinEd.returnPressed.connect(self.kgTO_fun)
		self.mtoni_LinEd.returnPressed.connect(self.mtonTO_fun)
		self.ouncei_LinEd.returnPressed.connect(self.ounceTO_fun)
		self.poundi_LinEd.returnPressed.connect(self.poundTO_fun)
		self.shorttoni_LinEd.returnPressed.connect(self.shorttonTO_fun)
		self.longtoni_LinEd.returnPressed.connect(self.longtonTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["kg", "metric ton", "ounce", "pound", "short ton", "long ton"]
		
		i = 0
		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.kgTOkg_res       = QtWidgets.QLabel("0", self)
		self.kgTOmton_res     = QtWidgets.QLabel("0", self)
		self.kgTOounce_res    = QtWidgets.QLabel("0", self)
		self.kgTOpound_res    = QtWidgets.QLabel("0", self)
		self.kgTOshortton_res = QtWidgets.QLabel("0", self)
		self.kgTOlongton_res  = QtWidgets.QLabel("0", self)

		self.mtonTOkg_res       = QtWidgets.QLabel("0", self)
		self.mtonTOmton_res     = QtWidgets.QLabel("0", self)
		self.mtonTOounce_res    = QtWidgets.QLabel("0", self)
		self.mtonTOpound_res    = QtWidgets.QLabel("0", self)
		self.mtonTOshortton_res = QtWidgets.QLabel("0", self)
		self.mtonTOlongton_res  = QtWidgets.QLabel("0", self)

		self.ounceTOkg_res       = QtWidgets.QLabel("0", self)
		self.ounceTOmton_res     = QtWidgets.QLabel("0", self)
		self.ounceTOounce_res    = QtWidgets.QLabel("0", self)
		self.ounceTOpound_res    = QtWidgets.QLabel("0", self)
		self.ounceTOshortton_res = QtWidgets.QLabel("0", self)
		self.ounceTOlongton_res  = QtWidgets.QLabel("0", self)

		self.poundTOkg_res       = QtWidgets.QLabel("0", self)
		self.poundTOmton_res     = QtWidgets.QLabel("0", self)
		self.poundTOounce_res    = QtWidgets.QLabel("0", self)
		self.poundTOpound_res    = QtWidgets.QLabel("0", self)
		self.poundTOshortton_res = QtWidgets.QLabel("0", self)
		self.poundTOlongton_res  = QtWidgets.QLabel("0", self)

		self.shorttonTOkg_res       = QtWidgets.QLabel("0", self)
		self.shorttonTOmton_res     = QtWidgets.QLabel("0", self)
		self.shorttonTOounce_res    = QtWidgets.QLabel("0", self)
		self.shorttonTOpound_res    = QtWidgets.QLabel("0", self)
		self.shorttonTOshortton_res = QtWidgets.QLabel("0", self)
		self.shorttonTOlongton_res  = QtWidgets.QLabel("0", self)

		self.longtonTOkg_res       = QtWidgets.QLabel("0", self)
		self.longtonTOmton_res     = QtWidgets.QLabel("0", self)
		self.longtonTOounce_res    = QtWidgets.QLabel("0", self)
		self.longtonTOpound_res    = QtWidgets.QLabel("0", self)
		self.longtonTOshortton_res = QtWidgets.QLabel("0", self)
		self.longtonTOlongton_res  = QtWidgets.QLabel("0", self)

		self.kgTO_Label       = [self.kgTOkg_res, self.kgTOmton_res, self.kgTOounce_res, self.kgTOpound_res, self.kgTOshortton_res, self.kgTOlongton_res]

		self.mtonTO_Label     = [self.mtonTOkg_res, self.mtonTOmton_res, self.mtonTOounce_res, self.mtonTOpound_res, self.mtonTOshortton_res, self.mtonTOlongton_res]

		self.ounceTO_Label    = [self.ounceTOkg_res, self.ounceTOmton_res, self.ounceTOounce_res, self.ounceTOpound_res, self.ounceTOshortton_res, self.ounceTOlongton_res]

		self.poundTO_Label    = [self.poundTOkg_res, self.poundTOmton_res, self.poundTOounce_res, self.poundTOpound_res, self.poundTOshortton_res, self.poundTOlongton_res]

		self.shorttonTO_Label = [self.shorttonTOkg_res, self.shorttonTOmton_res, self.shorttonTOounce_res, self.shorttonTOpound_res, self.shorttonTOshortton_res, 
								 self.shorttonTOlongton_res]

		self.longtonTO_Label  = [self.longtonTOkg_res, self.longtonTOmton_res, self.longtonTOounce_res, self.longtonTOpound_res, self.longtonTOshortton_res, 
							 	 self.longtonTOlongton_res]

		i = 0
		for item in self.kgTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.mtonTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in self.ounceTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in self.poundTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in self.shorttonTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1
			
		i = 0
		for item in self.longtonTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def kgTO_fun(self):
		kgTOkg_proc       = float(self.kgi_LinEd.text()) * 1
		kgTOmton_proc     = float(self.kgi_LinEd.text()) * 1e-03
		kgTOounce_proc    = float(self.kgi_LinEd.text()) * 35.27396
		kgTOpound_proc    = float(self.kgi_LinEd.text()) * 2.204623
		kgTOshortton_proc = float(self.kgi_LinEd.text()) * 1.102311e-03
		kgTOlongton_proc  = float(self.kgi_LinEd.text()) * 9.842065e-04

		self.kgTOkg_res.setText(str(round(kgTOkg_proc,             8)))
		self.kgTOmton_res.setText(str(round(kgTOmton_proc,         8)))
		self.kgTOounce_res.setText(str(round(kgTOounce_proc,       8)))
		self.kgTOpound_res.setText(str(round(kgTOpound_proc,       8)))
		self.kgTOshortton_res.setText(str(round(kgTOshortton_proc, 8)))
		self.kgTOlongton_res.setText(str(round(kgTOlongton_proc,   8)))

	def mtonTO_fun(self):
		mtonTOkg_proc       = float(self.mtoni_LinEd.text()) * 1e+03
		mtonTOmton_proc     = float(self.mtoni_LinEd.text()) * 1
		mtonTOounce_proc    = float(self.mtoni_LinEd.text()) * 3.527396e+04
		mtonTOpound_proc    = float(self.mtoni_LinEd.text()) * 2.204623e+03
		mtonTOshortton_proc = float(self.mtoni_LinEd.text()) * 1.102311
		mtonTOlongton_proc  = float(self.mtoni_LinEd.text()) * 0.9842065

		self.mtonTOkg_res.setText(str(round(mtonTOkg_proc,             8)))
		self.mtonTOmton_res.setText(str(round(mtonTOmton_proc,         8)))
		self.mtonTOounce_res.setText(str(round(mtonTOounce_proc,       8)))
		self.mtonTOpound_res.setText(str(round(mtonTOpound_proc,       8)))
		self.mtonTOshortton_res.setText(str(round(mtonTOshortton_proc, 8)))
		self.mtonTOlongton_res.setText(str(round(mtonTOlongton_proc,   8)))

	def ounceTO_fun(self):
		ounceTOkg_proc       = float(self.ouncei_LinEd.text()) * 2.834952e-02
		ounceTOmton_proc     = float(self.ouncei_LinEd.text()) * 2.834950e-05
		ounceTOounce_proc    = float(self.ouncei_LinEd.text()) * 1
		ounceTOpound_proc    = float(self.ouncei_LinEd.text()) * 6.25e-02
		ounceTOshortton_proc = float(self.ouncei_LinEd.text()) * 3.125e-05
		ounceTOlongton_proc  = float(self.ouncei_LinEd.text()) * 2.790179e-05

		self.ounceTOkg_res.setText(str(round(ounceTOkg_proc,             8)))
		self.ounceTOmton_res.setText(str(round(ounceTOmton_proc,         8)))
		self.ounceTOounce_res.setText(str(round(ounceTOounce_proc,       8)))
		self.ounceTOpound_res.setText(str(round(ounceTOpound_proc,       8)))
		self.ounceTOshortton_res.setText(str(round(ounceTOshortton_proc, 8)))
		self.ounceTOlongton_res.setText(str(round(ounceTOlongton_proc,   8)))

	def poundTO_fun(self):
		poundTOkg_proc       = float(self.poundi_LinEd.text()) * 0.4535924
		poundTOmton_proc     = float(self.poundi_LinEd.text()) * 4.535924e-04
		poundTOounce_proc    = float(self.poundi_LinEd.text()) * 16
		poundTOpound_proc    = float(self.poundi_LinEd.text()) * 1
		poundTOshortton_proc = float(self.poundi_LinEd.text()) * 5e-04
		poundTOlongton_proc  = float(self.poundi_LinEd.text()) * 4.464286e-04

		self.poundTOkg_res.setText(str(round(poundTOkg_proc,             8)))
		self.poundTOmton_res.setText(str(round(poundTOmton_proc,         8)))
		self.poundTOounce_res.setText(str(round(poundTOounce_proc,       8)))
		self.poundTOpound_res.setText(str(round(poundTOpound_proc,       8)))
		self.poundTOshortton_res.setText(str(round(poundTOshortton_proc, 8)))
		self.poundTOlongton_res.setText(str(round(poundTOlongton_proc,   8)))

	def shorttonTO_fun(self):
		shorttonTOkg_proc       = float(self.shorttoni_LinEd.text()) * 9.071847e+02
		shorttonTOmton_proc     = float(self.shorttoni_LinEd.text()) * 0.9071847
		shorttonTOounce_proc    = float(self.shorttoni_LinEd.text()) * 3.2e+04
		shorttonTOpound_proc    = float(self.shorttoni_LinEd.text()) * 2e+03
		shorttonTOshortton_proc = float(self.shorttoni_LinEd.text()) * 1
		shorttonTOlongton_proc  = float(self.shorttoni_LinEd.text()) * 0.8928571

		self.shorttonTOkg_res.setText(str(round(shorttonTOkg_proc,             8)))
		self.shorttonTOmton_res.setText(str(round(shorttonTOmton_proc,         8)))
		self.shorttonTOounce_res.setText(str(round(shorttonTOounce_proc,       8)))
		self.shorttonTOpound_res.setText(str(round(shorttonTOpound_proc,       8)))
		self.shorttonTOshortton_res.setText(str(round(shorttonTOshortton_proc, 8)))
		self.shorttonTOlongton_res.setText(str(round(shorttonTOlongton_proc,   8)))

	def longtonTO_fun(self):
		longtonTOkg_proc       = float(self.longtoni_LinEd.text()) * 1.016047e+03
		longtonTOmton_proc     = float(self.longtoni_LinEd.text()) * 1.016047
		longtonTOounce_proc    = float(self.longtoni_LinEd.text()) * 3.584e+04
		longtonTOpound_proc    = float(self.longtoni_LinEd.text()) * 2.24e+03
		longtonTOshortton_proc = float(self.longtoni_LinEd.text()) * 1.12
		longtonTOlongton_proc  = float(self.longtoni_LinEd.text()) * 1

		self.longtonTOkg_res.setText(str(round(longtonTOkg_proc,             8)))
		self.longtonTOmton_res.setText(str(round(longtonTOmton_proc,         8)))
		self.longtonTOounce_res.setText(str(round(longtonTOounce_proc,       8)))
		self.longtonTOpound_res.setText(str(round(longtonTOpound_proc,       8)))
		self.longtonTOshortton_res.setText(str(round(longtonTOshortton_proc, 8)))
		self.longtonTOlongton_res.setText(str(round(longtonTOlongton_proc,   8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Massflow_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Mass Flow Rate Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		Label_list = ["g/sec", "g/min", "kg/sec", "kg/hour", "kg/day", "ton/sec", "ton/hour", "ton/day", "lb/sec", "lb/hour", "lb/day"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

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

		input_grid.addWidget(blanklabel,   0, 0)
		input_grid.addWidget(self.gsi_LinEd,    1, 0)
		input_grid.addWidget(self.gmini_LinEd,  2, 0)
		input_grid.addWidget(self.kgsi_LinEd,   3, 0)
		input_grid.addWidget(self.kghi_LinEd,   4, 0)
		input_grid.addWidget(self.kgdi_LinEd,   5, 0)
		input_grid.addWidget(self.tonsi_LinEd,  6, 0)
		input_grid.addWidget(self.tonhi_LinEd,  7, 0)
		input_grid.addWidget(self.tondi_LinEd,  8, 0)
		input_grid.addWidget(self.lbsi_LinEd,   9, 0)
		input_grid.addWidget(self.lbhi_LinEd,  10, 0)
		input_grid.addWidget(self.lbdi_LinEd,  11, 0)

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
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

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

		output_grid.addWidget(self.gsTOgs_res,   1, 0)
		output_grid.addWidget(self.gsTOgmin_res, 1, 1)
		output_grid.addWidget(self.gsTOkgs_res,  1, 2)
		output_grid.addWidget(self.gsTOkgh_res,  1, 3)
		output_grid.addWidget(self.gsTOkgd_res,  1, 4)
		output_grid.addWidget(self.gsTOtons_res, 1, 5)
		output_grid.addWidget(self.gsTOtonh_res, 1, 6)
		output_grid.addWidget(self.gsTOtond_res, 1, 7)
		output_grid.addWidget(self.gsTOlbs_res,  1, 8)
		output_grid.addWidget(self.gsTOlbh_res,  1, 9)
		output_grid.addWidget(self.gsTOlbd_res,  1, 10)

		output_grid.addWidget(self.gminTOgs_res,   2, 0)
		output_grid.addWidget(self.gminTOgmin_res, 2, 1)
		output_grid.addWidget(self.gminTOkgs_res,  2, 2)
		output_grid.addWidget(self.gminTOkgh_res,  2, 3)
		output_grid.addWidget(self.gminTOkgd_res,  2, 4)
		output_grid.addWidget(self.gminTOtons_res, 2, 5)
		output_grid.addWidget(self.gminTOtonh_res, 2, 6)
		output_grid.addWidget(self.gminTOtond_res, 2, 7)
		output_grid.addWidget(self.gminTOlbs_res,  2, 8)
		output_grid.addWidget(self.gminTOlbh_res,  2, 9)
		output_grid.addWidget(self.gminTOlbd_res,  2, 10)

		output_grid.addWidget(self.kgsTOgs_res,   3, 0)
		output_grid.addWidget(self.kgsTOgmin_res, 3, 1)
		output_grid.addWidget(self.kgsTOkgs_res,  3, 2)
		output_grid.addWidget(self.kgsTOkgh_res,  3, 3)
		output_grid.addWidget(self.kgsTOkgd_res,  3, 4)
		output_grid.addWidget(self.kgsTOtons_res, 3, 5)
		output_grid.addWidget(self.kgsTOtonh_res, 3, 6)
		output_grid.addWidget(self.kgsTOtond_res, 3, 7)
		output_grid.addWidget(self.kgsTOlbs_res,  3, 8)
		output_grid.addWidget(self.kgsTOlbh_res,  3, 9)
		output_grid.addWidget(self.kgsTOlbd_res,  3, 10)

		output_grid.addWidget(self.kghTOgs_res,   4, 0)
		output_grid.addWidget(self.kghTOgmin_res, 4, 1)
		output_grid.addWidget(self.kghTOkgs_res,  4, 2)
		output_grid.addWidget(self.kghTOkgh_res,  4, 3)
		output_grid.addWidget(self.kghTOkgd_res,  4, 4)
		output_grid.addWidget(self.kghTOtons_res, 4, 5)
		output_grid.addWidget(self.kghTOtonh_res, 4, 6)
		output_grid.addWidget(self.kghTOtond_res, 4, 7)
		output_grid.addWidget(self.kghTOlbs_res,  4, 8)
		output_grid.addWidget(self.kghTOlbh_res,  4, 9)
		output_grid.addWidget(self.kghTOlbd_res,  4, 10)

		output_grid.addWidget(self.kgdTOgs_res,   5, 0)
		output_grid.addWidget(self.kgdTOgmin_res, 5, 1)
		output_grid.addWidget(self.kgdTOkgs_res,  5, 2)
		output_grid.addWidget(self.kgdTOkgh_res,  5, 3)
		output_grid.addWidget(self.kgdTOkgd_res,  5, 4)
		output_grid.addWidget(self.kgdTOtons_res, 5, 5)
		output_grid.addWidget(self.kgdTOtonh_res, 5, 6)
		output_grid.addWidget(self.kgdTOtond_res, 5, 7)
		output_grid.addWidget(self.kgdTOlbs_res,  5, 8)
		output_grid.addWidget(self.kgdTOlbh_res,  5, 9)
		output_grid.addWidget(self.kgdTOlbd_res,  5, 10)

		output_grid.addWidget(self.tonsTOgs_res,   6, 0)
		output_grid.addWidget(self.tonsTOgmin_res, 6, 1)
		output_grid.addWidget(self.tonsTOkgs_res,  6, 2)
		output_grid.addWidget(self.tonsTOkgh_res,  6, 3)
		output_grid.addWidget(self.tonsTOkgd_res,  6, 4)
		output_grid.addWidget(self.tonsTOtons_res, 6, 5)
		output_grid.addWidget(self.tonsTOtonh_res, 6, 6)
		output_grid.addWidget(self.tonsTOtond_res, 6, 7)
		output_grid.addWidget(self.tonsTOlbs_res,  6, 8)
		output_grid.addWidget(self.tonsTOlbh_res,  6, 9)
		output_grid.addWidget(self.tonsTOlbd_res,  6, 10)

		output_grid.addWidget(self.tonhTOgs_res,   7, 0)
		output_grid.addWidget(self.tonhTOgmin_res, 7, 1)
		output_grid.addWidget(self.tonhTOkgs_res,  7, 2)
		output_grid.addWidget(self.tonhTOkgh_res,  7, 3)
		output_grid.addWidget(self.tonhTOkgd_res,  7, 4)
		output_grid.addWidget(self.tonhTOtons_res, 7, 5)
		output_grid.addWidget(self.tonhTOtonh_res, 7, 6)
		output_grid.addWidget(self.tonhTOtond_res, 7, 7)
		output_grid.addWidget(self.tonhTOlbs_res,  7, 8)
		output_grid.addWidget(self.tonhTOlbh_res,  7, 9)
		output_grid.addWidget(self.tonhTOlbd_res,  7, 10)

		output_grid.addWidget(self.tondTOgs_res,   8, 0)
		output_grid.addWidget(self.tondTOgmin_res, 8, 1)
		output_grid.addWidget(self.tondTOkgs_res,  8, 2)
		output_grid.addWidget(self.tondTOkgh_res,  8, 3)
		output_grid.addWidget(self.tondTOkgd_res,  8, 4)
		output_grid.addWidget(self.tondTOtons_res, 8, 5)
		output_grid.addWidget(self.tondTOtonh_res, 8, 6)
		output_grid.addWidget(self.tondTOtond_res, 8, 7)
		output_grid.addWidget(self.tondTOlbs_res,  8, 8)
		output_grid.addWidget(self.tondTOlbh_res,  8, 9)
		output_grid.addWidget(self.tondTOlbd_res,  8, 10)

		output_grid.addWidget(self.lbsTOgs_res,   9, 0)
		output_grid.addWidget(self.lbsTOgmin_res, 9, 1)
		output_grid.addWidget(self.lbsTOkgs_res,  9, 2)
		output_grid.addWidget(self.lbsTOkgh_res,  9, 3)
		output_grid.addWidget(self.lbsTOkgd_res,  9, 4)
		output_grid.addWidget(self.lbsTOtons_res, 9, 5)
		output_grid.addWidget(self.lbsTOtonh_res, 9, 6)
		output_grid.addWidget(self.lbsTOtond_res, 9, 7)
		output_grid.addWidget(self.lbsTOlbs_res,  9, 8)
		output_grid.addWidget(self.lbsTOlbh_res,  9, 9)
		output_grid.addWidget(self.lbsTOlbd_res,  9, 10)

		output_grid.addWidget(self.lbhTOgs_res,   10, 0)
		output_grid.addWidget(self.lbhTOgmin_res, 10, 1)
		output_grid.addWidget(self.lbhTOkgs_res,  10, 2)
		output_grid.addWidget(self.lbhTOkgh_res,  10, 3)
		output_grid.addWidget(self.lbhTOkgd_res,  10, 4)
		output_grid.addWidget(self.lbhTOtons_res, 10, 5)
		output_grid.addWidget(self.lbhTOtonh_res, 10, 6)
		output_grid.addWidget(self.lbhTOtond_res, 10, 7)
		output_grid.addWidget(self.lbhTOlbs_res,  10, 8)
		output_grid.addWidget(self.lbhTOlbh_res,  10, 9)
		output_grid.addWidget(self.lbhTOlbd_res,  10, 10)

		output_grid.addWidget(self.lbdTOgs_res,   11, 0)
		output_grid.addWidget(self.lbdTOgmin_res, 11, 1)
		output_grid.addWidget(self.lbdTOkgs_res,  11, 2)
		output_grid.addWidget(self.lbdTOkgh_res,  11, 3)
		output_grid.addWidget(self.lbdTOkgd_res,  11, 4)
		output_grid.addWidget(self.lbdTOtons_res, 11, 5)
		output_grid.addWidget(self.lbdTOtonh_res, 11, 6)
		output_grid.addWidget(self.lbdTOtond_res, 11, 7)
		output_grid.addWidget(self.lbdTOlbs_res,  11, 8)
		output_grid.addWidget(self.lbdTOlbh_res,  11, 9)
		output_grid.addWidget(self.lbdTOlbd_res,  11, 10)

		output_group.setLayout(output_grid)

		return output_group

	def gsTO_fun(self):
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

	def gminTO_fun(self):
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

	def kgsTO_fun(self):
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

	def kghTO_fun(self):
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

	def kgdTO_fun(self):
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

	def tonsTO_fun(self):
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

	def tonhTO_fun(self):
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

	def tondTO_fun(self):
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

	def lbsTO_fun(self):
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

	def lbhTO_fun(self):
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


	def lbdTO_fun(self):
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


	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Massfrac_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Mass Fraction Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel          = QtWidgets.QLabel()
		self.decimali_LinEd = QtWidgets.QLineEdit()
		self.percenti_LinEd = QtWidgets.QLineEdit()
		self.promilei_LinEd = QtWidgets.QLineEdit()
		self.ppmi_LinEd     = QtWidgets.QLineEdit()
		self.ppbi_LinEd     = QtWidgets.QLineEdit()

		Label_list = ["decimal (1)", "%", "‰", "ppm", "ppb"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_grid.addWidget(blanklabel,          0, 0)
		input_grid.addWidget(self.decimali_LinEd, 1, 0)
		input_grid.addWidget(self.percenti_LinEd, 2, 0)
		input_grid.addWidget(self.promilei_LinEd, 3, 0)
		input_grid.addWidget(self.ppmi_LinEd,     4, 0)
		input_grid.addWidget(self.ppbi_LinEd,     5, 0)

		input_group.setLayout(input_grid)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["decimal (1)", "%", "‰", "ppm", "ppb"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.decimalTOdecimal_res = QtWidgets.QLabel("0", self)
		self.decimalTOpercent_res = QtWidgets.QLabel("0", self)
		self.decimalTOpromile_res = QtWidgets.QLabel("0", self)
		self.decimalTOppm_res     = QtWidgets.QLabel("0", self)
		self.decimalTOppb_res     = QtWidgets.QLabel("0", self)

		self.percentTOdecimal_res = QtWidgets.QLabel("0", self)
		self.percentTOpercent_res = QtWidgets.QLabel("0", self)
		self.percentTOpromile_res = QtWidgets.QLabel("0", self)
		self.percentTOppm_res     = QtWidgets.QLabel("0", self)
		self.percentTOppb_res     = QtWidgets.QLabel("0", self)

		self.promileTOdecimal_res = QtWidgets.QLabel("0", self)
		self.promileTOpercent_res = QtWidgets.QLabel("0", self)
		self.promileTOpromile_res = QtWidgets.QLabel("0", self)
		self.promileTOppm_res     = QtWidgets.QLabel("0", self)
		self.promileTOppb_res     = QtWidgets.QLabel("0", self)

		self.ppmTOdecimal_res = QtWidgets.QLabel("0", self)
		self.ppmTOpercent_res = QtWidgets.QLabel("0", self)
		self.ppmTOpromile_res = QtWidgets.QLabel("0", self)
		self.ppmTOppm_res     = QtWidgets.QLabel("0", self)
		self.ppmTOppb_res     = QtWidgets.QLabel("0", self)

		self.ppbTOdecimal_res = QtWidgets.QLabel("0", self)
		self.ppbTOpercent_res = QtWidgets.QLabel("0", self)
		self.ppbTOpromile_res = QtWidgets.QLabel("0", self)
		self.ppbTOppm_res     = QtWidgets.QLabel("0", self)
		self.ppbTOppb_res     = QtWidgets.QLabel("0", self)

		output_grid.addWidget(self.decimalTOdecimal_res, 1, 0)
		output_grid.addWidget(self.decimalTOpercent_res, 1, 1)
		output_grid.addWidget(self.decimalTOpromile_res, 1, 2)
		output_grid.addWidget(self.decimalTOppm_res,     1, 3)
		output_grid.addWidget(self.decimalTOppb_res,     1, 4)

		output_grid.addWidget(self.percentTOdecimal_res, 2, 0)
		output_grid.addWidget(self.percentTOpercent_res, 2, 1)
		output_grid.addWidget(self.percentTOpromile_res, 2, 2)
		output_grid.addWidget(self.percentTOppm_res,     2, 3)
		output_grid.addWidget(self.percentTOppb_res,     2, 4)

		output_grid.addWidget(self.promileTOdecimal_res, 3, 0)
		output_grid.addWidget(self.promileTOpercent_res, 3, 1)
		output_grid.addWidget(self.promileTOpromile_res, 3, 2)
		output_grid.addWidget(self.promileTOppm_res,     3, 3)
		output_grid.addWidget(self.promileTOppb_res,     3, 4)

		output_grid.addWidget(self.ppmTOdecimal_res, 4, 0)
		output_grid.addWidget(self.ppmTOpercent_res, 4, 1)
		output_grid.addWidget(self.ppmTOpromile_res, 4, 2)
		output_grid.addWidget(self.ppmTOppm_res,     4, 3)
		output_grid.addWidget(self.ppmTOppb_res,     4, 4)

		output_grid.addWidget(self.ppbTOdecimal_res, 5, 0)
		output_grid.addWidget(self.ppbTOpercent_res, 5, 1)
		output_grid.addWidget(self.ppbTOpromile_res, 5, 2)
		output_grid.addWidget(self.ppbTOppm_res,     5, 3)
		output_grid.addWidget(self.ppbTOppb_res,     5, 4)

		output_group.setLayout(output_grid)

		self.decimali_LinEd.returnPressed.connect(self.decimalTO_fun)
		self.percenti_LinEd.returnPressed.connect(self.percentTO_fun)
		self.promilei_LinEd.returnPressed.connect(self.promileTO_fun)
		self.ppmi_LinEd.returnPressed.connect(self.ppmTO_fun)
		self.ppbi_LinEd.returnPressed.connect(self.ppbTO_fun)

		return output_group

	def decimalTO_fun(self):
		decimalTOdecimal_proc = float(self.decimali_LinEd.text()) * 1
		decimalTOpercent_proc = float(self.decimali_LinEd.text()) * 1e-02
		decimalTOpromile_proc = float(self.decimali_LinEd.text()) * 1e-03
		decimalTOppm_proc     = float(self.decimali_LinEd.text()) * 1e-06
		decimalTOppb_proc     = float(self.decimali_LinEd.text()) * 1e-09

		self.decimalTOdecimal_res.setText(str(round(decimalTOdecimal_proc, 8)))
		self.decimalTOpercent_res.setText(str(round(decimalTOpercent_proc, 8)))
		self.decimalTOpromile_res.setText(str(round(decimalTOpromile_proc, 8)))
		self.decimalTOppm_res.setText(str(decimalTOppm_proc                  ))
		self.decimalTOppb_res.setText(str(decimalTOppb_proc                  ))

	def percentTO_fun(self):
		percentTOdecimal_proc = float(self.percenti_LinEd.text()) * 1e+02
		percentTOpercent_proc = float(self.percenti_LinEd.text()) * 1
		percentTOpromile_proc = float(self.percenti_LinEd.text()) * 1e-01
		percentTOppm_proc     = float(self.percenti_LinEd.text()) * 1e-04
		percentTOppb_proc     = float(self.percenti_LinEd.text()) * 1e-07

		self.percentTOdecimal_res.setText(str(round(percentTOdecimal_proc, 8)))
		self.percentTOpercent_res.setText(str(round(percentTOpercent_proc, 8)))
		self.percentTOpromile_res.setText(str(round(percentTOpromile_proc, 8)))
		self.percentTOppm_res.setText(str(percentTOppm_proc                  ))
		self.percentTOppb_res.setText(str(percentTOppb_proc                  ))

	def promileTO_fun(self):
		promileTOdecimal_proc = float(self.promilei_LinEd.text()) * 1e+03
		promileTOpercent_proc = float(self.promilei_LinEd.text()) * 1e+01
		promileTOpromile_proc = float(self.promilei_LinEd.text()) * 1
		promileTOppm_proc     = float(self.promilei_LinEd.text()) * 1e-03
		promileTOppb_proc     = float(self.promilei_LinEd.text()) * 1e-06

		self.promileTOdecimal_res.setText(str(round(promileTOdecimal_proc, 8)))
		self.promileTOpercent_res.setText(str(round(promileTOpercent_proc, 8)))
		self.promileTOpromile_res.setText(str(round(promileTOpromile_proc, 8)))
		self.promileTOppm_res.setText(str(round(promileTOppm_proc,         8)))
		self.promileTOppb_res.setText(str(round(promileTOppb_proc,         8)))

	def ppmTO_fun(self):
		ppmTOdecimal_proc = float(self.ppmi_LinEd.text()) * 1e+06
		ppmTOpercent_proc = float(self.ppmi_LinEd.text()) * 1e+04
		ppmTOpromile_proc = float(self.ppmi_LinEd.text()) * 1e+03
		ppmTOppm_proc     = float(self.ppmi_LinEd.text()) * 1
		ppmTOppb_proc     = float(self.ppmi_LinEd.text()) * 1e-03

		self.ppmTOdecimal_res.setText(str(round(ppmTOdecimal_proc, 8)))
		self.ppmTOpercent_res.setText(str(round(ppmTOpercent_proc, 8)))
		self.ppmTOpromile_res.setText(str(round(ppmTOpromile_proc, 8)))
		self.ppmTOppm_res.setText(str(round(ppmTOppm_proc,         8)))
		self.ppmTOppb_res.setText(str(round(ppmTOppb_proc,         8)))

	def ppbTO_fun(self):
		ppbTOdecimal_proc = float(self.ppbi_LinEd.text()) * 1e+09
		ppbTOpercent_proc = float(self.ppbi_LinEd.text()) * 1e+07
		ppbTOpromile_proc = float(self.ppbi_LinEd.text()) * 1e+06
		ppbTOppm_proc     = float(self.ppbi_LinEd.text()) * 1e+03
		ppbTOppb_proc     = float(self.ppbi_LinEd.text()) * 1

		self.ppbTOdecimal_res.setText(str(round(ppbTOdecimal_proc, 8)))
		self.ppbTOpercent_res.setText(str(round(ppbTOpercent_proc, 8)))
		self.ppbTOpromile_res.setText(str(round(ppbTOpromile_proc, 8)))
		self.ppbTOppm_res.setText(str(round(ppbTOppm_proc,         8)))
		self.ppbTOppb_res.setText(str(round(ppbTOppb_proc,         8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Powheatfl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Powheatfl_Win")



class Pressstres_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Pressure Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel          = QtWidgets.QLabel()
		self.Pai_LinEd      = QtWidgets.QLineEdit()
		self.kPai_LinEd     = QtWidgets.QLineEdit()
		self.MPai_LinEd     = QtWidgets.QLineEdit()
		self.mbari_LinEd    = QtWidgets.QLineEdit()
		self.bari_LinEd     = QtWidgets.QLineEdit()
		self.atmi_LinEd     = QtWidgets.QLineEdit()
		self.psii_LinEd     = QtWidgets.QLineEdit()
		self.kgcm2i_LinEd   = QtWidgets.QLineEdit()
		self.kgm2i_LinEd    = QtWidgets.QLineEdit()
		self.Nm2i_LinEd     = QtWidgets.QLineEdit()
		self.lbin2i_LinEd   = QtWidgets.QLineEdit()
		self.lbft2i_LinEd   = QtWidgets.QLineEdit()
		self.Torri_LinEd    = QtWidgets.QLineEdit()
		self.dynecm2i_LinEd = QtWidgets.QLineEdit()
		self.mmH2Oi_LinEd   = QtWidgets.QLineEdit()
		self.mmHgi_LinEd    = QtWidgets.QLineEdit()
		self.inH2Oi_LinEd   = QtWidgets.QLineEdit()
		self.inHgi_LinEd    = QtWidgets.QLineEdit()

		Label_list = ["Pa", "kPa", "MPa", "mbar", "bar", "atm", "psi", "kg/cm\u00B2", "kg/m\u00B2", "N/m\u00B2", "lb/in\u00B2", "lb/ft\u00B2", "Torr", "dyne/cm\u00B2",
					  "mm H<sub>2</sub>O", "mm Hg", "in H<sub>2</sub>O", "in Hg"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_grid.addWidget(blanklabel,           0, 0)
		input_grid.addWidget(self.Pai_LinEd,       1, 0)
		input_grid.addWidget(self.kPai_LinEd,      2, 0)
		input_grid.addWidget(self.MPai_LinEd,      3, 0)
		input_grid.addWidget(self.mbari_LinEd,     4, 0)
		input_grid.addWidget(self.bari_LinEd,      5, 0)
		input_grid.addWidget(self.atmi_LinEd,      6, 0)
		input_grid.addWidget(self.psii_LinEd,      7, 0)
		input_grid.addWidget(self.kgcm2i_LinEd,    8, 0)
		input_grid.addWidget(self.kgm2i_LinEd,     9, 0)
		input_grid.addWidget(self.Nm2i_LinEd,     10, 0)
		input_grid.addWidget(self.lbin2i_LinEd,   11, 0)
		input_grid.addWidget(self.lbft2i_LinEd,   12, 0)
		input_grid.addWidget(self.Torri_LinEd,    13, 0)
		input_grid.addWidget(self.dynecm2i_LinEd, 14, 0)
		input_grid.addWidget(self.mmH2Oi_LinEd,   15, 0)
		input_grid.addWidget(self.mmHgi_LinEd,    16, 0)
		input_grid.addWidget(self.inH2Oi_LinEd,   17, 0)
		input_grid.addWidget(self.inHgi_LinEd,    18, 0)

		input_group.setLayout(input_grid)

		self.Pai_LinEd.returnPressed.connect(self.PaTO_fun)

		return input_group

	def PaTO_fun(self):
		pass

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["Pa", "kPa", "MPa", "mbar", "bar", "atm", "psi", "kg/cm\u00B2", "kg/m\u00B2", "N/m\u00B2", "lb/in\u00B2", "lb/ft\u00B2", "Torr", "dyne/cm\u00B2",
					  "mm H<sub>2</sub>O", "mm Hg", "in H<sub>2</sub>O", "in Hg"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Pressabsg_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressabsg_Win")



class Pressdrl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Pressure Drop per Length Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel           = QtWidgets.QLabel()
		self.Pami_LinEd      = QtWidgets.QLineEdit()
		self.kPa100mi_LinEd  = QtWidgets.QLineEdit()
		self.psifti_LinEd    = QtWidgets.QLineEdit()
		self.psi100fti_LinEd = QtWidgets.QLineEdit()

		Label_list = ["Pa/m", "kPa/100m", "psi/ft", "psi/100ft"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_grid.addWidget(blanklabel,          0, 0)
		input_grid.addWidget(self.Pami_LinEd,     1, 0)
		input_grid.addWidget(self.kPa100mi_LinEd, 2, 0)
		input_grid.addWidget(self.psifti_LinEd,   3, 0)
		input_grid.addWidget(self.psi100ft_LinEd, 4, 0)

		input_group.setLayout(input_grid)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["Pa/m", "kPa/100m", "psi/ft", "psi/100ft"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.PamTOPam_res      = QtWidgets.QLabel("0", self)
		self.PamTOkPa100m_res  = QtWidgets.QLabel("0", self)
		self.PamTOpsift_res    = QtWidgets.QLabel("0", self)
		self.PamTOpsi100ft_res = QtWidgets.QLabel("0", self)

		output_grid.addWidget(self.decimalTOdecimal_res, 1, 0)
		output_grid.addWidget(self.decimalTOpercent_res, 1, 1)
		output_grid.addWidget(self.decimalTOpromile_res, 1, 2)
		output_grid.addWidget(self.decimalTOppm_res,     1, 3)
		output_grid.addWidget(self.decimalTOppb_res,     1, 4)

		output_grid.addWidget(self.percentTOdecimal_res, 2, 0)
		output_grid.addWidget(self.percentTOpercent_res, 2, 1)
		output_grid.addWidget(self.percentTOpromile_res, 2, 2)
		output_grid.addWidget(self.percentTOppm_res,     2, 3)
		output_grid.addWidget(self.percentTOppb_res,     2, 4)

		output_grid.addWidget(self.promileTOdecimal_res, 3, 0)
		output_grid.addWidget(self.promileTOpercent_res, 3, 1)
		output_grid.addWidget(self.promileTOpromile_res, 3, 2)
		output_grid.addWidget(self.promileTOppm_res,     3, 3)
		output_grid.addWidget(self.promileTOppb_res,     3, 4)

		output_grid.addWidget(self.ppmTOdecimal_res, 4, 0)
		output_grid.addWidget(self.ppmTOpercent_res, 4, 1)
		output_grid.addWidget(self.ppmTOpromile_res, 4, 2)
		output_grid.addWidget(self.ppmTOppm_res,     4, 3)
		output_grid.addWidget(self.ppmTOppb_res,     4, 4)

		output_grid.addWidget(self.ppbTOdecimal_res, 5, 0)
		output_grid.addWidget(self.ppbTOpercent_res, 5, 1)
		output_grid.addWidget(self.ppbTOpromile_res, 5, 2)
		output_grid.addWidget(self.ppbTOppm_res,     5, 3)
		output_grid.addWidget(self.ppbTOppb_res,     5, 4)

		output_group.setLayout(output_grid)

		self.decimali_LinEd.returnPressed.connect(self.decimalTO_fun)
		self.percenti_LinEd.returnPressed.connect(self.percentTO_fun)
		self.promilei_LinEd.returnPressed.connect(self.promileTO_fun)
		self.ppmi_LinEd.returnPressed.connect(self.ppmTO_fun)
		self.ppbi_LinEd.returnPressed.connect(self.ppbTO_fun)

		return output_group

	def decimalTO_fun(self):
		decimalTOdecimal_proc = float(self.decimali_LinEd.text()) * 1
		decimalTOpercent_proc = float(self.decimali_LinEd.text()) * 1e-02
		decimalTOpromile_proc = float(self.decimali_LinEd.text()) * 1e-03
		decimalTOppm_proc     = float(self.decimali_LinEd.text()) * 1e-06
		decimalTOppb_proc     = float(self.decimali_LinEd.text()) * 1e-09

		self.decimalTOdecimal_res.setText(str(round(decimalTOdecimal_proc, 8)))
		self.decimalTOpercent_res.setText(str(round(decimalTOpercent_proc, 8)))
		self.decimalTOpromile_res.setText(str(round(decimalTOpromile_proc, 8)))
		self.decimalTOppm_res.setText(str(decimalTOppm_proc                  ))
		self.decimalTOppb_res.setText(str(decimalTOppb_proc                  ))

	def percentTO_fun(self):
		percentTOdecimal_proc = float(self.percenti_LinEd.text()) * 1e+02
		percentTOpercent_proc = float(self.percenti_LinEd.text()) * 1
		percentTOpromile_proc = float(self.percenti_LinEd.text()) * 1e-01
		percentTOppm_proc     = float(self.percenti_LinEd.text()) * 1e-04
		percentTOppb_proc     = float(self.percenti_LinEd.text()) * 1e-07

		self.percentTOdecimal_res.setText(str(round(percentTOdecimal_proc, 8)))
		self.percentTOpercent_res.setText(str(round(percentTOpercent_proc, 8)))
		self.percentTOpromile_res.setText(str(round(percentTOpromile_proc, 8)))
		self.percentTOppm_res.setText(str(percentTOppm_proc                  ))
		self.percentTOppb_res.setText(str(percentTOppb_proc                  ))

	def promileTO_fun(self):
		promileTOdecimal_proc = float(self.promilei_LinEd.text()) * 1e+03
		promileTOpercent_proc = float(self.promilei_LinEd.text()) * 1e+01
		promileTOpromile_proc = float(self.promilei_LinEd.text()) * 1
		promileTOppm_proc     = float(self.promilei_LinEd.text()) * 1e-03
		promileTOppb_proc     = float(self.promilei_LinEd.text()) * 1e-06

		self.promileTOdecimal_res.setText(str(round(promileTOdecimal_proc, 8)))
		self.promileTOpercent_res.setText(str(round(promileTOpercent_proc, 8)))
		self.promileTOpromile_res.setText(str(round(promileTOpromile_proc, 8)))
		self.promileTOppm_res.setText(str(round(promileTOppm_proc,         8)))
		self.promileTOppb_res.setText(str(round(promileTOppb_proc,         8)))

	def ppmTO_fun(self):
		ppmTOdecimal_proc = float(self.ppmi_LinEd.text()) * 1e+06
		ppmTOpercent_proc = float(self.ppmi_LinEd.text()) * 1e+04
		ppmTOpromile_proc = float(self.ppmi_LinEd.text()) * 1e+03
		ppmTOppm_proc     = float(self.ppmi_LinEd.text()) * 1
		ppmTOppb_proc     = float(self.ppmi_LinEd.text()) * 1e-03

		self.ppmTOdecimal_res.setText(str(round(ppmTOdecimal_proc, 8)))
		self.ppmTOpercent_res.setText(str(round(ppmTOpercent_proc, 8)))
		self.ppmTOpromile_res.setText(str(round(ppmTOpromile_proc, 8)))
		self.ppmTOppm_res.setText(str(round(ppmTOppm_proc,         8)))
		self.ppmTOppb_res.setText(str(round(ppmTOppb_proc,         8)))

	def ppbTO_fun(self):
		ppbTOdecimal_proc = float(self.ppbi_LinEd.text()) * 1e+09
		ppbTOpercent_proc = float(self.ppbi_LinEd.text()) * 1e+07
		ppbTOpromile_proc = float(self.ppbi_LinEd.text()) * 1e+06
		ppbTOppm_proc     = float(self.ppbi_LinEd.text()) * 1e+03
		ppbTOppb_proc     = float(self.ppbi_LinEd.text()) * 1

		self.ppbTOdecimal_res.setText(str(round(ppbTOdecimal_proc, 8)))
		self.ppbTOpercent_res.setText(str(round(ppbTOpercent_proc, 8)))
		self.ppbTOpromile_res.setText(str(round(ppbTOpromile_proc, 8)))
		self.ppbTOppm_res.setText(str(round(ppbTOppm_proc,         8)))
		self.ppbTOppb_res.setText(str(round(ppbTOppb_proc,         8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Specener_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Specener_Win")

class Specheatcap_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Specheatcap_Win")

class Surftens_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Surftens_Win")

class Temp_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Temp_Win")

class Dynvis_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Dynvis_Win")

class Kinvis_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Kinvis_Win")



class Veloc_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		
		self.setWindowTitle("Velocity Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)
		
		blanklabel         = QtWidgets.QLabel()
		self.msi_LinEd     = QtWidgets.QLineEdit()
		self.mmini_LinEd   = QtWidgets.QLineEdit()
		self.kmhi_LinEd    = QtWidgets.QLineEdit()
		self.ftsi_LinEd    = QtWidgets.QLineEdit()
		self.ftmini_LinEd  = QtWidgets.QLineEdit()
		self.miSThi_LinEd  = QtWidgets.QLineEdit()
		self.knotUKi_LinEd = QtWidgets.QLineEdit()
		self.knotITi_LinEd = QtWidgets.QLineEdit()

		Label_list = ["m/sec", "m/min", "km/hour", "ft/sec", "ft/min", "mile<sub>statute</sub>/hour", "knot<sub>English</sub>", "knot<sub>internat</sub>"]
		i = 1

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			input_grid.addWidget(Label_name, i, 1)
			i = i + 1

		input_grid.addWidget(blanklabel,         0, 0)
		input_grid.addWidget(self.msi_LinEd,     1, 0)
		input_grid.addWidget(self.mmini_LinEd,   2, 0)
		input_grid.addWidget(self.kmhi_LinEd,    3, 0)
		input_grid.addWidget(self.ftsi_LinEd,    4, 0)
		input_grid.addWidget(self.ftmini_LinEd,  5, 0)
		input_grid.addWidget(self.miSThi_LinEd,  6, 0)
		input_grid.addWidget(self.knotUKi_LinEd, 7, 0)
		input_grid.addWidget(self.knotITi_LinEd, 8, 0)

		input_group.setLayout(input_grid)

		self.msi_LinEd.returnPressed.connect(self.msTO_fun)
		self.mmini_LinEd.returnPressed.connect(self.mminTO_fun)
		self.kmhi_LinEd.returnPressed.connect(self.kmhTO_fun)
		self.ftsi_LinEd.returnPressed.connect(self.ftsTO_fun)
		self.ftmini_LinEd.returnPressed.connect(self.ftminTO_fun)
		self.miSThi_LinEd.returnPressed.connect(self.miSThTO_fun)
		self.knotUKi_LinEd.returnPressed.connect(self.knotUKTO_fun)
		self.knotITi_LinEd.returnPressed.connect(self.knotITTO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["m/sec", "m/min", "km/hour", "ft/sec", "ft/min", "mile<sub>statute</sub>/hour", "knot<sub>English</sub>", "knot<sub>internat</sub>"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.msTOms_res     = QtWidgets.QLabel("0", self)
		self.msTOmmin_res   = QtWidgets.QLabel("0", self)
		self.msTOkmh_res    = QtWidgets.QLabel("0", self)
		self.msTOfts_res    = QtWidgets.QLabel("0", self)
		self.msTOftmin_res  = QtWidgets.QLabel("0", self)
		self.msTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.msTOknotUK_res = QtWidgets.QLabel("0", self)
		self.msTOknotIT_res = QtWidgets.QLabel("0", self)

		self.mminTOms_res     = QtWidgets.QLabel("0", self)
		self.mminTOmmin_res   = QtWidgets.QLabel("0", self)
		self.mminTOkmh_res    = QtWidgets.QLabel("0", self)
		self.mminTOfts_res    = QtWidgets.QLabel("0", self)
		self.mminTOftmin_res  = QtWidgets.QLabel("0", self)
		self.mminTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.mminTOknotUK_res = QtWidgets.QLabel("0", self)
		self.mminTOknotIT_res = QtWidgets.QLabel("0", self)

		self.kmhTOms_res     = QtWidgets.QLabel("0", self)
		self.kmhTOmmin_res   = QtWidgets.QLabel("0", self)
		self.kmhTOkmh_res    = QtWidgets.QLabel("0", self)
		self.kmhTOfts_res    = QtWidgets.QLabel("0", self)
		self.kmhTOftmin_res  = QtWidgets.QLabel("0", self)
		self.kmhTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.kmhTOknotUK_res = QtWidgets.QLabel("0", self)
		self.kmhTOknotIT_res = QtWidgets.QLabel("0", self)

		self.ftsTOms_res     = QtWidgets.QLabel("0", self)
		self.ftsTOmmin_res   = QtWidgets.QLabel("0", self)
		self.ftsTOkmh_res    = QtWidgets.QLabel("0", self)
		self.ftsTOfts_res    = QtWidgets.QLabel("0", self)
		self.ftsTOftmin_res  = QtWidgets.QLabel("0", self)
		self.ftsTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.ftsTOknotUK_res = QtWidgets.QLabel("0", self)
		self.ftsTOknotIT_res = QtWidgets.QLabel("0", self)

		self.ftminTOms_res     = QtWidgets.QLabel("0", self)
		self.ftminTOmmin_res   = QtWidgets.QLabel("0", self)
		self.ftminTOkmh_res    = QtWidgets.QLabel("0", self)
		self.ftminTOfts_res    = QtWidgets.QLabel("0", self)
		self.ftminTOftmin_res  = QtWidgets.QLabel("0", self)
		self.ftminTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.ftminTOknotUK_res = QtWidgets.QLabel("0", self)
		self.ftminTOknotIT_res = QtWidgets.QLabel("0", self)

		self.miSThTOms_res     = QtWidgets.QLabel("0", self)
		self.miSThTOmmin_res   = QtWidgets.QLabel("0", self)
		self.miSThTOkmh_res    = QtWidgets.QLabel("0", self)
		self.miSThTOfts_res    = QtWidgets.QLabel("0", self)
		self.miSThTOftmin_res  = QtWidgets.QLabel("0", self)
		self.miSThTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.miSThTOknotUK_res = QtWidgets.QLabel("0", self)
		self.miSThTOknotIT_res = QtWidgets.QLabel("0", self)

		self.knotUKTOms_res     = QtWidgets.QLabel("0", self)
		self.knotUKTOmmin_res   = QtWidgets.QLabel("0", self)
		self.knotUKTOkmh_res    = QtWidgets.QLabel("0", self)
		self.knotUKTOfts_res    = QtWidgets.QLabel("0", self)
		self.knotUKTOftmin_res  = QtWidgets.QLabel("0", self)
		self.knotUKTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.knotUKTOknotUK_res = QtWidgets.QLabel("0", self)
		self.knotUKTOknotIT_res = QtWidgets.QLabel("0", self)

		self.knotITTOms_res     = QtWidgets.QLabel("0", self)
		self.knotITTOmmin_res   = QtWidgets.QLabel("0", self)
		self.knotITTOkmh_res    = QtWidgets.QLabel("0", self)
		self.knotITTOfts_res    = QtWidgets.QLabel("0", self)
		self.knotITTOftmin_res  = QtWidgets.QLabel("0", self)
		self.knotITTOmiSTh_res  = QtWidgets.QLabel("0", self)
		self.knotITTOknotUK_res = QtWidgets.QLabel("0", self)
		self.knotITTOknotIT_res = QtWidgets.QLabel("0", self)

		output_grid.addWidget(self.msTOms_res,     1, 0)
		output_grid.addWidget(self.msTOmmin_res,   1, 1)
		output_grid.addWidget(self.msTOkmh_res,    1, 2)
		output_grid.addWidget(self.msTOfts_res,    1, 3)
		output_grid.addWidget(self.msTOftmin_res,  1, 4)
		output_grid.addWidget(self.msTOmiSTh_res,  1, 5)
		output_grid.addWidget(self.msTOknotUK_res, 1, 6)
		output_grid.addWidget(self.msTOknotIT_res, 1, 7)

		output_grid.addWidget(self.mminTOms_res,     2, 0)
		output_grid.addWidget(self.mminTOmmin_res,   2, 1)
		output_grid.addWidget(self.mminTOkmh_res,    2, 2)
		output_grid.addWidget(self.mminTOfts_res,    2, 3)
		output_grid.addWidget(self.mminTOftmin_res,  2, 4)
		output_grid.addWidget(self.mminTOmiSTh_res,  2, 5)
		output_grid.addWidget(self.mminTOknotUK_res, 2, 6)
		output_grid.addWidget(self.mminTOknotIT_res, 2, 7)

		output_grid.addWidget(self.kmhTOms_res,     3, 0)
		output_grid.addWidget(self.kmhTOmmin_res,   3, 1)
		output_grid.addWidget(self.kmhTOkmh_res,    3, 2)
		output_grid.addWidget(self.kmhTOfts_res,    3, 3)
		output_grid.addWidget(self.kmhTOftmin_res,  3, 4)
		output_grid.addWidget(self.kmhTOmiSTh_res,  3, 5)
		output_grid.addWidget(self.kmhTOknotUK_res, 3, 6)
		output_grid.addWidget(self.kmhTOknotIT_res, 3, 7)

		output_grid.addWidget(self.ftsTOms_res,     4, 0)
		output_grid.addWidget(self.ftsTOmmin_res,   4, 1)
		output_grid.addWidget(self.ftsTOkmh_res,    4, 2)
		output_grid.addWidget(self.ftsTOfts_res,    4, 3)
		output_grid.addWidget(self.ftsTOftmin_res,  4, 4)
		output_grid.addWidget(self.ftsTOmiSTh_res,  4, 5)
		output_grid.addWidget(self.ftsTOknotUK_res, 4, 6)
		output_grid.addWidget(self.ftsTOknotIT_res, 4, 7)

		output_grid.addWidget(self.ftminTOms_res,     5, 0)
		output_grid.addWidget(self.ftminTOmmin_res,   5, 1)
		output_grid.addWidget(self.ftminTOkmh_res,    5, 2)
		output_grid.addWidget(self.ftminTOfts_res,    5, 3)
		output_grid.addWidget(self.ftminTOftmin_res,  5, 4)
		output_grid.addWidget(self.ftminTOmiSTh_res,  5, 5)
		output_grid.addWidget(self.ftminTOknotUK_res, 5, 6)
		output_grid.addWidget(self.ftminTOknotIT_res, 5, 7)

		output_grid.addWidget(self.miSThTOms_res,     6, 0)
		output_grid.addWidget(self.miSThTOmmin_res,   6, 1)
		output_grid.addWidget(self.miSThTOkmh_res,    6, 2)
		output_grid.addWidget(self.miSThTOfts_res,    6, 3)
		output_grid.addWidget(self.miSThTOftmin_res,  6, 4)
		output_grid.addWidget(self.miSThTOmiSTh_res,  6, 5)
		output_grid.addWidget(self.miSThTOknotUK_res, 6, 6)
		output_grid.addWidget(self.miSThTOknotIT_res, 6, 7)

		output_grid.addWidget(self.knotUKTOms_res,     7, 0)
		output_grid.addWidget(self.knotUKTOmmin_res,   7, 1)
		output_grid.addWidget(self.knotUKTOkmh_res,    7, 2)
		output_grid.addWidget(self.knotUKTOfts_res,    7, 3)
		output_grid.addWidget(self.knotUKTOftmin_res,  7, 4)
		output_grid.addWidget(self.knotUKTOmiSTh_res,  7, 5)
		output_grid.addWidget(self.knotUKTOknotUK_res, 7, 6)
		output_grid.addWidget(self.knotUKTOknotIT_res, 7, 7)

		output_grid.addWidget(self.knotITTOms_res,     8, 0)
		output_grid.addWidget(self.knotITTOmmin_res,   8, 1)
		output_grid.addWidget(self.knotITTOkmh_res,    8, 2)
		output_grid.addWidget(self.knotITTOfts_res,    8, 3)
		output_grid.addWidget(self.knotITTOftmin_res,  8, 4)
		output_grid.addWidget(self.knotITTOmiSTh_res,  8, 5)
		output_grid.addWidget(self.knotITTOknotUK_res, 8, 6)
		output_grid.addWidget(self.knotITTOknotIT_res, 8, 7)

		output_group.setLayout(output_grid)

		return output_group

	def msTO_fun(self):
		msTOms_proc     = float(self.msi_LinEd.text()) * 1
		msTOmmin_proc   = float(self.msi_LinEd.text()) * 60
		msTOkmh_proc    = float(self.msi_LinEd.text()) * 3.6
		msTOfts_proc    = float(self.msi_LinEd.text()) * 3.280840
		msTOftmin_proc  = float(self.msi_LinEd.text()) * 196.8504
		msTOmiSTh_proc  = float(self.msi_LinEd.text()) * 2.236936
		msTOknotUK_proc = float(self.msi_LinEd.text()) * 1.942604
		msTOknotIT_proc = float(self.msi_LinEd.text()) * 1.943844

		msTOms_res.setText(str(round(msTOms_proc,         8)))
		msTOmmin_res.setText(str(round(msTOmmin_proc,     8)))
		msTOkmh_res.setText(str(round(msTOkmh_proc,       8)))
		msTOfts_res.setText(str(round(msTOfts_proc,       8)))
		msTOftmin_res.setText(str(round(msTOftmin_proc,   8)))
		msTOmiSTh_res.setText(str(round(msTOmiSTh_proc,   8)))
		msTOknotUK_res.setText(str(round(msTOknotUK_proc, 8)))
		msTOknotIT_res.setText(str(round(msTOknotIT_proc, 8)))

	def mminTO_fun(self):
		mminTOms_proc     = float(self.mmini_LinEd.text()) / 60
		mminTOmmin_proc   = float(self.mmini_LinEd.text()) * 1
		mminTOkmh_proc    = float(self.mmini_LinEd.text()) * 0.06
		mminTOfts_proc    = float(self.mmini_LinEd.text()) * 0.05468066
		mminTOftmin_proc  = float(self.mmini_LinEd.text()) * 3.28084000
		mminTOmiSTh_proc  = float(self.mmini_LinEd.text()) * 0.03728227
		mminTOknotUK_proc = float(self.mmini_LinEd.text()) * 1.942604 / 60
		mminTOknotIT_proc = float(self.mmini_LinEd.text()) * 1.943844 / 60

		mminTOms_res.setText(str(round(mminTOms_proc,         8)))
		mminTOmmin_res.setText(str(round(mminTOmmin_proc,     8)))
		mminTOkmh_res.setText(str(round(mminTOkmh_proc,       8)))
		mminTOfts_res.setText(str(round(mminTOfts_proc,       8)))
		mminTOftmin_res.setText(str(round(mminTOftmin_proc,   8)))
		mminTOmiSTh_res.setText(str(round(mminTOmiSTh_proc,   8)))
		mminTOknotUK_res.setText(str(round(mminTOknotUK_proc, 8)))
		mminTOknotIT_res.setText(str(round(mminTOknotIT_proc, 8)))

	def kmhTO_fun(self):
		kmhTOms_proc     = float(self.kmhi_LinEd.text()) / 3.6
		kmhTOmmin_proc   = float(self.kmhi_LinEd.text()) * 50 / 3
		kmhTOkmh_proc    = float(self.kmhi_LinEd.text()) * 1
		kmhTOfts_proc    = float(self.kmhi_LinEd.text()) * 0.9113444
		kmhTOftmin_proc  = float(self.kmhi_LinEd.text()) * 54.68066
		kmhTOmiSTh_proc  = float(self.kmhi_LinEd.text()) * 0.6213712
		kmhTOknotUK_proc = float(self.kmhi_LinEd.text()) * 0.5396122
		kmhTOknotIT_proc = float(self.kmhi_LinEd.text()) * 0.5399573

		kmhTOms_res.setText(str(round(kmhTOms_proc,         8)))
		kmhTOmmin_res.setText(str(round(kmhTOmmin_proc,     8)))
		kmhTOkmh_res.setText(str(round(kmhTOkmh_proc,       8)))
		kmhTOfts_res.setText(str(round(kmhTOfts_proc,       8)))
		kmhTOftmin_res.setText(str(round(kmhTOftmin_proc,   8)))
		kmhTOmiSTh_res.setText(str(round(kmhTOmiSTh_proc,   8)))
		kmhTOknotUK_res.setText(str(round(kmhTOknotUK_proc, 8)))
		kmhTOknotIT_res.setText(str(round(kmhTOknotIT_proc, 8)))

	def ftsTO_fun(self):
		ftsTOms_proc     = float(self.ftsi_LinEd.text()) * 0.3048
		ftsTOmmin_proc   = float(self.ftsi_LinEd.text()) * 18.288
		ftsTOkmh_proc    = float(self.ftsi_LinEd.text()) * 1.09728
		ftsTOfts_proc    = float(self.ftsi_LinEd.text()) * 1
		ftsTOftmin_proc  = float(self.ftsi_LinEd.text()) * 60
		ftsTOmiSTh_proc  = float(self.ftsi_LinEd.text()) * 0.6818182
		ftsTOknotUK_proc = float(self.ftsi_LinEd.text()) * 0.5921056
		ftsTOknotIT_proc = float(self.ftsi_LinEd.text()) * 0.5924843

		ftsTOms_res.setText(str(round(ftsTOms_proc,         8)))
		ftsTOmmin_res.setText(str(round(ftsTOmmin_proc,     8)))
		ftsTOkmh_res.setText(str(round(ftsTOkmh_proc,       8)))
		ftsTOfts_res.setText(str(round(ftsTOfts_proc,       8)))
		ftsTOftmin_res.setText(str(round(ftsTOftmin_proc,   8)))
		ftsTOmiSTh_res.setText(str(round(ftsTOmiSTh_proc,   8)))
		ftsTOknotUK_res.setText(str(round(ftsTOknotUK_proc, 8)))
		ftsTOknotIT_res.setText(str(round(ftsTOknotIT_proc, 8)))

	def ftminTO_fun(self):
		ftminTOms_proc     = float(self.ftmini_LinEd.text()) * 5.8e-03
		ftminTOmmin_proc   = float(self.ftmini_LinEd.text()) * 0.3048
		ftminTOkmh_proc    = float(self.ftmini_LinEd.text()) * 1.8288e-02
		ftminTOfts_proc    = float(self.ftmini_LinEd.text()) / 60
		ftminTOftmin_proc  = float(self.ftmini_LinEd.text()) * 1
		ftminTOmiSTh_proc  = float(self.ftmini_LinEd.text()) * 1.136364e-02
		ftminTOknotUK_proc = float(self.ftmini_LinEd.text()) * 0.5921056 / 60
		ftminTOknotIT_proc = float(self.ftmini_LinEd.text()) * 0.5924843 / 60

		ftminTOms_res.setText(str(round(ftminTOms_proc,         8)))
		ftminTOmmin_res.setText(str(round(ftminTOmmin_proc,     8)))
		ftminTOkmh_res.setText(str(round(ftminTOkmh_proc,       8)))
		ftminTOfts_res.setText(str(round(ftminTOfts_proc,       8)))
		ftminTOftmin_res.setText(str(round(ftminTOftmin_proc,   8)))
		ftminTOmiSTh_res.setText(str(round(ftminTOmiSTh_proc,   8)))
		ftminTOknotUK_res.setText(str(round(ftminTOknotUK_proc, 8)))
		ftminTOknotIT_res.setText(str(round(ftminTOknotIT_proc, 8)))

	def miSThTO_fun(self):
		miSThTOms_proc     = float(self.miSThi_LinEd.text()) * 0.44704
		miSThTOmmin_proc   = float(self.miSThi_LinEd.text()) * 26.8224
		miSThTOkmh_proc    = float(self.miSThi_LinEd.text()) * 1.609344
		miSThTOfts_proc    = float(self.miSThi_LinEd.text()) * 1.466667
		miSThTOftmin_proc  = float(self.miSThi_LinEd.text()) * 88
		miSThTOmiSTh_proc  = float(self.miSThi_LinEd.text()) * 1
		miSThTOknotUK_proc = float(self.miSThi_LinEd.text()) * 0.8684216
		miSThTOknotIT_proc = float(self.miSThi_LinEd.text()) * 0.868977

		miSThTOms_res.setText(str(round(miSThTOms_proc,         8)))
		miSThTOmmin_res.setText(str(round(miSThTOmmin_proc,     8)))
		miSThTOkmh_res.setText(str(round(miSThTOkmh_proc,       8)))
		miSThTOfts_res.setText(str(round(miSThTOfts_proc,       8)))
		miSThTOftmin_res.setText(str(round(miSThTOftmin_proc,   8)))
		miSThTOmiSTh_res.setText(str(round(miSThTOmiSTh_proc,   8)))
		miSThTOknotUK_res.setText(str(round(miSThTOknotUK_proc, 8)))
		miSThTOknotIT_res.setText(str(round(miSThTOknotIT_proc, 8)))

	def knotUKTO_fun(self):
		knotUKTOms_proc     = float(self.knotUKi_LinEd.text()) * 0.5147730
		knotUKTOmmin_proc   = float(self.knotUKi_LinEd.text()) * 0.5147730 * 60
		knotUKTOkmh_proc    = float(self.knotUKi_LinEd.text()) * 0.5147730 * 3.6
		knotUKTOfts_proc    = float(self.knotUKi_LinEd.text()) * 1.6888878
		knotUKTOftmin_proc  = float(self.knotUKi_LinEd.text()) * 1.6888878 * 60
		knotUKTOmiSTh_proc  = float(self.knotUKi_LinEd.text()) * 1.1515144
		knotUKTOknotUK_proc = float(self.knotUKi_LinEd.text()) * 1
		knotUKTOknotIT_proc = float(self.knotUKi_LinEd.text()) * 1.0006395

		knotUKTOms_res.setText(str(round(knotUKTOms_proc,         8)))
		knotUKTOmmin_res.setText(str(round(knotUKTOmmin_proc,     8)))
		knotUKTOkmh_res.setText(str(round(knotUKTOkmh_proc,       8)))
		knotUKTOfts_res.setText(str(round(knotUKTOfts_proc,       8)))
		knotUKTOftmin_res.setText(str(round(knotUKTOftmin_proc,   8)))
		knotUKTOmiSTh_res.setText(str(round(knotUKTOmiSTh_proc,   8)))
		knotUKTOknotUK_res.setText(str(round(knotUKTOknotUK_proc, 8)))
		knotUKTOknotIT_res.setText(str(round(knotUKTOknotIT_proc, 8)))

	def knotITTO_fun(self):
		knotITTOms_proc     = float(self.knotITi_LinEd.text()) * 0.5144440
		knotITTOmmin_proc   = float(self.knotITi_LinEd.text()) * 0.5144440 * 60
		knotITTOkmh_proc    = float(self.knotITi_LinEd.text()) * 0.5144440 * 3.6
		knotITTOfts_proc    = float(self.knotITi_LinEd.text()) * 1.6878084
		knotITTOftmin_proc  = float(self.knotITi_LinEd.text()) * 1.6878084 * 60
		knotITTOmiSTh_proc  = float(self.knotITi_LinEd.text()) * 1.1507785
		knotITTOknotUK_proc = float(self.knotITi_LinEd.text()) * 0.9993609
		knotITTOknotIT_proc = float(self.knotITi_LinEd.text()) * 1

		knotITTOms_res.setText(str(round(knotITTOms_proc,         8)))
		knotITTOmmin_res.setText(str(round(knotITTOmmin_proc,     8)))
		knotITTOkmh_res.setText(str(round(knotITTOkmh_proc,       8)))
		knotITTOfts_res.setText(str(round(knotITTOfts_proc,       8)))
		knotITTOftmin_res.setText(str(round(knotITTOftmin_proc,   8)))
		knotITTOmiSTh_res.setText(str(round(knotITTOmiSTh_proc,   8)))
		knotITTOknotUK_res.setText(str(round(knotITTOknotUK_proc, 8)))
		knotITTOknotIT_res.setText(str(round(knotITTOknotIT_proc, 8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Vol_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		
		self.setWindowTitle("Volumetric Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
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
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

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

	def dm3TO_fun(self):
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

	def cm3TO_fun(self):
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

	def in3TO_fun(self):
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

	def ft3TO_fun(self):
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

	def yd3TO_fun(self):
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

	def galUSTO_fun(self):
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

	def galUKTO_fun(self):
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

	def barrTO_fun(self):
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

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()



class Volflow_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Volflow_Win")

class Weight_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Weight_Win")



aplikace = QtWidgets.QApplication(sys.argv)
okno = MainWindow()
okno.show()
sys.exit(aplikace.exec_())

