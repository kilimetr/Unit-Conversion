# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		JTO_Label = [self.JTOJ_res, self.JTOkJ_res, self.JTOkWh_res, self.JTOBTUIT_res, self.JTOBTUmean_res, self.JTOcalIT_res, self.JTOcalTH_res,
						  self.JTOhphr_res, self.JTOftlbf_res, self.JTOftpdl_res]

		kJTO_Label = [self.kJTOJ_res, self.kJTOkJ_res, self.kJTOkWh_res, self.kJTOBTUIT_res, self.kJTOBTUmean_res, self.kJTOcalIT_res, self.kJTOcalTH_res,
						   self.kJTOhphr_res, self.kJTOftlbf_res, self.kJTOftpdl_res]

		kWhTO_Label = [self.kWhTOJ_res, self.kWhTOkJ_res, self.kWhTOkWh_res, self.kWhTOBTUIT_res, self.kWhTOBTUmean_res, self.kWhTOcalIT_res, self.kWhTOcalTH_res,
						    self.kWhTOhphr_res, self.kWhTOftlbf_res, self.kWhTOftpdl_res]

		BTUITTO_Label = [self.BTUITTOJ_res, self.BTUITTOkJ_res, self.BTUITTOkWh_res, self.BTUITTOBTUIT_res, self.BTUITTOBTUmean_res, self.BTUITTOcalIT_res, 
							  self.BTUITTOcalTH_res, self.BTUITTOhphr_res, self.BTUITTOftlbf_res, self.BTUITTOftpdl_res]

		BTUmeanTO_Label = [self.BTUmeanTOJ_res, self.BTUmeanTOkJ_res, self.BTUmeanTOkWh_res, self.BTUmeanTOBTUIT_res, self.BTUmeanTOBTUmean_res, 
								self.BTUmeanTOcalIT_res, self.BTUmeanTOcalTH_res, self.BTUmeanTOhphr_res, self.BTUmeanTOftlbf_res, self.BTUmeanTOftpdl_res]

		calITTO_Label = [self.calITTOJ_res, self.calITTOkJ_res, self.calITTOkWh_res, self.calITTOBTUIT_res, self.calITTOBTUmean_res, self.calITTOcalIT_res, 
							  self.calITTOcalTH_res, self.calITTOhphr_res, self.calITTOftlbf_res, self.calITTOftpdl_res]

		calTHTO_Label = [self.calTHTOJ_res, self.calTHTOkJ_res, self.calTHTOkWh_res, self.calTHTOBTUIT_res, self.calTHTOBTUmean_res, self.calTHTOcalIT_res, 
							  self.calTHTOcalTH_res, self.calTHTOhphr_res, self.calTHTOftlbf_res, self.calTHTOftpdl_res]

		hphrTO_Label = [self.hphrTOJ_res, self.hphrTOkJ_res, self.hphrTOkWh_res, self.hphrTOBTUIT_res, self.hphrTOBTUmean_res, self.hphrTOcalIT_res, 
							 self.hphrTOcalTH_res, self.hphrTOhphr_res, self.hphrTOftlbf_res, self.hphrTOftpdl_res]

		ftlbfTO_Label = [self.ftlbfTOJ_res, self.ftlbfTOkJ_res, self.ftlbfTOkWh_res, self.ftlbfTOBTUIT_res, self.ftlbfTOBTUmean_res, self.ftlbfTOcalIT_res, 
							  self.ftlbfTOcalTH_res, self.ftlbfTOhphr_res, self.ftlbfTOftlbf_res, self.ftlbfTOftpdl_res]

		ftpdlTO_Label = [self.ftpdlTOJ_res, self.ftpdlTOkJ_res, self.ftpdlTOkWh_res, self.ftpdlTOBTUIT_res, self.ftpdlTOBTUmean_res, self.ftpdlTOcalIT_res, 
							  self.ftpdlTOcalTH_res, self.ftpdlTOhphr_res, self.ftpdlTOftlbf_res, self.ftpdlTOftpdl_res]

		i = 0
		for item in JTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kJTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kWhTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in BTUITTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in BTUmeanTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in calITTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in calTHTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in hphrTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ftlbfTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ftpdlTO_Label:
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
		

		