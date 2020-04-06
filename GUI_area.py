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


class Area_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Area Converter")
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))
		
		input_grid = QtWidgets.QGridLayout()
		
		blanklabel      = QtWidgets.QLabel(self)
		self.m2i_LinEd  = QtWidgets.QLineEdit()		# ,self) 
		self.cm2i_LinEd = QtWidgets.QLineEdit()
		self.mm2i_LinEd = QtWidgets.QLineEdit()
		self.ai_LinEd	= QtWidgets.QLineEdit()
		self.hai_LinEd	= QtWidgets.QLineEdit()
		self.in2i_LinEd	= QtWidgets.QLineEdit()
		self.ft2i_LinEd	= QtWidgets.QLineEdit()

		m2u_Label  = QtWidgets.QLabel("m\u00B2")
		cm2u_Label = QtWidgets.QLabel("cm\u00B2")
		mm2u_Label = QtWidgets.QLabel("mm\u00B2")
		au_Label   = QtWidgets.QLabel("a")
		hau_Label  = QtWidgets.QLabel("ha")
		in2u_Label = QtWidgets.QLabel("in\u00B2")
		ft2u_Label = QtWidgets.QLabel("ft\u00B2")

		input_grid.addWidget(blanklabel, 0, 0)
		input_grid.addWidget(self.m2i_LinEd,  1, 0)
		input_grid.addWidget(self.cm2i_LinEd, 2, 0)
		input_grid.addWidget(self.mm2i_LinEd, 3, 0)
		input_grid.addWidget(self.ai_LinEd,   4, 0)
		input_grid.addWidget(self.hai_LinEd,  5, 0)
		input_grid.addWidget(self.in2i_LinEd,  6, 0)
		input_grid.addWidget(self.ft2i_LinEd,  7, 0)

		input_grid.addWidget(m2u_Label,  1, 1)
		input_grid.addWidget(cm2u_Label, 2, 1)
		input_grid.addWidget(mm2u_Label, 3, 1)
		input_grid.addWidget(au_Label,   4, 1)
		input_grid.addWidget(hau_Label,  5, 1)
		input_grid.addWidget(in2u_Label, 6, 1)
		input_grid.addWidget(ft2u_Label, 7, 1)

		input_group.setLayout(input_grid)

		self.m2i_LinEd.returnPressed.connect(self.m2TO_fun)
		self.cm2i_LinEd.returnPressed.connect(self.cm2TO_fun)
		self.mm2i_LinEd.returnPressed.connect(self.mm2TO_fun)
		self.ai_LinEd.returnPressed.connect(self.aTO_fun)
		self.hai_LinEd.returnPressed.connect(self.haTO_fun)
		self.in2i_LinEd.returnPressed.connect(self.in2TO_fun)
		self.ft2i_LinEd.returnPressed.connect(self.ft2TO_fun)

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Black))

		output_grid = QtWidgets.QGridLayout()

		m2_Label  = QtWidgets.QLabel("m\u00B2")
		cm2_Label = QtWidgets.QLabel("cm\u00B2")
		mm2_Label = QtWidgets.QLabel("mm\u00B2")
		a_Label   = QtWidgets.QLabel("a")
		ha_Label  = QtWidgets.QLabel("ha")
		in2_Label = QtWidgets.QLabel("in\u00B2")
		ft2_Label = QtWidgets.QLabel("ft\u00B2")

		self.m2TOm2_res   = QtWidgets.QLabel("0", self)
		self.m2TOcm2_res  = QtWidgets.QLabel("0", self)
		self.m2TOmm2_res  =	QtWidgets.QLabel("0", self)
		self.m2TOa_res    = QtWidgets.QLabel("0", self)
		self.m2TOha_res   = QtWidgets.QLabel("0", self)
		self.m2TOin2_res  = QtWidgets.QLabel("0", self)
		self.m2TOft2_res  = QtWidgets.QLabel("0", self)

		self.cm2TOm2_res  = QtWidgets.QLabel("0", self)
		self.cm2TOcm2_res = QtWidgets.QLabel("0", self)
		self.cm2TOmm2_res = QtWidgets.QLabel("0", self)
		self.cm2TOa_res   = QtWidgets.QLabel("0", self)
		self.cm2TOha_res  = QtWidgets.QLabel("0", self)
		self.cm2TOin2_res = QtWidgets.QLabel("0", self)
		self.cm2TOft2_res = QtWidgets.QLabel("0", self)

		self.mm2TOm2_res  = QtWidgets.QLabel("0", self)
		self.mm2TOcm2_res = QtWidgets.QLabel("0", self)
		self.mm2TOmm2_res = QtWidgets.QLabel("0", self)
		self.mm2TOa_res   = QtWidgets.QLabel("0", self)
		self.mm2TOha_res  = QtWidgets.QLabel("0", self)
		self.mm2TOin2_res = QtWidgets.QLabel("0", self)
		self.mm2TOft2_res = QtWidgets.QLabel("0", self)

		self.aTOm2_res  = QtWidgets.QLabel("0", self)
		self.aTOcm2_res = QtWidgets.QLabel("0", self)
		self.aTOmm2_res = QtWidgets.QLabel("0", self)
		self.aTOa_res   = QtWidgets.QLabel("0", self)
		self.aTOha_res  = QtWidgets.QLabel("0", self)
		self.aTOin2_res = QtWidgets.QLabel("0", self)
		self.aTOft2_res = QtWidgets.QLabel("0", self)

		self.haTOm2_res  = QtWidgets.QLabel("0", self)
		self.haTOcm2_res = QtWidgets.QLabel("0", self)
		self.haTOmm2_res = QtWidgets.QLabel("0", self)
		self.haTOa_res   = QtWidgets.QLabel("0", self)
		self.haTOha_res  = QtWidgets.QLabel("0", self)
		self.haTOin2_res = QtWidgets.QLabel("0", self)
		self.haTOft2_res = QtWidgets.QLabel("0", self)

		self.in2TOm2_res  = QtWidgets.QLabel("0", self)
		self.in2TOcm2_res = QtWidgets.QLabel("0", self)
		self.in2TOmm2_res = QtWidgets.QLabel("0", self)
		self.in2TOa_res   = QtWidgets.QLabel("0", self)
		self.in2TOha_res  = QtWidgets.QLabel("0", self)
		self.in2TOin2_res = QtWidgets.QLabel("0", self)
		self.in2TOft2_res = QtWidgets.QLabel("0", self)

		self.ft2TOm2_res  = QtWidgets.QLabel("0", self)
		self.ft2TOcm2_res = QtWidgets.QLabel("0", self)
		self.ft2TOmm2_res = QtWidgets.QLabel("0", self)
		self.ft2TOa_res   = QtWidgets.QLabel("0", self)
		self.ft2TOha_res  = QtWidgets.QLabel("0", self)
		self.ft2TOin2_res = QtWidgets.QLabel("0", self)
		self.ft2TOft2_res = QtWidgets.QLabel("0", self)

		output_grid.addWidget(m2_Label,  0, 0)
		output_grid.addWidget(cm2_Label, 0, 1)
		output_grid.addWidget(mm2_Label, 0, 2)
		output_grid.addWidget(a_Label,   0, 3)
		output_grid.addWidget(ha_Label,  0, 4)
		output_grid.addWidget(in2_Label, 0, 5)
		output_grid.addWidget(ft2_Label, 0, 6)

		output_grid.addWidget(self.m2TOm2_res,  1, 0)
		output_grid.addWidget(self.m2TOcm2_res, 1, 1)
		output_grid.addWidget(self.m2TOmm2_res, 1, 2)
		output_grid.addWidget(self.m2TOa_res,   1, 3)
		output_grid.addWidget(self.m2TOha_res,  1, 4)
		output_grid.addWidget(self.m2TOin2_res, 1, 5)
		output_grid.addWidget(self.m2TOft2_res, 1, 6)

		output_grid.addWidget(self.cm2TOm2_res,  2, 0)
		output_grid.addWidget(self.cm2TOcm2_res, 2, 1)
		output_grid.addWidget(self.cm2TOmm2_res, 2, 2)
		output_grid.addWidget(self.cm2TOa_res,   2, 3)
		output_grid.addWidget(self.cm2TOha_res,  2, 4)
		output_grid.addWidget(self.cm2TOin2_res, 2, 5)
		output_grid.addWidget(self.cm2TOft2_res, 2, 6)

		output_grid.addWidget(self.mm2TOm2_res,  3, 0)
		output_grid.addWidget(self.mm2TOcm2_res, 3, 1)
		output_grid.addWidget(self.mm2TOmm2_res, 3, 2)
		output_grid.addWidget(self.mm2TOa_res,   3, 3)
		output_grid.addWidget(self.mm2TOha_res,  3, 4)
		output_grid.addWidget(self.mm2TOin2_res, 3, 5)
		output_grid.addWidget(self.mm2TOft2_res, 3, 6)

		output_grid.addWidget(self.aTOm2_res,  4, 0)
		output_grid.addWidget(self.aTOcm2_res, 4, 1)
		output_grid.addWidget(self.aTOmm2_res, 4, 2)
		output_grid.addWidget(self.aTOa_res,   4, 3)
		output_grid.addWidget(self.aTOha_res,  4, 4)
		output_grid.addWidget(self.aTOin2_res, 4, 5)
		output_grid.addWidget(self.aTOft2_res, 4, 6)

		output_grid.addWidget(self.haTOm2_res,  5, 0)
		output_grid.addWidget(self.haTOcm2_res, 5, 1)
		output_grid.addWidget(self.haTOmm2_res, 5, 2)
		output_grid.addWidget(self.haTOa_res,   5, 3)
		output_grid.addWidget(self.haTOha_res,  5, 4)
		output_grid.addWidget(self.haTOin2_res, 5, 5)
		output_grid.addWidget(self.haTOft2_res, 5, 6)

		output_grid.addWidget(self.in2TOm2_res,  6, 0)
		output_grid.addWidget(self.in2TOcm2_res, 6, 1)
		output_grid.addWidget(self.in2TOmm2_res, 6, 2)
		output_grid.addWidget(self.in2TOa_res,   6, 3)
		output_grid.addWidget(self.in2TOha_res,  6, 4)
		output_grid.addWidget(self.in2TOin2_res, 6, 5)
		output_grid.addWidget(self.in2TOft2_res, 6, 6)

		output_grid.addWidget(self.ft2TOm2_res,  7, 0)
		output_grid.addWidget(self.ft2TOcm2_res, 7, 1)
		output_grid.addWidget(self.ft2TOmm2_res, 7, 2)
		output_grid.addWidget(self.ft2TOa_res,   7, 3)
		output_grid.addWidget(self.ft2TOha_res,  7, 4)
		output_grid.addWidget(self.ft2TOin2_res, 7, 5)
		output_grid.addWidget(self.ft2TOft2_res, 7, 6)

		output_group.setLayout(output_grid)

		return output_group

	def m2TO_fun(self):
		m2TOm2_proc  = float(self.m2i_LinEd.text()) * 1
		m2TOcm2_proc = float(self.m2i_LinEd.text()) * 1e+04
		m2TOmm2_proc = float(self.m2i_LinEd.text()) * 1e+06
		m2TOa_proc   = float(self.m2i_LinEd.text()) * 1e-02
		m2TOha_proc  = float(self.m2i_LinEd.text()) * 1e-04
		m2TOin2_proc = float(self.m2i_LinEd.text()) / pow(0.0254, 2)
		m2TOft2_proc = float(self.m2i_LinEd.text()) / pow(0.3048, 2)

		self.m2TOm2_res.setText(str(m2TOm2_proc))
		self.m2TOcm2_res.setText(str(m2TOcm2_proc))
		self.m2TOmm2_res.setText(str(m2TOmm2_proc))
		self.m2TOa_res.setText(str(round(m2TOa_proc,     8)))
		self.m2TOha_res.setText(str(round(m2TOha_proc,   8)))
		self.m2TOin2_res.setText(str(round(m2TOin2_proc, 8)))
		self.m2TOft2_res.setText(str(round(m2TOft2_proc, 8)))

	def cm2TO_fun(self):
		cm2TOm2_proc  = float(self.cm2i_LinEd.text()) * 1e-04
		cm2TOcm2_proc = float(self.cm2i_LinEd.text()) * 1
		cm2TOmm2_proc = float(self.cm2i_LinEd.text()) * 1e+02
		cm2TOa_proc   = float(self.cm2i_LinEd.text()) * 1e-06
		cm2TOha_proc  = float(self.cm2i_LinEd.text()) * 1e-08
		cm2TOin2_proc = float(self.cm2i_LinEd.text()) * 0.155
		cm2TOft2_proc = float(self.cm2i_LinEd.text()) * 0.0010764

		self.cm2TOm2_res.setText(str(cm2TOm2_proc))
		self.cm2TOcm2_res.setText(str(cm2TOcm2_proc))
		self.cm2TOmm2_res.setText(str(cm2TOmm2_proc))
		self.cm2TOa_res.setText(str(round(cm2TOa_proc,     8)))
		self.cm2TOha_res.setText(str(round(cm2TOha_proc,   8)))
		self.cm2TOin2_res.setText(str(round(cm2TOin2_proc, 8)))
		self.cm2TOft2_res.setText(str(round(cm2TOft2_proc, 8)))

	def mm2TO_fun(self):
		mm2TOm2_proc  = float(self.mm2i_LinEd.text()) * 1e-06
		mm2TOcm2_proc = float(self.mm2i_LinEd.text()) * 1e-02
		mm2TOmm2_proc = float(self.mm2i_LinEd.text()) * 1
		mm2TOa_proc   = float(self.mm2i_LinEd.text()) * 1e-08
		mm2TOha_proc  = float(self.mm2i_LinEd.text()) * 1e-10
		mm2TOin2_proc = float(self.mm2i_LinEd.text()) / pow(25.4, 2)
		mm2TOft2_proc = float(self.mm2i_LinEd.text()) * 1.07639e-05

		self.mm2TOm2_res.setText(str(round(mm2TOm2_proc,   8)))
		self.mm2TOcm2_res.setText(str(round(mm2TOcm2_proc, 8)))
		self.mm2TOmm2_res.setText(str(round(mm2TOmm2_proc, 8)))
		self.mm2TOa_res.setText(str(round(mm2TOa_proc,     8)))
		self.mm2TOin2_res.setText(str(round(mm2TOin2_proc, 8)))
		self.mm2TOft2_res.setText(str(round(mm2TOft2_proc, 8)))

	def aTO_fun(self):
		aTOm2_proc  = float(self.ai_LinEd.text()) * 1e+02
		# aTOcm2_proc = float(self.ai_LinEd.text()) * 1e+06
		# aTOmm2_proc = float(self.ai_LinEd.text()) * 1e+08
		aTOa_proc   = float(self.ai_LinEd.text()) * 1
		aTOha_proc  = float(self.ai_LinEd.text()) * 1e-02
		aTOin2_proc = float(self.ai_LinEd.text()) / 6.4516e-06
		aTOft2_proc = float(self.ai_LinEd.text()) / 9.290304e-04

		self.aTOm2_res.setText(str(round(aTOm2_proc,   8)))
		self.aTOcm2_res.setText("-")
		self.aTOmm2_res.setText("-")
		self.aTOa_res.setText(str(round(aTOa_proc,     8)))
		self.aTOha_res.setText(str(round(aTOha_proc,   8)))
		self.aTOin2_res.setText(str(round(aTOin2_proc, 8)))
		self.aTOft2_res.setText(str(round(aTOft2_proc, 8)))

	def haTO_fun(self):
		haTOm2_proc  = float(self.hai_LinEd.text()) * 1e+04
		# haTOcm2_proc = float(self.hai_LinEd.text()) * 1e+08
		# haTOmm2_proc = float(self.hai_LinEd.text()) * 1e+10
		haTOa_proc   = float(self.hai_LinEd.text()) * 1e+02
		haTOha_proc  = float(self.hai_LinEd.text()) * 1
		haTOin2_proc = float(self.hai_LinEd.text()) / 6.4516e-09
		haTOft2_proc = float(self.hai_LinEd.text()) / 9.290304e-02

		self.haTOm2_res.setText(str(round(haTOm2_proc,   8)))
		self.haTOcm2_res.setText("-")
		self.haTOmm2_res.setText("-")
		self.haTOa_res.setText(str(round(haTOa_proc,     8)))
		self.haTOha_res.setText(str(round(haTOha_proc,   8)))
		self.haTOin2_res.setText("-")
		self.haTOft2_res.setText(str(round(haTOft2_proc, 8)))

	def in2TO_fun(self):
		in2TOm2_proc  = float(self.in2i_LinEd.text()) * pow(0.0254, 2)
		in2TOcm2_proc = float(self.in2i_LinEd.text()) * 6.4516
		in2TOmm2_proc = float(self.in2i_LinEd.text()) * 6.4516e+02
		in2TOa_proc   = float(self.in2i_LinEd.text()) * 6.4516e-06
		in2TOha_proc  = float(self.in2i_LinEd.text()) * 6.4616e-08
		in2TOin2_proc = float(self.in2i_LinEd.text()) * 1
		in2TOft2_proc = float(self.in2i_LinEd.text()) * 6.4516e-02/9.290304

		self.in2TOm2_res.setText(str(round(in2TOm2_proc,   8)))
		self.in2TOcm2_res.setText(str(round(in2TOcm2_proc, 8)))
		self.in2TOmm2_res.setText(str(round(in2TOmm2_proc, 8)))
		self.in2TOa_res.setText(str(round(in2TOa_proc,     8)))
		self.in2TOha_res.setText(str(round(in2TOha_proc,   8)))
		self.in2TOin2_res.setText(str(round(in2TOin2_proc, 8)))
		self.in2TOft2_res.setText(str(round(in2TOft2_proc, 8)))

	def ft2TO_fun(self):
		ft2TOm2_proc  = float(self.ft2i_LinEd.text()) * pow(0.3048, 2)
		ft2TOcm2_proc = float(self.ft2i_LinEd.text()) * 9.290304e+02
		ft2TOmm2_proc = float(self.ft2i_LinEd.text()) * 9.290304e+04
		ft2TOa_proc   = float(self.ft2i_LinEd.text()) * 9.290304e-04
		ft2TOha_proc  = float(self.ft2i_LinEd.text()) * 9.290304e-06
		ft2TOin2_proc = float(self.ft2i_LinEd.text()) * 9.290304e+02/6.4516
		ft2TOft2_proc = float(self.ft2i_LinEd.text()) * 1

		self.ft2TOm2_res.setText(str(round(ft2TOm2_proc,   8)))
		self.ft2TOcm2_res.setText(str(round(ft2TOcm2_proc, 8)))
		self.ft2TOmm2_res.setText(str(round(ft2TOmm2_proc, 8)))
		self.ft2TOa_res.setText(str(round(ft2TOa_proc,     8)))
		self.ft2TOha_res.setText(str(round(ft2TOha_proc,   8)))
		self.ft2TOin2_res.setText(str(round(ft2TOin2_proc, 8)))
		self.ft2TOft2_res.setText(str(round(ft2TOft2_proc, 8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()


class Heatval_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.setWindowTitle("Heatval_Win")

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

