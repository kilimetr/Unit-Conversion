# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		self.msTOms_res.setText(str(round(msTOms_proc,         8)))
		self.msTOmmin_res.setText(str(round(msTOmmin_proc,     8)))
		self.msTOkmh_res.setText(str(round(msTOkmh_proc,       8)))
		self.msTOfts_res.setText(str(round(msTOfts_proc,       8)))
		self.msTOftmin_res.setText(str(round(msTOftmin_proc,   8)))
		self.msTOmiSTh_res.setText(str(round(msTOmiSTh_proc,   8)))
		self.msTOknotUK_res.setText(str(round(msTOknotUK_proc, 8)))
		self.msTOknotIT_res.setText(str(round(msTOknotIT_proc, 8)))

	def mminTO_fun(self):
		mminTOms_proc     = float(self.mmini_LinEd.text()) / 60
		mminTOmmin_proc   = float(self.mmini_LinEd.text()) * 1
		mminTOkmh_proc    = float(self.mmini_LinEd.text()) * 0.06
		mminTOfts_proc    = float(self.mmini_LinEd.text()) * 0.05468066
		mminTOftmin_proc  = float(self.mmini_LinEd.text()) * 3.28084000
		mminTOmiSTh_proc  = float(self.mmini_LinEd.text()) * 0.03728227
		mminTOknotUK_proc = float(self.mmini_LinEd.text()) * 1.942604 / 60
		mminTOknotIT_proc = float(self.mmini_LinEd.text()) * 1.943844 / 60

		self.mminTOms_res.setText(str(round(mminTOms_proc,         8)))
		self.mminTOmmin_res.setText(str(round(mminTOmmin_proc,     8)))
		self.mminTOkmh_res.setText(str(round(mminTOkmh_proc,       8)))
		self.mminTOfts_res.setText(str(round(mminTOfts_proc,       8)))
		self.mminTOftmin_res.setText(str(round(mminTOftmin_proc,   8)))
		self.mminTOmiSTh_res.setText(str(round(mminTOmiSTh_proc,   8)))
		self.mminTOknotUK_res.setText(str(round(mminTOknotUK_proc, 8)))
		self.mminTOknotIT_res.setText(str(round(mminTOknotIT_proc, 8)))

	def kmhTO_fun(self):
		kmhTOms_proc     = float(self.kmhi_LinEd.text()) / 3.6
		kmhTOmmin_proc   = float(self.kmhi_LinEd.text()) * 50 / 3
		kmhTOkmh_proc    = float(self.kmhi_LinEd.text()) * 1
		kmhTOfts_proc    = float(self.kmhi_LinEd.text()) * 0.9113444
		kmhTOftmin_proc  = float(self.kmhi_LinEd.text()) * 54.68066
		kmhTOmiSTh_proc  = float(self.kmhi_LinEd.text()) * 0.6213712
		kmhTOknotUK_proc = float(self.kmhi_LinEd.text()) * 0.5396122
		kmhTOknotIT_proc = float(self.kmhi_LinEd.text()) * 0.5399573

		self.kmhTOms_res.setText(str(round(kmhTOms_proc,         8)))
		self.kmhTOmmin_res.setText(str(round(kmhTOmmin_proc,     8)))
		self.kmhTOkmh_res.setText(str(round(kmhTOkmh_proc,       8)))
		self.kmhTOfts_res.setText(str(round(kmhTOfts_proc,       8)))
		self.kmhTOftmin_res.setText(str(round(kmhTOftmin_proc,   8)))
		self.kmhTOmiSTh_res.setText(str(round(kmhTOmiSTh_proc,   8)))
		self.kmhTOknotUK_res.setText(str(round(kmhTOknotUK_proc, 8)))
		self.kmhTOknotIT_res.setText(str(round(kmhTOknotIT_proc, 8)))

	def ftsTO_fun(self):
		ftsTOms_proc     = float(self.ftsi_LinEd.text()) * 0.3048
		ftsTOmmin_proc   = float(self.ftsi_LinEd.text()) * 18.288
		ftsTOkmh_proc    = float(self.ftsi_LinEd.text()) * 1.09728
		ftsTOfts_proc    = float(self.ftsi_LinEd.text()) * 1
		ftsTOftmin_proc  = float(self.ftsi_LinEd.text()) * 60
		ftsTOmiSTh_proc  = float(self.ftsi_LinEd.text()) * 0.6818182
		ftsTOknotUK_proc = float(self.ftsi_LinEd.text()) * 0.5921056
		ftsTOknotIT_proc = float(self.ftsi_LinEd.text()) * 0.5924843

		self.ftsTOms_res.setText(str(round(ftsTOms_proc,         8)))
		self.ftsTOmmin_res.setText(str(round(ftsTOmmin_proc,     8)))
		self.ftsTOkmh_res.setText(str(round(ftsTOkmh_proc,       8)))
		self.ftsTOfts_res.setText(str(round(ftsTOfts_proc,       8)))
		self.ftsTOftmin_res.setText(str(round(ftsTOftmin_proc,   8)))
		self.ftsTOmiSTh_res.setText(str(round(ftsTOmiSTh_proc,   8)))
		self.ftsTOknotUK_res.setText(str(round(ftsTOknotUK_proc, 8)))
		self.ftsTOknotIT_res.setText(str(round(ftsTOknotIT_proc, 8)))

	def ftminTO_fun(self):
		ftminTOms_proc     = float(self.ftmini_LinEd.text()) * 5.8e-03
		ftminTOmmin_proc   = float(self.ftmini_LinEd.text()) * 0.3048
		ftminTOkmh_proc    = float(self.ftmini_LinEd.text()) * 1.8288e-02
		ftminTOfts_proc    = float(self.ftmini_LinEd.text()) / 60
		ftminTOftmin_proc  = float(self.ftmini_LinEd.text()) * 1
		ftminTOmiSTh_proc  = float(self.ftmini_LinEd.text()) * 1.136364e-02
		ftminTOknotUK_proc = float(self.ftmini_LinEd.text()) * 0.5921056 / 60
		ftminTOknotIT_proc = float(self.ftmini_LinEd.text()) * 0.5924843 / 60

		self.ftminTOms_res.setText(str(round(ftminTOms_proc,         8)))
		self.ftminTOmmin_res.setText(str(round(ftminTOmmin_proc,     8)))
		self.ftminTOkmh_res.setText(str(round(ftminTOkmh_proc,       8)))
		self.ftminTOfts_res.setText(str(round(ftminTOfts_proc,       8)))
		self.ftminTOftmin_res.setText(str(round(ftminTOftmin_proc,   8)))
		self.ftminTOmiSTh_res.setText(str(round(ftminTOmiSTh_proc,   8)))
		self.ftminTOknotUK_res.setText(str(round(ftminTOknotUK_proc, 8)))
		self.ftminTOknotIT_res.setText(str(round(ftminTOknotIT_proc, 8)))

	def miSThTO_fun(self):
		miSThTOms_proc     = float(self.miSThi_LinEd.text()) * 0.44704
		miSThTOmmin_proc   = float(self.miSThi_LinEd.text()) * 26.8224
		miSThTOkmh_proc    = float(self.miSThi_LinEd.text()) * 1.609344
		miSThTOfts_proc    = float(self.miSThi_LinEd.text()) * 1.466667
		miSThTOftmin_proc  = float(self.miSThi_LinEd.text()) * 88
		miSThTOmiSTh_proc  = float(self.miSThi_LinEd.text()) * 1
		miSThTOknotUK_proc = float(self.miSThi_LinEd.text()) * 0.8684216
		miSThTOknotIT_proc = float(self.miSThi_LinEd.text()) * 0.868977

		self.miSThTOms_res.setText(str(round(miSThTOms_proc,         8)))
		self.miSThTOmmin_res.setText(str(round(miSThTOmmin_proc,     8)))
		self.miSThTOkmh_res.setText(str(round(miSThTOkmh_proc,       8)))
		self.miSThTOfts_res.setText(str(round(miSThTOfts_proc,       8)))
		self.miSThTOftmin_res.setText(str(round(miSThTOftmin_proc,   8)))
		self.miSThTOmiSTh_res.setText(str(round(miSThTOmiSTh_proc,   8)))
		self.miSThTOknotUK_res.setText(str(round(miSThTOknotUK_proc, 8)))
		self.miSThTOknotIT_res.setText(str(round(miSThTOknotIT_proc, 8)))

	def knotUKTO_fun(self):
		knotUKTOms_proc     = float(self.knotUKi_LinEd.text()) * 0.5147730
		knotUKTOmmin_proc   = float(self.knotUKi_LinEd.text()) * 0.5147730 * 60
		knotUKTOkmh_proc    = float(self.knotUKi_LinEd.text()) * 0.5147730 * 3.6
		knotUKTOfts_proc    = float(self.knotUKi_LinEd.text()) * 1.6888878
		knotUKTOftmin_proc  = float(self.knotUKi_LinEd.text()) * 1.6888878 * 60
		knotUKTOmiSTh_proc  = float(self.knotUKi_LinEd.text()) * 1.1515144
		knotUKTOknotUK_proc = float(self.knotUKi_LinEd.text()) * 1
		knotUKTOknotIT_proc = float(self.knotUKi_LinEd.text()) * 1.0006395

		self.knotUKTOms_res.setText(str(round(knotUKTOms_proc,         8)))
		self.knotUKTOmmin_res.setText(str(round(knotUKTOmmin_proc,     8)))
		self.knotUKTOkmh_res.setText(str(round(knotUKTOkmh_proc,       8)))
		self.knotUKTOfts_res.setText(str(round(knotUKTOfts_proc,       8)))
		self.knotUKTOftmin_res.setText(str(round(knotUKTOftmin_proc,   8)))
		self.knotUKTOmiSTh_res.setText(str(round(knotUKTOmiSTh_proc,   8)))
		self.knotUKTOknotUK_res.setText(str(round(knotUKTOknotUK_proc, 8)))
		self.knotUKTOknotIT_res.setText(str(round(knotUKTOknotIT_proc, 8)))

	def knotITTO_fun(self):
		knotITTOms_proc     = float(self.knotITi_LinEd.text()) * 0.5144440
		knotITTOmmin_proc   = float(self.knotITi_LinEd.text()) * 0.5144440 * 60
		knotITTOkmh_proc    = float(self.knotITi_LinEd.text()) * 0.5144440 * 3.6
		knotITTOfts_proc    = float(self.knotITi_LinEd.text()) * 1.6878084
		knotITTOftmin_proc  = float(self.knotITi_LinEd.text()) * 1.6878084 * 60
		knotITTOmiSTh_proc  = float(self.knotITi_LinEd.text()) * 1.1507785
		knotITTOknotUK_proc = float(self.knotITi_LinEd.text()) * 0.9993609
		knotITTOknotIT_proc = float(self.knotITi_LinEd.text()) * 1

		self.knotITTOms_res.setText(str(round(knotITTOms_proc,         8)))
		self.knotITTOmmin_res.setText(str(round(knotITTOmmin_proc,     8)))
		self.knotITTOkmh_res.setText(str(round(knotITTOkmh_proc,       8)))
		self.knotITTOfts_res.setText(str(round(knotITTOfts_proc,       8)))
		self.knotITTOftmin_res.setText(str(round(knotITTOftmin_proc,   8)))
		self.knotITTOmiSTh_res.setText(str(round(knotITTOmiSTh_proc,   8)))
		self.knotITTOknotUK_res.setText(str(round(knotITTOknotUK_proc, 8)))
		self.knotITTOknotIT_res.setText(str(round(knotITTOknotIT_proc, 8)))

	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()


		