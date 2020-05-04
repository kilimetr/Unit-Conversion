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
		self.massflow_pb    = QtWidgets.QPushButton("Mass Flow Rate",                    self)
		self.massfrac_pb    = QtWidgets.QPushButton("Mass Fraction",                     self)

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
		vbox1.addWidget(self.massflow_pb)
		vbox1.addWidget(self.massfrac_pb)
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
		self.massflow_pb.clicked.connect(self.massflow_win)
		self.massfrac_pb.clicked.connect(self.massfrac_win)

		return groupBox_1

	def createGroup_2(self):
		groupBox_2 = QtWidgets.QGroupBox()

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

		m2u_Label    = QtWidgets.QLabel("m\u00B2")
		cm2u_Label   = QtWidgets.QLabel("cm\u00B2")
		mm2u_Label   = QtWidgets.QLabel("mm\u00B2")
		au_Label     = QtWidgets.QLabel("a")
		hau_Label    = QtWidgets.QLabel("ha")
		in2u_Label   = QtWidgets.QLabel("in\u00B2")
		ft2u_Label   = QtWidgets.QLabel("ft\u00B2")
		yd2u_Label   = QtWidgets.QLabel("yard\u00B2")
		acru_Label   = QtWidgets.QLabel("acr")
		mi2STu_Label = QtWidgets.QLabel("mile\u00B2<sub>statute</sub>")

		input_grid.addWidget(blanklabel,         0, 0)
		input_grid.addWidget(self.m2i_LinEd,     1, 0)
		input_grid.addWidget(self.cm2i_LinEd,    2, 0)
		input_grid.addWidget(self.mm2i_LinEd,    3, 0)
		input_grid.addWidget(self.ai_LinEd,      4, 0)
		input_grid.addWidget(self.hai_LinEd,     5, 0)
		input_grid.addWidget(self.in2i_LinEd,    6, 0)
		input_grid.addWidget(self.ft2i_LinEd,    7, 0)
		input_grid.addWidget(self.yd2i_LinEd,    8, 0)
		input_grid.addWidget(self.acri_LinEd,    9, 0)
		input_grid.addWidget(self.mi2STi_LinEd, 10, 0)

		input_grid.addWidget(m2u_Label,     1, 1)
		input_grid.addWidget(cm2u_Label,    2, 1)
		input_grid.addWidget(mm2u_Label,    3, 1)
		input_grid.addWidget(au_Label,      4, 1)
		input_grid.addWidget(hau_Label,     5, 1)
		input_grid.addWidget(in2u_Label,    6, 1)
		input_grid.addWidget(ft2u_Label,    7, 1)
		input_grid.addWidget(yd2u_Label,    8, 1)
		input_grid.addWidget(acru_Label,    9, 1)
		input_grid.addWidget(mi2STu_Label, 10, 1)

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

		m2_Label    = QtWidgets.QLabel("m\u00B2")
		cm2_Label   = QtWidgets.QLabel("cm\u00B2")
		mm2_Label   = QtWidgets.QLabel("mm\u00B2")
		a_Label     = QtWidgets.QLabel("a")
		ha_Label    = QtWidgets.QLabel("ha")
		in2_Label   = QtWidgets.QLabel("in\u00B2")
		ft2_Label   = QtWidgets.QLabel("ft\u00B2")
		yd2_Label   = QtWidgets.QLabel("yard\u00B2")
		acr_Label   = QtWidgets.QLabel("acr")
		mi2ST_Label = QtWidgets.QLabel("mile\u00B2<sub>statute</sub>")

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

		# self.m2TOm2_res.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

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

		# self.widget = widget("", *args, **kw)
		# if widget == QtWidgets.QLabel():
			# self.widget.setTextInteractionFlags(Qt.TextSelectableByMouse)

		output_grid.addWidget(m2_Label,    0, 0)
		output_grid.addWidget(cm2_Label,   0, 1)
		output_grid.addWidget(mm2_Label,   0, 2)
		output_grid.addWidget(a_Label,     0, 3)
		output_grid.addWidget(ha_Label,    0, 4)
		output_grid.addWidget(in2_Label,   0, 5)
		output_grid.addWidget(ft2_Label,   0, 6)
		output_grid.addWidget(yd2_Label,   0, 7)
		output_grid.addWidget(acr_Label,   0, 8)
		output_grid.addWidget(mi2ST_Label, 0, 9)

		output_grid.addWidget(self.m2TOm2_res,    1, 0)
		output_grid.addWidget(self.m2TOcm2_res,   1, 1)
		output_grid.addWidget(self.m2TOmm2_res,   1, 2)
		output_grid.addWidget(self.m2TOa_res,     1, 3)
		output_grid.addWidget(self.m2TOha_res,    1, 4)
		output_grid.addWidget(self.m2TOin2_res,   1, 5)
		output_grid.addWidget(self.m2TOft2_res,   1, 6)
		output_grid.addWidget(self.m2TOyd2_res,   1, 7)
		output_grid.addWidget(self.m2TOacr_res,   1, 8)
		output_grid.addWidget(self.m2TOmi2ST_res, 1, 9)

		output_grid.addWidget(self.cm2TOm2_res,    2, 0)
		output_grid.addWidget(self.cm2TOcm2_res,   2, 1)
		output_grid.addWidget(self.cm2TOmm2_res,   2, 2)
		output_grid.addWidget(self.cm2TOa_res,     2, 3)
		output_grid.addWidget(self.cm2TOha_res,    2, 4)
		output_grid.addWidget(self.cm2TOin2_res,   2, 5)
		output_grid.addWidget(self.cm2TOft2_res,   2, 6)
		output_grid.addWidget(self.cm2TOyd2_res,   2, 7)
		output_grid.addWidget(self.cm2TOacr_res,   2, 8)
		output_grid.addWidget(self.cm2TOmi2ST_res, 2, 9)

		output_grid.addWidget(self.mm2TOm2_res,    3, 0)
		output_grid.addWidget(self.mm2TOcm2_res,   3, 1)
		output_grid.addWidget(self.mm2TOmm2_res,   3, 2)
		output_grid.addWidget(self.mm2TOa_res,     3, 3)
		output_grid.addWidget(self.mm2TOha_res,    3, 4)
		output_grid.addWidget(self.mm2TOin2_res,   3, 5)
		output_grid.addWidget(self.mm2TOft2_res,   3, 6)
		output_grid.addWidget(self.mm2TOyd2_res,   3, 7)
		output_grid.addWidget(self.mm2TOacr_res,   3, 8)
		output_grid.addWidget(self.mm2TOmi2ST_res, 3, 9)

		output_grid.addWidget(self.aTOm2_res,    4, 0)
		output_grid.addWidget(self.aTOcm2_res,   4, 1)
		output_grid.addWidget(self.aTOmm2_res,   4, 2)
		output_grid.addWidget(self.aTOa_res,     4, 3)
		output_grid.addWidget(self.aTOha_res,    4, 4)
		output_grid.addWidget(self.aTOin2_res,   4, 5)
		output_grid.addWidget(self.aTOft2_res,   4, 6)
		output_grid.addWidget(self.aTOyd2_res,   4, 7)
		output_grid.addWidget(self.aTOacr_res,   4, 8)
		output_grid.addWidget(self.aTOmi2ST_res, 4, 9)

		output_grid.addWidget(self.haTOm2_res,    5, 0)
		output_grid.addWidget(self.haTOcm2_res,   5, 1)
		output_grid.addWidget(self.haTOmm2_res,   5, 2)
		output_grid.addWidget(self.haTOa_res,     5, 3)
		output_grid.addWidget(self.haTOha_res,    5, 4)
		output_grid.addWidget(self.haTOin2_res,   5, 5)
		output_grid.addWidget(self.haTOft2_res,   5, 6)
		output_grid.addWidget(self.haTOyd2_res,   5, 7)
		output_grid.addWidget(self.haTOacr_res,   5, 8)
		output_grid.addWidget(self.haTOmi2ST_res, 5, 9)

		output_grid.addWidget(self.in2TOm2_res,    6, 0)
		output_grid.addWidget(self.in2TOcm2_res,   6, 1)
		output_grid.addWidget(self.in2TOmm2_res,   6, 2)
		output_grid.addWidget(self.in2TOa_res,     6, 3)
		output_grid.addWidget(self.in2TOha_res,    6, 4)
		output_grid.addWidget(self.in2TOin2_res,   6, 5)
		output_grid.addWidget(self.in2TOft2_res,   6, 6)
		output_grid.addWidget(self.in2TOyd2_res,   6, 7)
		output_grid.addWidget(self.in2TOacr_res,   6, 8)
		output_grid.addWidget(self.in2TOmi2ST_res, 6, 9)

		output_grid.addWidget(self.ft2TOm2_res,    7, 0)
		output_grid.addWidget(self.ft2TOcm2_res,   7, 1)
		output_grid.addWidget(self.ft2TOmm2_res,   7, 2)
		output_grid.addWidget(self.ft2TOa_res,     7, 3)
		output_grid.addWidget(self.ft2TOha_res,    7, 4)
		output_grid.addWidget(self.ft2TOin2_res,   7, 5)
		output_grid.addWidget(self.ft2TOft2_res,   7, 6)
		output_grid.addWidget(self.ft2TOyd2_res,   7, 7)
		output_grid.addWidget(self.ft2TOacr_res,   7, 8)
		output_grid.addWidget(self.ft2TOmi2ST_res, 7, 9)

		output_grid.addWidget(self.yd2TOm2_res,    8, 0)
		output_grid.addWidget(self.yd2TOcm2_res,   8, 1)
		output_grid.addWidget(self.yd2TOmm2_res,   8, 2)
		output_grid.addWidget(self.yd2TOa_res,     8, 3)
		output_grid.addWidget(self.yd2TOha_res,    8, 4)
		output_grid.addWidget(self.yd2TOin2_res,   8, 5)
		output_grid.addWidget(self.yd2TOft2_res,   8, 6)
		output_grid.addWidget(self.yd2TOyd2_res,   8, 7)
		output_grid.addWidget(self.yd2TOacr_res,   8, 8)
		output_grid.addWidget(self.yd2TOmi2ST_res, 8, 9)

		output_grid.addWidget(self.acrTOm2_res,    9, 0)
		output_grid.addWidget(self.acrTOcm2_res,   9, 1)
		output_grid.addWidget(self.acrTOmm2_res,   9, 2)
		output_grid.addWidget(self.acrTOa_res,     9, 3)
		output_grid.addWidget(self.acrTOha_res,    9, 4)
		output_grid.addWidget(self.acrTOin2_res,   9, 5)
		output_grid.addWidget(self.acrTOft2_res,   9, 6)
		output_grid.addWidget(self.acrTOyd2_res,   9, 7)
		output_grid.addWidget(self.acrTOacr_res,   9, 8)
		output_grid.addWidget(self.acrTOmi2ST_res, 9, 9)

		output_grid.addWidget(self.mi2STTOm2_res,    10, 0)
		output_grid.addWidget(self.mi2STTOcm2_res,   10, 1)
		output_grid.addWidget(self.mi2STTOmm2_res,   10, 2)
		output_grid.addWidget(self.mi2STTOa_res,     10, 3)
		output_grid.addWidget(self.mi2STTOha_res,    10, 4)
		output_grid.addWidget(self.mi2STTOin2_res,   10, 5)
		output_grid.addWidget(self.mi2STTOft2_res,   10, 6)
		output_grid.addWidget(self.mi2STTOyd2_res,   10, 7)
		output_grid.addWidget(self.mi2STTOacr_res,   10, 8)
		output_grid.addWidget(self.mi2STTOmi2ST_res, 10, 9)

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
		
		blanklabel              = QtWidgets.QLabel(self)
		self.BTUft3i_LinEd      = QtWidgets.QLineEdit()
		self.BTUgalUKi_LinEd    = QtWidgets.QLineEdit()
		self.BTUgalUSi_LinEd    = QtWidgets.QLineEdit()
		self.kJm3i_LinEd	    = QtWidgets.QLineEdit()
		self.kWhm3i_LinEd	    = QtWidgets.QLineEdit()
		self.MJm3_kJdm3i_LinEd	= QtWidgets.QLineEdit()

		BTUft3u_Label  = QtWidgets.QLabel("BTU/ft\u00B3")
		BTUgalUKu_Label = QtWidgets.QLabel("BTU/gal<sub>UK</sub>")
		BTUgalUSu_Label = QtWidgets.QLabel("BTU/gal<sub>US</sub>")
		kJm3u_Label   = QtWidgets.QLabel("kJ/m\u00B3")
		kWhm3u_Label  = QtWidgets.QLabel("kWh/m\u00B3")
		MJm3_kJdm3u_Label = QtWidgets.QLabel("MJ/m\u00B3 & kJ/dm\u00B3")

		input_grid.addWidget(blanklabel, 0, 0)
		input_grid.addWidget(self.BTUft3i_LinEd,  1, 0)
		input_grid.addWidget(self.BTUgalUKi_LinEd, 2, 0)
		input_grid.addWidget(self.BTUgalUSi_LinEd, 3, 0)
		input_grid.addWidget(self.kJm3i_LinEd,   4, 0)
		input_grid.addWidget(self.kWhm3i_LinEd,  5, 0)
		input_grid.addWidget(self.MJm3_kJdm3i_LinEd,  6, 0)

		input_grid.addWidget(BTUft3u_Label,  1, 1)
		input_grid.addWidget(BTUgalUKu_Label, 2, 1)
		input_grid.addWidget(BTUgalUSu_Label, 3, 1)
		input_grid.addWidget(kJm3u_Label,   4, 1)
		input_grid.addWidget(kWhm3u_Label,  5, 1)
		input_grid.addWidget(MJm3_kJdm3u_Label, 6, 1)

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

		BTUft3_Label  = QtWidgets.QLabel("BTU/ft\u00B3")
		BTUgalUK_Label = QtWidgets.QLabel("BTU/gal<sub>UK</sub>")
		BTUgalUS_Label = QtWidgets.QLabel("BTU/gal<sub>US</sub>")
		kJm3_Label   = QtWidgets.QLabel("kJ/m\u00B3")
		kWhm3_Label  = QtWidgets.QLabel("kWh/m\u00B3")
		MJm3_kJdm3_Label = QtWidgets.QLabel("MJ/m\u00B3 & kJ/dm\u00B3")

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

		output_grid.addWidget(BTUft3_Label,     0, 0)
		output_grid.addWidget(BTUgalUK_Label,   0, 1)
		output_grid.addWidget(BTUgalUS_Label,   0, 2)
		output_grid.addWidget(kJm3_Label,       0, 3)
		output_grid.addWidget(kWhm3_Label,      0, 4)
		output_grid.addWidget(MJm3_kJdm3_Label, 0, 5)

		output_grid.addWidget(self.BTUft3TOBTUft3_res,     1, 0)
		output_grid.addWidget(self.BTUft3TOBTUgalUK_res,   1, 1)
		output_grid.addWidget(self.BTUft3TOBTUgalUS_res,   1, 2)
		output_grid.addWidget(self.BTUft3TOkJm3_res,       1, 3)
		output_grid.addWidget(self.BTUft3TOkWhm3_res,      1, 4)
		output_grid.addWidget(self.BTUft3TOMJm3_kJdm3_res, 1, 5)

		output_grid.addWidget(self.BTUgalUKTOBTUft3_res,     2, 0)
		output_grid.addWidget(self.BTUgalUKTOBTUgalUK_res,   2, 1)
		output_grid.addWidget(self.BTUgalUKTOBTUgalUS_res,   2, 2)
		output_grid.addWidget(self.BTUgalUKTOkJm3_res,       2, 3)
		output_grid.addWidget(self.BTUgalUKTOkWhm3_res,      2, 4)
		output_grid.addWidget(self.BTUgalUKTOMJm3_kJdm3_res, 2, 5)

		output_grid.addWidget(self.BTUgalUSTOBTUft3_res,     3, 0)
		output_grid.addWidget(self.BTUgalUSTOBTUgalUK_res,   3, 1)
		output_grid.addWidget(self.BTUgalUSTOBTUgalUS_res,   3, 2)
		output_grid.addWidget(self.BTUgalUSTOkJm3_res,       3, 3)
		output_grid.addWidget(self.BTUgalUSTOkWhm3_res,      3, 4)
		output_grid.addWidget(self.BTUgalUSTOMJm3_kJdm3_res, 3, 5)

		output_grid.addWidget(self.kJm3TOBTUft3_res,     4, 0)
		output_grid.addWidget(self.kJm3TOBTUgalUK_res,   4, 1)
		output_grid.addWidget(self.kJm3TOBTUgalUS_res,   4, 2)
		output_grid.addWidget(self.kJm3TOkJm3_res,       4, 3)
		output_grid.addWidget(self.kJm3TOkWhm3_res,      4, 4)
		output_grid.addWidget(self.kJm3TOMJm3_kJdm3_res, 4, 5)

		output_grid.addWidget(self.kWhm3TOBTUft3_res,     5, 0)
		output_grid.addWidget(self.kWhm3TOBTUgalUK_res,   5, 1)
		output_grid.addWidget(self.kWhm3TOBTUgalUS_res,   5, 2)
		output_grid.addWidget(self.kWhm3TOkJm3_res,       5, 3)
		output_grid.addWidget(self.kWhm3TOkWhm3_res,      5, 4)
		output_grid.addWidget(self.kWhm3TOMJm3_kJdm3_res, 5, 5)

		output_grid.addWidget(self.MJm3_kJdm3TOBTUft3_res,     6, 0)
		output_grid.addWidget(self.MJm3_kJdm3TOBTUgalUK_res,   6, 1)
		output_grid.addWidget(self.MJm3_kJdm3TOBTUgalUS_res,   6, 2)
		output_grid.addWidget(self.MJm3_kJdm3TOkJm3_res,       6, 3)
		output_grid.addWidget(self.MJm3_kJdm3TOkWhm3_res,      6, 4)
		output_grid.addWidget(self.MJm3_kJdm3TOMJm3_kJdm3_res, 6, 5)

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

		blanklabel        = QtWidgets.QLabel()
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

		mu_Label    = QtWidgets.QLabel("m")
		cmu_Label   = QtWidgets.QLabel("cm")
		mmu_Label   = QtWidgets.QLabel("mm")
		umu_Label   = QtWidgets.QLabel("\u03BCm & micron")
		angsu_Label = QtWidgets.QLabel("Å")
		nmu_Label   = QtWidgets.QLabel("nm")
		kmu_Label   = QtWidgets.QLabel("km")
		inu_Label   = QtWidgets.QLabel("in")
		ftu_Label   = QtWidgets.QLabel("ft")
		ydu_Label   = QtWidgets.QLabel("yard")
		miSTu_Label = QtWidgets.QLabel("mile<sub>statute</sub>")
		miNVu_Label = QtWidgets.QLabel("mile<sub>navy</sub>")

		input_grid.addWidget(blanklabel,        0, 0)
		input_grid.addWidget(self.mi_LinEd,     1, 0)
		input_grid.addWidget(self.cmi_LinEd,    2, 0)
		input_grid.addWidget(self.mmi_LinEd,    3, 0)
		input_grid.addWidget(self.umi_LinEd,    4, 0)
		input_grid.addWidget(self.angsi_LinEd,  5, 0)
		input_grid.addWidget(self.nmi_LinEd,    6, 0)
		input_grid.addWidget(self.kmi_LinEd,    7, 0)
		input_grid.addWidget(self.ini_LinEd,    8, 0)
		input_grid.addWidget(self.fti_LinEd,    9, 0)
		input_grid.addWidget(self.ydi_LinEd,   10, 0)
		input_grid.addWidget(self.miSTi_LinEd, 11, 0)
		input_grid.addWidget(self.miNVi_LinEd, 12, 0)

		input_grid.addWidget(mu_Label,     1, 1)
		input_grid.addWidget(cmu_Label,    2, 1)
		input_grid.addWidget(mmu_Label,    3, 1)
		input_grid.addWidget(umu_Label,    4, 1)
		input_grid.addWidget(angsu_Label,  5, 1)
		input_grid.addWidget(nmu_Label,    6, 1)
		input_grid.addWidget(kmu_Label,    7, 1)
		input_grid.addWidget(inu_Label,    8, 1)
		input_grid.addWidget(ftu_Label,    9, 1)
		input_grid.addWidget(ydu_Label,   10, 1)
		input_grid.addWidget(miSTu_Label, 11, 1)
		input_grid.addWidget(miNVu_Label, 12, 1)

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

		m_Label    = QtWidgets.QLabel("m")
		cm_Label   = QtWidgets.QLabel("cm")
		mm_Label   = QtWidgets.QLabel("mm")
		um_Label   = QtWidgets.QLabel("\u03BCm & micron")
		angs_Label = QtWidgets.QLabel("Å")
		nm_Label   = QtWidgets.QLabel("nm")
		km_Label   = QtWidgets.QLabel("km")
		in_Label   = QtWidgets.QLabel("in")
		ft_Label   = QtWidgets.QLabel("ft")
		yd_Label   = QtWidgets.QLabel("yard")
		miST_Label = QtWidgets.QLabel("mile<sub>statute</sub>")
		miNV_Label = QtWidgets.QLabel("mile<sub>navy</sub>")

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

		output_grid.addWidget(m_Label,    0,  0)
		output_grid.addWidget(cm_Label,   0,  1)
		output_grid.addWidget(mm_Label,   0,  2)
		output_grid.addWidget(um_Label,   0,  3)
		output_grid.addWidget(angs_Label, 0,  4)
		output_grid.addWidget(nm_Label,   0,  5)
		output_grid.addWidget(km_Label,   0,  6)
		output_grid.addWidget(in_Label,   0,  7)
		output_grid.addWidget(ft_Label,   0,  8)
		output_grid.addWidget(yd_Label,   0,  9)
		output_grid.addWidget(miST_Label, 0, 10)
		output_grid.addWidget(miNV_Label, 0, 11)

		output_grid.addWidget(self.mTOm_res,    1,  0)
		output_grid.addWidget(self.mTOcm_res,   1,  1)
		output_grid.addWidget(self.mTOmm_res,   1,  2)
		output_grid.addWidget(self.mTOum_res,   1,  3)
		output_grid.addWidget(self.mTOangs_res, 1,  4)
		output_grid.addWidget(self.mTOnm_res,   1,  5)
		output_grid.addWidget(self.mTOkm_res,   1,  6)
		output_grid.addWidget(self.mTOin_res,   1,  7)
		output_grid.addWidget(self.mTOft_res,   1,  8)
		output_grid.addWidget(self.mTOyd_res,   1,  9)
		output_grid.addWidget(self.mTOmiST_res, 1, 10)
		output_grid.addWidget(self.mTOmiNV_res, 1, 11)

		output_grid.addWidget(self.cmTOm_res,    2,  0)
		output_grid.addWidget(self.cmTOcm_res,   2,  1)
		output_grid.addWidget(self.cmTOmm_res,   2,  2)
		output_grid.addWidget(self.cmTOum_res,   2,  3)
		output_grid.addWidget(self.cmTOangs_res, 2,  4)
		output_grid.addWidget(self.cmTOnm_res,   2,  5)
		output_grid.addWidget(self.cmTOkm_res,   2,  6)
		output_grid.addWidget(self.cmTOin_res,   2,  7)
		output_grid.addWidget(self.cmTOft_res,   2,  8)
		output_grid.addWidget(self.cmTOyd_res,   2,  9)
		output_grid.addWidget(self.cmTOmiST_res, 2, 10)
		output_grid.addWidget(self.cmTOmiNV_res, 2, 11)

		output_grid.addWidget(self.mmTOm_res,    3,  0)
		output_grid.addWidget(self.mmTOcm_res,   3,  1)
		output_grid.addWidget(self.mmTOmm_res,   3,  2)
		output_grid.addWidget(self.mmTOum_res,   3,  3)
		output_grid.addWidget(self.mmTOangs_res, 3,  4)
		output_grid.addWidget(self.mmTOnm_res,   3,  5)
		output_grid.addWidget(self.mmTOkm_res,   3,  6)
		output_grid.addWidget(self.mmTOin_res,   3,  7)
		output_grid.addWidget(self.mmTOft_res,   3,  8)
		output_grid.addWidget(self.mmTOyd_res,   3,  9)
		output_grid.addWidget(self.mmTOmiST_res, 3, 10)
		output_grid.addWidget(self.mmTOmiNV_res, 3, 11)

		output_grid.addWidget(self.umTOm_res,    4,  0)
		output_grid.addWidget(self.umTOcm_res,   4,  1)
		output_grid.addWidget(self.umTOmm_res,   4,  2)
		output_grid.addWidget(self.umTOum_res,   4,  3)
		output_grid.addWidget(self.umTOangs_res, 4,  4)
		output_grid.addWidget(self.umTOnm_res,   4,  5)
		output_grid.addWidget(self.umTOkm_res,   4,  6)
		output_grid.addWidget(self.umTOin_res,   4,  7)
		output_grid.addWidget(self.umTOft_res,   4,  8)
		output_grid.addWidget(self.umTOyd_res,   4,  9)
		output_grid.addWidget(self.umTOmiST_res, 4, 10)
		output_grid.addWidget(self.umTOmiNV_res, 4, 11)

		output_grid.addWidget(self.angsTOm_res,    5,  0)
		output_grid.addWidget(self.angsTOcm_res,   5,  1)
		output_grid.addWidget(self.angsTOmm_res,   5,  2)
		output_grid.addWidget(self.angsTOum_res,   5,  3)
		output_grid.addWidget(self.angsTOangs_res, 5,  4)
		output_grid.addWidget(self.angsTOnm_res,   5,  5)
		output_grid.addWidget(self.angsTOkm_res,   5,  6)
		output_grid.addWidget(self.angsTOin_res,   5,  7)
		output_grid.addWidget(self.angsTOft_res,   5,  8)
		output_grid.addWidget(self.angsTOyd_res,   5,  9)
		output_grid.addWidget(self.angsTOmiST_res, 5, 10)
		output_grid.addWidget(self.angsTOmiNV_res, 5, 11)

		output_grid.addWidget(self.nmTOm_res,    6,  0)
		output_grid.addWidget(self.nmTOcm_res,   6,  1)
		output_grid.addWidget(self.nmTOmm_res,   6,  2)
		output_grid.addWidget(self.nmTOum_res,   6,  3)
		output_grid.addWidget(self.nmTOangs_res, 6,  4)
		output_grid.addWidget(self.nmTOnm_res,   6,  5)
		output_grid.addWidget(self.nmTOkm_res,   6,  6)
		output_grid.addWidget(self.nmTOin_res,   6,  7)
		output_grid.addWidget(self.nmTOft_res,   6,  8)
		output_grid.addWidget(self.nmTOyd_res,   6,  9)
		output_grid.addWidget(self.nmTOmiST_res, 6, 10)
		output_grid.addWidget(self.nmTOmiNV_res, 6, 11)

		output_grid.addWidget(self.kmTOm_res,    7,  0)
		output_grid.addWidget(self.kmTOcm_res,   7,  1)
		output_grid.addWidget(self.kmTOmm_res,   7,  2)
		output_grid.addWidget(self.kmTOum_res,   7,  3)
		output_grid.addWidget(self.kmTOangs_res, 7,  4)
		output_grid.addWidget(self.kmTOnm_res,   7,  5)
		output_grid.addWidget(self.kmTOkm_res,   7,  6)
		output_grid.addWidget(self.kmTOin_res,   7,  7)
		output_grid.addWidget(self.kmTOft_res,   7,  8)
		output_grid.addWidget(self.kmTOyd_res,   7,  9)
		output_grid.addWidget(self.kmTOmiST_res, 7, 10)
		output_grid.addWidget(self.kmTOmiNV_res, 7, 11)

		output_grid.addWidget(self.inTOm_res,    8,  0)
		output_grid.addWidget(self.inTOcm_res,   8,  1)
		output_grid.addWidget(self.inTOmm_res,   8,  2)
		output_grid.addWidget(self.inTOum_res,   8,  3)
		output_grid.addWidget(self.inTOangs_res, 8,  4)
		output_grid.addWidget(self.inTOnm_res,   8,  5)
		output_grid.addWidget(self.inTOkm_res,   8,  6)
		output_grid.addWidget(self.inTOin_res,   8,  7)
		output_grid.addWidget(self.inTOft_res,   8,  8)
		output_grid.addWidget(self.inTOyd_res,   8,  9)
		output_grid.addWidget(self.inTOmiST_res, 8, 10)
		output_grid.addWidget(self.inTOmiNV_res, 8, 11)

		output_grid.addWidget(self.ftTOm_res,    9,  0)
		output_grid.addWidget(self.ftTOcm_res,   9,  1)
		output_grid.addWidget(self.ftTOmm_res,   9,  2)
		output_grid.addWidget(self.ftTOum_res,   9,  3)
		output_grid.addWidget(self.ftTOangs_res, 9,  4)
		output_grid.addWidget(self.ftTOnm_res,   9,  5)
		output_grid.addWidget(self.ftTOkm_res,   9,  6)
		output_grid.addWidget(self.ftTOin_res,   9,  7)
		output_grid.addWidget(self.ftTOft_res,   9,  8)
		output_grid.addWidget(self.ftTOyd_res,   9,  9)
		output_grid.addWidget(self.ftTOmiST_res, 9, 10)
		output_grid.addWidget(self.ftTOmiNV_res, 9, 11)

		output_grid.addWidget(self.ydTOm_res,    10,  0)
		output_grid.addWidget(self.ydTOcm_res,   10,  1)
		output_grid.addWidget(self.ydTOmm_res,   10,  2)
		output_grid.addWidget(self.ydTOum_res,   10,  3)
		output_grid.addWidget(self.ydTOangs_res, 10,  4)
		output_grid.addWidget(self.ydTOnm_res,   10,  5)
		output_grid.addWidget(self.ydTOkm_res,   10,  6)
		output_grid.addWidget(self.ydTOin_res,   10,  7)
		output_grid.addWidget(self.ydTOft_res,   10,  8)
		output_grid.addWidget(self.ydTOyd_res,   10,  9)
		output_grid.addWidget(self.ydTOmiST_res, 10, 10)
		output_grid.addWidget(self.ydTOmiNV_res, 10, 11)

		output_grid.addWidget(self.miSTTOm_res,    11,  0)
		output_grid.addWidget(self.miSTTOcm_res,   11,  1)
		output_grid.addWidget(self.miSTTOmm_res,   11,  2)
		output_grid.addWidget(self.miSTTOum_res,   11,  3)
		output_grid.addWidget(self.miSTTOangs_res, 11,  4)
		output_grid.addWidget(self.miSTTOnm_res,   11,  5)
		output_grid.addWidget(self.miSTTOkm_res,   11,  6)
		output_grid.addWidget(self.miSTTOin_res,   11,  7)
		output_grid.addWidget(self.miSTTOft_res,   11,  8)
		output_grid.addWidget(self.miSTTOyd_res,   11,  9)
		output_grid.addWidget(self.miSTTOmiST_res, 11, 10)
		output_grid.addWidget(self.miSTTOmiNV_res, 11, 11)

		output_grid.addWidget(self.miNVTOm_res,    12,  0)
		output_grid.addWidget(self.miNVTOcm_res,   12,  1)
		output_grid.addWidget(self.miNVTOmm_res,   12,  2)
		output_grid.addWidget(self.miNVTOum_res,   12,  3)
		output_grid.addWidget(self.miNVTOangs_res, 12,  4)
		output_grid.addWidget(self.miNVTOnm_res,   12,  5)
		output_grid.addWidget(self.miNVTOkm_res,   12,  6)
		output_grid.addWidget(self.miNVTOin_res,   12,  7)
		output_grid.addWidget(self.miNVTOft_res,   12,  8)
		output_grid.addWidget(self.miNVTOyd_res,   12,  9)
		output_grid.addWidget(self.miNVTOmiST_res, 12, 10)
		output_grid.addWidget(self.miNVTOmiNV_res, 12, 11)

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

