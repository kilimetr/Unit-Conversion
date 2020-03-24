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
		self.heatval_pb     = QtWidgets.QPushButton("Heat Value",                        self)
		self.dens_pb        = QtWidgets.QPushButton("Density",                           self)
		self.heatfldens_pb  = QtWidgets.QPushButton("Heat Flow Rate Density",            self)
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
		self.setWindowTitle("Area_Win")

class Heatval_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatval_Win")

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
		self.setWindowTitle("Energy_Win")

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
		self.setWindowTitle("Length_Win")

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
		self.setWindowTitle("Veloc_Win")

class Vol_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Vol_Win")

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

