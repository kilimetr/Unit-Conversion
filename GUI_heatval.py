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

		vbox1 = QtWidgets.QVBoxLayout()
		vbox1.addWidget(self.area_pb)
		vbox1.addWidget(self.heatval_pb)
		vbox1.addStretch()
		groupBox_1.setLayout(vbox1)

		self.area_pb.clicked.connect(self.area_win)
		self.heatval_pb.clicked.connect(self.heatval_win)

		return groupBox_1

	def createGroup_2(self):
		groupBox_2 = QtWidgets.QGroupBox()

		self.powheatfl_pb   = QtWidgets.QPushButton("Power & Heat Flow Rate",            self)
		self.pressstres_pb  = QtWidgets.QPushButton("Pressure & Stress",                 self)

		vbox2 = QtWidgets.QVBoxLayout()
		vbox2.addWidget(self.powheatfl_pb)
		vbox2.addWidget(self.pressstres_pb)
		vbox2.addStretch()
		groupBox_2.setLayout(vbox2)

		self.powheatfl_pb.clicked.connect(self.powheatfl_win)
		self.pressstres_pb.clicked.connect(self.pressstres_win)

		return groupBox_2

	def main_window(self):
		grid = QtWidgets.QGridLayout()
		grid.addWidget(self.createGroup_1(), 0, 0)
		grid.addWidget(self.createGroup_2(), 0, 1)
		self.setLayout(grid)
		self.show()

	def area_win(self):
		self.area_win2 = Area_Win()
		self.area_win2.show()

	def heatval_win(self):
		self.heatval_win2 = Heatval_Win()
		self.heatval_win2.show()

	def powheatfl_win(self):
		self.powheatfl_win2 = Powheatfl_Win()
		self.powheatfl_win2.show()

	def pressstres_win(self):
		self.pressstres_win2 = Pressstres_Win()
		self.pressstres_win2.show()



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

class Powheatfl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Powheatfl_Win")

class Pressstres_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Pressstres_Win")



aplikace = QtWidgets.QApplication(sys.argv)
okno = MainWindow()
okno.show()
sys.exit(aplikace.exec_())

