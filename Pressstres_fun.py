# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore



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

		LinEd_list = [self.Pai_LinEd, self.kPai_LinEd, self.MPai_LinEd, self.mbari_LinEd, self.bari_LinEd, self.atmi_LinEd, self.psii_LinEd, self.kgcm2i_LinEd,
					  self.kgm2i_LinEd, self.Nm2i_LinEd, self.lbin2i_LinEd, self.lbft2i_LinEd, self.Torri_LinEd, self.dynecm2i_LinEd, self.mmH2Oi_LinEd,
					  self.mmHgi_LinEd, self.inH2Oi_LinEd, self.inHgi_LinEd]

		Label_list = [blanklabel, "Pa", "kPa", "MPa", "mbar", "bar", "atm", "psi", "kg/cm\u00B2", "kg/m\u00B2", "N/m\u00B2", "lb/in\u00B2", "lb/ft\u00B2", "Torr", 
					  "dyne/cm\u00B2", "mm H<sub>2</sub>O", "mm Hg", "in H<sub>2</sub>O", "in Hg"]
		
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

		self.Pai_LinEd.returnPressed.connect(self.PaTO_fun)
		self.kPai_LinEd.returnPressed.connect(self.kPaTO_fun)
		self.MPai_LinEd.returnPressed.connect(self.MPaTO_fun)
		self.mbari_LinEd.returnPressed.connect(self.mbarTO_fun)
		self.bari_LinEd.returnPressed.connect(self.barTO_fun)
		self.atmi_LinEd.returnPressed.connect(self.atmTO_fun)
		self.psii_LinEd.returnPressed.connect(self.psiTO_fun)
		self.kgcm2i_LinEd.returnPressed.connect(self.kgcm2TO_fun)
		self.kgm2i_LinEd.returnPressed.connect(self.kgm2TO_fun)
		self.Nm2i_LinEd.returnPressed.connect(self.Nm2TO_fun)
		self.lbin2i_LinEd.returnPressed.connect(self.lbin2TO_fun)
		self.lbft2i_LinEd.returnPressed.connect(self.lbft2TO_fun)
		self.Torri_LinEd.returnPressed.connect(self.TorrTO_fun)
		self.dynecm2i_LinEd.returnPressed.connect(self.dynecm2TO_fun)
		self.mmH2Oi_LinEd.returnPressed.connect(self.mmH2OTO_fun)
		self.mmHgi_LinEd.returnPressed.connect(self.mmHgTO_fun)
		self.inH2Oi_LinEd.returnPressed.connect(self.inH2OTO_fun)
		self.inHgi_LinEd.returnPressed.connect(self.inHgTO_fun)

		return input_group

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

		self.PaTOPa_res      = QtWidgets.QLabel("0", self)
		self.PaTOkPa_res     = QtWidgets.QLabel("0", self)
		self.PaTOMPa_res     = QtWidgets.QLabel("0", self)
		self.PaTOmbar_res    = QtWidgets.QLabel("0", self)
		self.PaTObar_res     = QtWidgets.QLabel("0", self)
		self.PaTOatm_res     = QtWidgets.QLabel("0", self)
		self.PaTOpsi_res     = QtWidgets.QLabel("0", self)
		self.PaTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.PaTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.PaTONm2_res     = QtWidgets.QLabel("0", self)
		self.PaTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.PaTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.PaTOTorr_res    = QtWidgets.QLabel("0", self)
		self.PaTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.PaTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.PaTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.PaTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.PaTOinHg_res    = QtWidgets.QLabel("0", self)

		self.kPaTOPa_res      = QtWidgets.QLabel("0", self)
		self.kPaTOkPa_res     = QtWidgets.QLabel("0", self)
		self.kPaTOMPa_res     = QtWidgets.QLabel("0", self)
		self.kPaTOmbar_res    = QtWidgets.QLabel("0", self)
		self.kPaTObar_res     = QtWidgets.QLabel("0", self)
		self.kPaTOatm_res     = QtWidgets.QLabel("0", self)
		self.kPaTOpsi_res     = QtWidgets.QLabel("0", self)
		self.kPaTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.kPaTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.kPaTONm2_res     = QtWidgets.QLabel("0", self)
		self.kPaTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.kPaTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.kPaTOTorr_res    = QtWidgets.QLabel("0", self)
		self.kPaTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.kPaTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.kPaTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.kPaTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.kPaTOinHg_res    = QtWidgets.QLabel("0", self)

		self.MPaTOPa_res      = QtWidgets.QLabel("0", self)
		self.MPaTOkPa_res     = QtWidgets.QLabel("0", self)
		self.MPaTOMPa_res     = QtWidgets.QLabel("0", self)
		self.MPaTOmbar_res    = QtWidgets.QLabel("0", self)
		self.MPaTObar_res     = QtWidgets.QLabel("0", self)
		self.MPaTOatm_res     = QtWidgets.QLabel("0", self)
		self.MPaTOpsi_res     = QtWidgets.QLabel("0", self)
		self.MPaTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.MPaTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.MPaTONm2_res     = QtWidgets.QLabel("0", self)
		self.MPaTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.MPaTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.MPaTOTorr_res    = QtWidgets.QLabel("0", self)
		self.MPaTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.MPaTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.MPaTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.MPaTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.MPaTOinHg_res    = QtWidgets.QLabel("0", self)

		self.mbarTOPa_res      = QtWidgets.QLabel("0", self)
		self.mbarTOkPa_res     = QtWidgets.QLabel("0", self)
		self.mbarTOMPa_res     = QtWidgets.QLabel("0", self)
		self.mbarTOmbar_res    = QtWidgets.QLabel("0", self)
		self.mbarTObar_res     = QtWidgets.QLabel("0", self)
		self.mbarTOatm_res     = QtWidgets.QLabel("0", self)
		self.mbarTOpsi_res     = QtWidgets.QLabel("0", self)
		self.mbarTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.mbarTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.mbarTONm2_res     = QtWidgets.QLabel("0", self)
		self.mbarTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.mbarTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.mbarTOTorr_res    = QtWidgets.QLabel("0", self)
		self.mbarTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.mbarTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.mbarTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.mbarTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.mbarTOinHg_res    = QtWidgets.QLabel("0", self)

		self.barTOPa_res      = QtWidgets.QLabel("0", self)
		self.barTOkPa_res     = QtWidgets.QLabel("0", self)
		self.barTOMPa_res     = QtWidgets.QLabel("0", self)
		self.barTOmbar_res    = QtWidgets.QLabel("0", self)
		self.barTObar_res     = QtWidgets.QLabel("0", self)
		self.barTOatm_res     = QtWidgets.QLabel("0", self)
		self.barTOpsi_res     = QtWidgets.QLabel("0", self)
		self.barTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.barTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.barTONm2_res     = QtWidgets.QLabel("0", self)
		self.barTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.barTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.barTOTorr_res    = QtWidgets.QLabel("0", self)
		self.barTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.barTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.barTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.barTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.barTOinHg_res    = QtWidgets.QLabel("0", self)

		self.atmTOPa_res      = QtWidgets.QLabel("0", self)
		self.atmTOkPa_res     = QtWidgets.QLabel("0", self)
		self.atmTOMPa_res     = QtWidgets.QLabel("0", self)
		self.atmTOmbar_res    = QtWidgets.QLabel("0", self)
		self.atmTObar_res     = QtWidgets.QLabel("0", self)
		self.atmTOatm_res     = QtWidgets.QLabel("0", self)
		self.atmTOpsi_res     = QtWidgets.QLabel("0", self)
		self.atmTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.atmTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.atmTONm2_res     = QtWidgets.QLabel("0", self)
		self.atmTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.atmTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.atmTOTorr_res    = QtWidgets.QLabel("0", self)
		self.atmTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.atmTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.atmTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.atmTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.atmTOinHg_res    = QtWidgets.QLabel("0", self)

		self.psiTOPa_res      = QtWidgets.QLabel("0", self)
		self.psiTOkPa_res     = QtWidgets.QLabel("0", self)
		self.psiTOMPa_res     = QtWidgets.QLabel("0", self)
		self.psiTOmbar_res    = QtWidgets.QLabel("0", self)
		self.psiTObar_res     = QtWidgets.QLabel("0", self)
		self.psiTOatm_res     = QtWidgets.QLabel("0", self)
		self.psiTOpsi_res     = QtWidgets.QLabel("0", self)
		self.psiTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.psiTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.psiTONm2_res     = QtWidgets.QLabel("0", self)
		self.psiTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.psiTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.psiTOTorr_res    = QtWidgets.QLabel("0", self)
		self.psiTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.psiTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.psiTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.psiTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.psiTOinHg_res    = QtWidgets.QLabel("0", self)

		self.kgcm2TOPa_res      = QtWidgets.QLabel("0", self)
		self.kgcm2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.kgcm2TObar_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOatm_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.kgcm2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.kgcm2TONm2_res     = QtWidgets.QLabel("0", self)
		self.kgcm2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.kgcm2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.kgcm2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.kgcm2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.kgcm2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.kgcm2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.kgcm2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.kgcm2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.kgm2TOPa_res      = QtWidgets.QLabel("0", self)
		self.kgm2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.kgm2TObar_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOatm_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.kgm2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.kgm2TONm2_res     = QtWidgets.QLabel("0", self)
		self.kgm2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.kgm2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.kgm2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.kgm2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.kgm2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.kgm2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.kgm2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.kgm2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.Nm2TOPa_res      = QtWidgets.QLabel("0", self)
		self.Nm2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.Nm2TObar_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOatm_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.Nm2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.Nm2TONm2_res     = QtWidgets.QLabel("0", self)
		self.Nm2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.Nm2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.Nm2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.Nm2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.Nm2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.Nm2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.Nm2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.Nm2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.lbin2TOPa_res      = QtWidgets.QLabel("0", self)
		self.lbin2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.lbin2TObar_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOatm_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.lbin2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.lbin2TONm2_res     = QtWidgets.QLabel("0", self)
		self.lbin2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.lbin2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.lbin2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.lbin2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.lbin2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.lbin2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.lbin2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.lbin2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.lbft2TOPa_res      = QtWidgets.QLabel("0", self)
		self.lbft2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.lbft2TObar_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOatm_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.lbft2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.lbft2TONm2_res     = QtWidgets.QLabel("0", self)
		self.lbft2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.lbft2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.lbft2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.lbft2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.lbft2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.lbft2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.lbft2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.lbft2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.TorrTOPa_res      = QtWidgets.QLabel("0", self)
		self.TorrTOkPa_res     = QtWidgets.QLabel("0", self)
		self.TorrTOMPa_res     = QtWidgets.QLabel("0", self)
		self.TorrTOmbar_res    = QtWidgets.QLabel("0", self)
		self.TorrTObar_res     = QtWidgets.QLabel("0", self)
		self.TorrTOatm_res     = QtWidgets.QLabel("0", self)
		self.TorrTOpsi_res     = QtWidgets.QLabel("0", self)
		self.TorrTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.TorrTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.TorrTONm2_res     = QtWidgets.QLabel("0", self)
		self.TorrTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.TorrTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.TorrTOTorr_res    = QtWidgets.QLabel("0", self)
		self.TorrTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.TorrTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.TorrTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.TorrTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.TorrTOinHg_res    = QtWidgets.QLabel("0", self)

		self.dynecm2TOPa_res      = QtWidgets.QLabel("0", self)
		self.dynecm2TOkPa_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOMPa_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOmbar_res    = QtWidgets.QLabel("0", self)
		self.dynecm2TObar_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOatm_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOpsi_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.dynecm2TOkgm2_res    = QtWidgets.QLabel("0", self)
		self.dynecm2TONm2_res     = QtWidgets.QLabel("0", self)
		self.dynecm2TOlbin2_res   = QtWidgets.QLabel("0", self)
		self.dynecm2TOlbft2_res   = QtWidgets.QLabel("0", self)
		self.dynecm2TOTorr_res    = QtWidgets.QLabel("0", self)
		self.dynecm2TOdynecm2_res = QtWidgets.QLabel("0", self)
		self.dynecm2TOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.dynecm2TOmmHg_res    = QtWidgets.QLabel("0", self)
		self.dynecm2TOinH2O_res   = QtWidgets.QLabel("0", self)
		self.dynecm2TOinHg_res    = QtWidgets.QLabel("0", self)

		self.mmH2OTOPa_res      = QtWidgets.QLabel("0", self)
		self.mmH2OTOkPa_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOMPa_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOmbar_res    = QtWidgets.QLabel("0", self)
		self.mmH2OTObar_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOatm_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOpsi_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.mmH2OTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.mmH2OTONm2_res     = QtWidgets.QLabel("0", self)
		self.mmH2OTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.mmH2OTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.mmH2OTOTorr_res    = QtWidgets.QLabel("0", self)
		self.mmH2OTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.mmH2OTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.mmH2OTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.mmH2OTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.mmH2OTOinHg_res    = QtWidgets.QLabel("0", self)

		self.mmHgTOPa_res      = QtWidgets.QLabel("0", self)
		self.mmHgTOkPa_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOMPa_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOmbar_res    = QtWidgets.QLabel("0", self)
		self.mmHgTObar_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOatm_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOpsi_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.mmHgTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.mmHgTONm2_res     = QtWidgets.QLabel("0", self)
		self.mmHgTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.mmHgTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.mmHgTOTorr_res    = QtWidgets.QLabel("0", self)
		self.mmHgTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.mmHgTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.mmHgTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.mmHgTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.mmHgTOinHg_res    = QtWidgets.QLabel("0", self)

		self.inH2OTOPa_res      = QtWidgets.QLabel("0", self)
		self.inH2OTOkPa_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOMPa_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOmbar_res    = QtWidgets.QLabel("0", self)
		self.inH2OTObar_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOatm_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOpsi_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.inH2OTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.inH2OTONm2_res     = QtWidgets.QLabel("0", self)
		self.inH2OTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.inH2OTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.inH2OTOTorr_res    = QtWidgets.QLabel("0", self)
		self.inH2OTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.inH2OTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.inH2OTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.inH2OTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.inH2OTOinHg_res    = QtWidgets.QLabel("0", self)

		self.inHgTOPa_res      = QtWidgets.QLabel("0", self)
		self.inHgTOkPa_res     = QtWidgets.QLabel("0", self)
		self.inHgTOMPa_res     = QtWidgets.QLabel("0", self)
		self.inHgTOmbar_res    = QtWidgets.QLabel("0", self)
		self.inHgTObar_res     = QtWidgets.QLabel("0", self)
		self.inHgTOatm_res     = QtWidgets.QLabel("0", self)
		self.inHgTOpsi_res     = QtWidgets.QLabel("0", self)
		self.inHgTOkgcm2_res   = QtWidgets.QLabel("0", self)
		self.inHgTOkgm2_res    = QtWidgets.QLabel("0", self)
		self.inHgTONm2_res     = QtWidgets.QLabel("0", self)
		self.inHgTOlbin2_res   = QtWidgets.QLabel("0", self)
		self.inHgTOlbft2_res   = QtWidgets.QLabel("0", self)
		self.inHgTOTorr_res    = QtWidgets.QLabel("0", self)
		self.inHgTOdynecm2_res = QtWidgets.QLabel("0", self)
		self.inHgTOmmH2O_res   = QtWidgets.QLabel("0", self)
		self.inHgTOmmHg_res    = QtWidgets.QLabel("0", self)
		self.inHgTOinH2O_res   = QtWidgets.QLabel("0", self)
		self.inHgTOinHg_res    = QtWidgets.QLabel("0", self)

		PaTO_Label = [self.PaTOPa_res, self.PaTOkPa_res, self.PaTOMPa_res, self.PaTOmbar_res, self.PaTObar_res, self.PaTOatm_res, self.PaTOpsi_res, self.PaTOkgcm2_res,
					  self.PaTOkgm2_res, self.PaTONm2_res, self.PaTOlbin2_res, self.PaTOlbft2_res, self.PaTOTorr_res, self.PaTOdynecm2_res, self.PaTOmmH2O_res,
					  self.PaTOmmHg_res, self.PaTOinH2O_res, self.PaTOinHg_res]

		kPaTO_Label = [self.kPaTOPa_res, self.kPaTOkPa_res, self.kPaTOMPa_res, self.kPaTOmbar_res, self.kPaTObar_res, self.kPaTOatm_res, self.kPaTOpsi_res, 
					   self.kPaTOkgcm2_res, self.kPaTOkgm2_res, self.kPaTONm2_res, self.kPaTOlbin2_res, self.kPaTOlbft2_res, self.kPaTOTorr_res, self.kPaTOdynecm2_res, 
					   self.kPaTOmmH2O_res, self.kPaTOmmHg_res, self.kPaTOinH2O_res, self.kPaTOinHg_res]

		MPaTO_Label = [self.MPaTOPa_res, self.MPaTOkPa_res, self.MPaTOMPa_res, self.MPaTOmbar_res, self.MPaTObar_res, self.MPaTOatm_res, self.MPaTOpsi_res, 
					   self.MPaTOkgcm2_res, self.MPaTOkgm2_res, self.MPaTONm2_res, self.MPaTOlbin2_res, self.MPaTOlbft2_res, self.MPaTOTorr_res, self.MPaTOdynecm2_res, 
					   self.MPaTOmmH2O_res, self.MPaTOmmHg_res, self.MPaTOinH2O_res, self.MPaTOinHg_res]

		mbarTO_Label = [self.mbarTOPa_res, self.mbarTOkPa_res, self.mbarTOMPa_res, self.mbarTOmbar_res, self.mbarTObar_res, self.mbarTOatm_res, self.mbarTOpsi_res, 
						self.mbarTOkgcm2_res, self.mbarTOkgm2_res, self.mbarTONm2_res, self.mbarTOlbin2_res, self.mbarTOlbft2_res, self.mbarTOTorr_res, 
						self.mbarTOdynecm2_res, self.mbarTOmmH2O_res, self.mbarTOmmHg_res, self.mbarTOinH2O_res, self.mbarTOinHg_res]

		barTO_Label = [self.barTOPa_res, self.barTOkPa_res, self.barTOMPa_res, self.barTOmbar_res, self.barTObar_res, self.barTOatm_res, self.barTOpsi_res, 
					   self.barTOkgcm2_res, self.barTOkgm2_res, self.barTONm2_res, self.barTOlbin2_res, self.barTOlbft2_res, self.barTOTorr_res, 
					   self.barTOdynecm2_res, self.barTOmmH2O_res, self.barTOmmHg_res, self.barTOinH2O_res, self.barTOinHg_res]

		atmTO_Label = [self.atmTOPa_res, self.atmTOkPa_res, self.atmTOMPa_res, self.atmTOmbar_res, self.atmTObar_res, self.atmTOatm_res, self.atmTOpsi_res, 
					   self.atmTOkgcm2_res, self.atmTOkgm2_res, self.atmTONm2_res, self.atmTOlbin2_res, self.atmTOlbft2_res, self.atmTOTorr_res, 
					   self.atmTOdynecm2_res, self.atmTOmmH2O_res, self.atmTOmmHg_res, self.atmTOinH2O_res, self.atmTOinHg_res]

		psiTO_Label = [self.psiTOPa_res, self.psiTOkPa_res, self.psiTOMPa_res, self.psiTOmbar_res, self.psiTObar_res, self.psiTOatm_res, self.psiTOpsi_res, 
					   self.psiTOkgcm2_res, self.psiTOkgm2_res, self.psiTONm2_res, self.psiTOlbin2_res, self.psiTOlbft2_res, self.psiTOTorr_res, 
					   self.psiTOdynecm2_res, self.psiTOmmH2O_res, self.psiTOmmHg_res, self.psiTOinH2O_res, self.psiTOinHg_res]

		kgcm2TO_Label = [self.kgcm2TOPa_res, self.kgcm2TOkPa_res, self.kgcm2TOMPa_res, self.kgcm2TOmbar_res, self.kgcm2TObar_res, self.kgcm2TOatm_res, 
						 self.kgcm2TOpsi_res, self.kgcm2TOkgcm2_res, self.kgcm2TOkgm2_res, self.kgcm2TONm2_res, self.kgcm2TOlbin2_res, self.kgcm2TOlbft2_res, 
						 self.kgcm2TOTorr_res, self.kgcm2TOdynecm2_res, self.kgcm2TOmmH2O_res, self.kgcm2TOmmHg_res, self.kgcm2TOinH2O_res, self.kgcm2TOinHg_res]

		kgm2TO_Label = [self.kgm2TOPa_res, self.kgm2TOkPa_res, self.kgm2TOMPa_res, self.kgm2TOmbar_res, self.kgm2TObar_res, self.kgm2TOatm_res, 
						self.kgm2TOpsi_res, self.kgm2TOkgcm2_res, self.kgm2TOkgm2_res, self.kgm2TONm2_res, self.kgm2TOlbin2_res, self.kgm2TOlbft2_res, 
						self.kgm2TOTorr_res, self.kgm2TOdynecm2_res, self.kgm2TOmmH2O_res, self.kgm2TOmmHg_res, self.kgm2TOinH2O_res, self.kgm2TOinHg_res]

		Nm2TO_Label = [self.Nm2TOPa_res, self.Nm2TOkPa_res, self.Nm2TOMPa_res, self.Nm2TOmbar_res, self.Nm2TObar_res, self.Nm2TOatm_res, self.Nm2TOpsi_res, 
					   self.Nm2TOkgcm2_res, self.Nm2TOkgm2_res, self.Nm2TONm2_res, self.Nm2TOlbin2_res, self.Nm2TOlbft2_res, self.Nm2TOTorr_res, 
					   self.Nm2TOdynecm2_res, self.Nm2TOmmH2O_res, self.Nm2TOmmHg_res, self.Nm2TOinH2O_res, self.Nm2TOinHg_res]

		lbin2TO_Label = [self.lbin2TOPa_res, self.lbin2TOkPa_res, self.lbin2TOMPa_res, self.lbin2TOmbar_res, self.lbin2TObar_res, self.lbin2TOatm_res, 
						 self.lbin2TOpsi_res, self.lbin2TOkgcm2_res, self.lbin2TOkgm2_res, self.lbin2TONm2_res, self.lbin2TOlbin2_res, self.lbin2TOlbft2_res, 
						 self.lbin2TOTorr_res, self.lbin2TOdynecm2_res, self.lbin2TOmmH2O_res, self.lbin2TOmmHg_res, self.lbin2TOinH2O_res, self.lbin2TOinHg_res]

		lbft2TO_Label = [self.lbft2TOPa_res, self.lbft2TOkPa_res, self.lbft2TOMPa_res, self.lbft2TOmbar_res, self.lbft2TObar_res, self.lbft2TOatm_res, 
						 self.lbft2TOpsi_res, self.lbft2TOkgcm2_res, self.lbft2TOkgm2_res, self.lbft2TONm2_res, self.lbft2TOlbin2_res, self.lbft2TOlbft2_res, 
						 self.lbft2TOTorr_res, self.lbft2TOdynecm2_res, self.lbft2TOmmH2O_res, self.lbft2TOmmHg_res, self.lbft2TOinH2O_res, self.lbft2TOinHg_res]

		TorrTO_Label = [self.TorrTOPa_res, self.TorrTOkPa_res, self.TorrTOMPa_res, self.TorrTOmbar_res, self.TorrTObar_res, self.TorrTOatm_res, 
						self.TorrTOpsi_res, self.TorrTOkgcm2_res, self.TorrTOkgm2_res, self.TorrTONm2_res, self.TorrTOlbin2_res, self.TorrTOlbft2_res, 
						self.TorrTOTorr_res, self.TorrTOdynecm2_res, self.TorrTOmmH2O_res, self.TorrTOmmHg_res, self.TorrTOinH2O_res, self.TorrTOinHg_res]

		dynecm2TO_Label = [self.dynecm2TOPa_res, self.dynecm2TOkPa_res, self.dynecm2TOMPa_res, self.dynecm2TOmbar_res, self.dynecm2TObar_res, self.dynecm2TOatm_res, 
						   self.dynecm2TOpsi_res, self.dynecm2TOkgcm2_res, self.dynecm2TOkgm2_res, self.dynecm2TONm2_res, self.dynecm2TOlbin2_res, 
						   self.dynecm2TOlbft2_res, self.dynecm2TOTorr_res, self.dynecm2TOdynecm2_res, self.dynecm2TOmmH2O_res, self.dynecm2TOmmHg_res, 
						   self.dynecm2TOinH2O_res, self.dynecm2TOinHg_res]

		mmH2OTO_Label = [self.mmH2OTOPa_res, self.mmH2OTOkPa_res, self.mmH2OTOMPa_res, self.mmH2OTOmbar_res, self.mmH2OTObar_res, self.mmH2OTOatm_res, 
						 self.mmH2OTOpsi_res, self.mmH2OTOkgcm2_res, self.mmH2OTOkgm2_res, self.mmH2OTONm2_res, self.mmH2OTOlbin2_res, self.mmH2OTOlbft2_res, 
						 self.mmH2OTOTorr_res, self.mmH2OTOdynecm2_res, self.mmH2OTOmmH2O_res, self.mmH2OTOmmHg_res, self.mmH2OTOinH2O_res, self.mmH2OTOinHg_res]

		mmHgTO_Label = [self.mmHgTOPa_res, self.mmHgTOkPa_res, self.mmHgTOMPa_res, self.mmHgTOmbar_res, self.mmHgTObar_res, self.mmHgTOatm_res, 
						self.mmHgTOpsi_res, self.mmHgTOkgcm2_res, self.mmHgTOkgm2_res, self.mmHgTONm2_res, self.mmHgTOlbin2_res, self.mmHgTOlbft2_res, 
						self.mmHgTOTorr_res, self.mmHgTOdynecm2_res, self.mmHgTOmmH2O_res, self.mmHgTOmmHg_res, self.mmHgTOinH2O_res, self.mmHgTOinHg_res]

		inH2OTO_Label = [self.inH2OTOPa_res, self.inH2OTOkPa_res, self.inH2OTOMPa_res, self.inH2OTOmbar_res, self.inH2OTObar_res, self.inH2OTOatm_res, 
						 self.inH2OTOpsi_res, self.inH2OTOkgcm2_res, self.inH2OTOkgm2_res, self.inH2OTONm2_res, self.inH2OTOlbin2_res, self.inH2OTOlbft2_res, 
						 self.inH2OTOTorr_res, self.inH2OTOdynecm2_res, self.inH2OTOmmH2O_res, self.inH2OTOmmHg_res, self.inH2OTOinH2O_res, self.inH2OTOinHg_res]

		inHgTO_Label = [self.inHgTOPa_res, self.inHgTOkPa_res, self.inHgTOMPa_res, self.inHgTOmbar_res, self.inHgTObar_res, self.inHgTOatm_res, 
						self.inHgTOpsi_res, self.inHgTOkgcm2_res, self.inHgTOkgm2_res, self.inHgTONm2_res, self.inHgTOlbin2_res, self.inHgTOlbft2_res, 
						self.inHgTOTorr_res, self.inHgTOdynecm2_res, self.inHgTOmmH2O_res, self.inHgTOmmHg_res, self.inHgTOinH2O_res, self.inHgTOinHg_res]

		i = 1
		for item in PaTO_Label:
			output_grid.addWidget(item, 1, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in kPaTO_Label:
			output_grid.addWidget(item, 2, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in MPaTO_Label:
			output_grid.addWidget(item, 3, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in mbarTO_Label:
			output_grid.addWidget(item, 4, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in barTO_Label:
			output_grid.addWidget(item, 5, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in atmTO_Label:
			output_grid.addWidget(item, 6, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in psiTO_Label:
			output_grid.addWidget(item, 7, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in kgcm2TO_Label:
			output_grid.addWidget(item, 8, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in kgm2TO_Label:
			output_grid.addWidget(item, 9, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in Nm2TO_Label:
			output_grid.addWidget(item, 10, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in lbin2TO_Label:
			output_grid.addWidget(item, 11, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in lbft2TO_Label:
			output_grid.addWidget(item, 12, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in TorrTO_Label:
			output_grid.addWidget(item, 13, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in dynecm2TO_Label:
			output_grid.addWidget(item, 14, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in mmH2OTO_Label:
			output_grid.addWidget(item, 15, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in mmHgTO_Label:
			output_grid.addWidget(item, 16, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in inH2OTO_Label:
			output_grid.addWidget(item, 17, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		i = 1
		for item in inHgTO_Label:
			output_grid.addWidget(item, 18, i)
			item.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
			i = i + 1

		output_group.setLayout(output_grid)

		return output_group

	def PaTO_fun(self):
		pass

	def kPaTO_fun(self):
		pass

	def MPaTO_fun(self):
		pass

	def mbarTO_fun(self):
		pass

	def barTO_fun(self):
		pass

	def atmTO_fun(self):
		pass

	def psiTO_fun(self):
		pass

	def kgcm2TO_fun(self):
		pass

	def kgm2TO_fun(self):
		pass

	def Nm2TO_fun(self):
		pass

	def lbin2TO_fun(self):
		pass

	def lbft2TO_fun(self):
		pass

	def TorrTO_fun(self):
		pass

	def dynecm2TO_fun(self):
		pass

	def mmH2OTO_fun(self):
		pass

	def mmHgTO_fun(self):
		pass

	def inH2OTO_fun(self):
		pass

	def inHgTO_fun(self):
		pass


	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()


