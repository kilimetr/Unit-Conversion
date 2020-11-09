# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		mTO_Label = [self.mTOm_res, self.mTOcm_res, self.mTOmm_res, self.mTOum_res, self.mTOangs_res, self.mTOnm_res, self.mTOkm_res, self.mTOin_res, self.mTOft_res,
						  self.mTOyd_res, self.mTOmiST_res, self.mTOmiNV_res]

		cmTO_Label = [self.cmTOm_res, self.cmTOcm_res, self.cmTOmm_res, self.cmTOum_res, self.cmTOangs_res, self.cmTOnm_res, self.cmTOkm_res, self.cmTOin_res, 
						   self.cmTOft_res, self.cmTOyd_res, self.cmTOmiST_res, self.cmTOmiNV_res]

		mmTO_Label = [self.mmTOm_res, self.mmTOcm_res, self.mmTOmm_res, self.mmTOum_res, self.mmTOangs_res, self.mmTOnm_res, self.mmTOkm_res, self.mmTOin_res, 
						   self.mmTOft_res, self.mmTOyd_res, self.mmTOmiST_res, self.mmTOmiNV_res]

		umTO_Label = [self.umTOm_res, self.umTOcm_res, self.umTOmm_res, self.umTOum_res, self.umTOangs_res, self.umTOnm_res, self.umTOkm_res, self.umTOin_res, 
						   self.umTOft_res, self.umTOyd_res, self.umTOmiST_res, self.umTOmiNV_res]

		angsTO_Label = [self.angsTOm_res, self.angsTOcm_res, self.angsTOmm_res, self.angsTOum_res, self.angsTOangs_res, self.angsTOnm_res, self.angsTOkm_res, 
							 self.angsTOin_res, self.angsTOft_res, self.angsTOyd_res, self.angsTOmiST_res, self.angsTOmiNV_res]

		nmTO_Label = [self.nmTOm_res, self.nmTOcm_res, self.nmTOmm_res, self.nmTOum_res, self.nmTOangs_res, self.nmTOnm_res, self.nmTOkm_res, self.nmTOin_res, 
						   self.nmTOft_res, self.nmTOyd_res, self.nmTOmiST_res, self.nmTOmiNV_res]

		kmTO_Label = [self.kmTOm_res, self.kmTOcm_res, self.kmTOmm_res, self.kmTOum_res, self.kmTOangs_res, self.kmTOnm_res, self.kmTOkm_res, self.kmTOin_res, 
						   self.kmTOft_res, self.kmTOyd_res, self.kmTOmiST_res, self.kmTOmiNV_res]

		inTO_Label = [self.inTOm_res, self.inTOcm_res, self.inTOmm_res, self.inTOum_res, self.inTOangs_res, self.inTOnm_res, self.inTOkm_res, self.inTOin_res, 
						   self.inTOft_res, self.inTOyd_res, self.inTOmiST_res, self.inTOmiNV_res]

		ftTO_Label = [self.ftTOm_res, self.ftTOcm_res, self.ftTOmm_res, self.ftTOum_res, self.ftTOangs_res, self.ftTOnm_res, self.ftTOkm_res, self.ftTOin_res, 
						   self.ftTOft_res, self.ftTOyd_res, self.ftTOmiST_res, self.ftTOmiNV_res]

		ydTO_Label = [self.ydTOm_res, self.ydTOcm_res, self.ydTOmm_res, self.ydTOum_res, self.ydTOangs_res, self.ydTOnm_res, self.ydTOkm_res, self.ydTOin_res, 
						   self.ydTOft_res, self.ydTOyd_res, self.ydTOmiST_res, self.ydTOmiNV_res]

		miSTTO_Label = [self.miSTTOm_res, self.miSTTOcm_res, self.miSTTOmm_res, self.miSTTOum_res, self.miSTTOangs_res, self.miSTTOnm_res, self.miSTTOkm_res, 
							 self.miSTTOin_res, self.miSTTOft_res, self.miSTTOyd_res, self.miSTTOmiST_res, self.miSTTOmiNV_res]

		miNVTO_Label = [self.miNVTOm_res, self.miNVTOcm_res, self.miNVTOmm_res, self.miNVTOum_res, self.miNVTOangs_res, self.miNVTOnm_res, self.miNVTOkm_res, 
							 self.miNVTOin_res, self.miNVTOft_res, self.miNVTOyd_res, self.miNVTOmiST_res, self.miNVTOmiNV_res]

		i = 0
		for item in mTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in cmTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in mmTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in umTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in angsTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in nmTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in kmTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in inTO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ftTO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in ydTO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in miSTTO_Label:
			output_grid.addWidget(item, 11, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 0
		for item in miNVTO_Label:
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
		

		