class Massflow_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Massflow_Win")

class Massfrac_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Massfrac_Win")

class Powheatfl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Powheatfl_Win")

class Pressstres_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressstres_Win")

class Pressabsg_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressabsg_Win")

class Pressdrl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressdrl_Win")

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

		msu_Label     = QtWidgets.QLabel("m/sec")
		mminu_Label   = QtWidgets.QLabel("m/min")
		kmhu_Label    = QtWidgets.QLabel("km/hour")
		ftsu_Label    = QtWidgets.QLabel("ft/sec")
		ftminu_Label  = QtWidgets.QLabel("ft/min")
		miSThu_Label  = QtWidgets.QLabel("mile<sub>statute</sub>/hour")
		knotUKu_Label = QtWidgets.QLabel("knot<sub>English</sub>")
		knotITu_Label = QtWidgets.QLabel("knot<sub>internat.</sub>")

		input_grid.addWidget(blanklabel,         0, 0)
		input_grid.addWidget(self.msi_LinEd,     1, 0)
		input_grid.addWidget(self.mmini_LinEd,   2, 0)
		input_grid.addWidget(self.kmhi_LinEd,    3, 0)
		input_grid.addWidget(self.ftsi_LinEd,    4, 0)
		input_grid.addWidget(self.ftmini_LinEd,  5, 0)
		input_grid.addWidget(self.miSThi_LinEd,  6, 0)
		input_grid.addWidget(self.knotUKi_LinEd, 7, 0)
		input_grid.addWidget(self.knotITi_LinEd, 8, 0)

		input_grid.addWidget(msu_Label,     1, 1)
		input_grid.addWidget(mminu_Label,   2, 1)
		input_grid.addWidget(kmhu_Label,    3, 1)
		input_grid.addWidget(ftsu_Label,    4, 1)
		input_grid.addWidget(ftminu_Label,  5, 1)
		input_grid.addWidget(miSThu_Label,  6, 1)
		input_grid.addWidget(knotUKu_Label, 7, 1)
		input_grid.addWidget(knotITu_Label, 8, 1)

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

		ms_Label     = QtWidgets.QLabel("m/sec")
		mmin_Label   = QtWidgets.QLabel("m/min")
		kmh_Label    = QtWidgets.QLabel("km/hour")
		fts_Label    = QtWidgets.QLabel("ft/sec")
		ftmin_Label  = QtWidgets.QLabel("ft/min")
		miST_Label   = QtWidgets.QLabel("mile<sub>statute</sub>")
		knotUK_Label = QtWidgets.QLabel("knot<sub>English</sub>")
		knotIT_Label = QtWidgets.QLabel("knot<sub>internat</sub>")

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

		output_grid.addWidget(ms_Label,     0, 0)
		output_grid.addWidget(mmin_Label,   0, 1)
		output_grid.addWidget(kmh_Label,    0, 2)
		output_grid.addWidget(fts_Label,    0, 3)
		output_grid.addWidget(ftmin_Label,  0, 4)
		output_grid.addWidget(miSThu_Label, 0, 5)
		output_grid.addWidget(knotUK_Label, 0, 6)
		output_grid.addWidget(knotIT_Label, 0, 7)

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

		m3u_Label    = QtWidgets.QLabel("m\u00B3")
		dm3u_Label   = QtWidgets.QLabel("dm\u00B3 & l")
		cm3u_Label   = QtWidgets.QLabel("cm\u00B3 & ml")
		in3u_Label   = QtWidgets.QLabel("in\u00B3")
		ft3u_Label   = QtWidgets.QLabel("ft\u00B3")
		yd3u_Label   = QtWidgets.QLabel("yard\u00B3")
		galUSu_Label = QtWidgets.QLabel("gal<sub>US</sub>")
		galUKu_Label = QtWidgets.QLabel("gal<sub>UK</sub>")
		barru_Label  = QtWidgets.QLabel("barrel<sub>oil, US</sub>")

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

		input_grid.addWidget(m3u_Label,    1, 1)
		input_grid.addWidget(dm3u_Label,   2, 1)
		input_grid.addWidget(cm3u_Label,   3, 1)
		input_grid.addWidget(in3u_Label,   4, 1)
		input_grid.addWidget(ft3u_Label,   5, 1)
		input_grid.addWidget(yd3u_Label,   6, 1)
		input_grid.addWidget(galUSu_Label, 7, 1)
		input_grid.addWidget(galUKu_Label, 8, 1)
		input_grid.addWidget(barru_Label,  9, 1)

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

		m3_Label    = QtWidgets.QLabel("m\u00B3")
		dm3_Label   = QtWidgets.QLabel("dm\u00B3 & l")
		cm3_Label   = QtWidgets.QLabel("cm\u00B3 & ml")
		in3_Label   = QtWidgets.QLabel("in\u00B3")
		ft3_Label   = QtWidgets.QLabel("ft\u00B3")
		yd3_Label   = QtWidgets.QLabel("yard\u00B3")
		galUS_Label = QtWidgets.QLabel("gal<sub>US</sub>")
		galUK_Label = QtWidgets.QLabel("gal<sub>UK</sub>")
		barr_Label = QtWidgets.QLabel("barrel<sub>oil, US</sub>")

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

		output_grid.addWidget(m3_Label,    0, 0)
		output_grid.addWidget(dm3_Label,   0, 1)
		output_grid.addWidget(cm3_Label,   0, 2)
		output_grid.addWidget(in3_Label,   0, 3)
		output_grid.addWidget(ft3_Label,   0, 4)
		output_grid.addWidget(yd3_Label,   0, 5)
		output_grid.addWidget(galUS_Label, 0, 6)
		output_grid.addWidget(galUK_Label, 0, 7)
		output_grid.addWidget(barr_Label,  0, 8)

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

