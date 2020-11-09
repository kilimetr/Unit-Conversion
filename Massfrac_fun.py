# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		LinEd_list = [self.decimali_LinEd, self.percenti_LinEd, self.promilei_LinEd, self.ppmi_LinEd, self.ppbi_LinEd]

		Label_list = [blanklabel, "decimal (1)", "%", "‰", "ppm", "ppb"]
		
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

		self.decimali_LinEd.returnPressed.connect(self.decimalTO_fun)
		self.percenti_LinEd.returnPressed.connect(self.percentTO_fun)
		self.promilei_LinEd.returnPressed.connect(self.promileTO_fun)
		self.ppmi_LinEd.returnPressed.connect(self.ppmTO_fun)
		self.ppbi_LinEd.returnPressed.connect(self.ppbTO_fun)

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

		decimalTO_Label = [self.decimalTOdecimal_res, self.decimalTOpercent_res, self.decimalTOpromile_res, self.decimalTOppm_res, self.decimalTOppb_res]

		percentTO_Label = [self.percentTOdecimal_res, self.percentTOpercent_res, self.percentTOpromile_res, self.percentTOppm_res, self.percentTOppb_res]

		promileTO_Label = [self.promileTOdecimal_res, self.promileTOpercent_res, self.promileTOpromile_res, self.promileTOppm_res, self.promileTOppb_res]

		ppmTO_Label = [self.ppmTOdecimal_res, self.ppmTOpercent_res, self.ppmTOpromile_res, self.ppmTOppm_res, self.ppmTOppb_res]

		ppbTO_Label = [self.ppbTOdecimal_res, self.ppbTOpercent_res, self.ppbTOpromile_res, self.ppbTOppm_res, self.ppbTOppb_res]

		i = 0
		for item in decimalTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in percentTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in promileTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ppmTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ppbTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

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


