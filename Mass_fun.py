# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		kgTO_Label       = [self.kgTOkg_res, self.kgTOmton_res, self.kgTOounce_res, self.kgTOpound_res, self.kgTOshortton_res, self.kgTOlongton_res]

		mtonTO_Label     = [self.mtonTOkg_res, self.mtonTOmton_res, self.mtonTOounce_res, self.mtonTOpound_res, self.mtonTOshortton_res, self.mtonTOlongton_res]

		ounceTO_Label    = [self.ounceTOkg_res, self.ounceTOmton_res, self.ounceTOounce_res, self.ounceTOpound_res, self.ounceTOshortton_res, self.ounceTOlongton_res]

		poundTO_Label    = [self.poundTOkg_res, self.poundTOmton_res, self.poundTOounce_res, self.poundTOpound_res, self.poundTOshortton_res, self.poundTOlongton_res]

		shorttonTO_Label = [self.shorttonTOkg_res, self.shorttonTOmton_res, self.shorttonTOounce_res, self.shorttonTOpound_res, self.shorttonTOshortton_res, 
								 self.shorttonTOlongton_res]

		longtonTO_Label  = [self.longtonTOkg_res, self.longtonTOmton_res, self.longtonTOounce_res, self.longtonTOpound_res, self.longtonTOshortton_res, 
							 	 self.longtonTOlongton_res]

		i = 0
		for item in kgTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in mtonTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ounceTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in poundTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in shorttonTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in longtonTO_Label:
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


	