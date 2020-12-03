# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

from PyQt5 import QtWidgets, QtGui, QtCore
import sys



class Pressdrl_Win(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.setWindowTitle("Pressure Drop per Length Converter")
		self.setWindowIcon(QtGui.QIcon("logo.jpg"))
		
		self.main_window()

	def createGroup_input(self):
		input_group = QtWidgets.QGroupBox("Input", self)
		input_group.setFont(QtGui.QFont("Arial", 10))

		input_grid = QtWidgets.QGridLayout()
		input_grid.setColumnMinimumWidth(0, 130)

		blanklabel           = QtWidgets.QLabel()
		self.Pami_LinEd      = QtWidgets.QLineEdit()
		self.kPa100mi_LinEd  = QtWidgets.QLineEdit()
		self.psifti_LinEd    = QtWidgets.QLineEdit()
		self.psi100fti_LinEd = QtWidgets.QLineEdit()

		LinEd_list = [self.Pami_LinEd, self.kPa100mi_LinEd, self.psifti_LinEd, self.psi100fti_LinEd]

		Label_list = [blanklabel, "Pa/m", "kPa/100m", "psi/ft", "psi/100ft"]
		
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

		return input_group

	def createGroup_output(self):
		output_group = QtWidgets.QGroupBox("Output", self)
		output_group.setFont(QtGui.QFont("Arial", 10))

		output_grid = QtWidgets.QGridLayout()

		Label_list = ["Pa/m", "kPa/100m", "psi/ft", "psi/100ft"]
		i = 0

		for item in Label_list:
			Label_name = QtWidgets.QLabel(item)
			output_grid.addWidget(Label_name, 0, i)
			i = i + 1

		self.PamTOPam_res      = QtWidgets.QLabel("0", self)
		self.PamTOkPa100m_res  = QtWidgets.QLabel("0", self)
		self.PamTOpsift_res    = QtWidgets.QLabel("0", self)
		self.PamTOpsi100ft_res = QtWidgets.QLabel("0", self)

		output_grid.addWidget(self.decimalTOdecimal_res, 1, 0)
		output_grid.addWidget(self.decimalTOpercent_res, 1, 1)
		output_grid.addWidget(self.decimalTOpromile_res, 1, 2)
		output_grid.addWidget(self.decimalTOppm_res,     1, 3)
		output_grid.addWidget(self.decimalTOppb_res,     1, 4)

		output_grid.addWidget(self.percentTOdecimal_res, 2, 0)
		output_grid.addWidget(self.percentTOpercent_res, 2, 1)
		output_grid.addWidget(self.percentTOpromile_res, 2, 2)
		output_grid.addWidget(self.percentTOppm_res,     2, 3)
		output_grid.addWidget(self.percentTOppb_res,     2, 4)

		output_grid.addWidget(self.promileTOdecimal_res, 3, 0)
		output_grid.addWidget(self.promileTOpercent_res, 3, 1)
		output_grid.addWidget(self.promileTOpromile_res, 3, 2)
		output_grid.addWidget(self.promileTOppm_res,     3, 3)
		output_grid.addWidget(self.promileTOppb_res,     3, 4)

		output_grid.addWidget(self.ppmTOdecimal_res, 4, 0)
		output_grid.addWidget(self.ppmTOpercent_res, 4, 1)
		output_grid.addWidget(self.ppmTOpromile_res, 4, 2)
		output_grid.addWidget(self.ppmTOppm_res,     4, 3)
		output_grid.addWidget(self.ppmTOppb_res,     4, 4)

		output_grid.addWidget(self.ppbTOdecimal_res, 5, 0)
		output_grid.addWidget(self.ppbTOpercent_res, 5, 1)
		output_grid.addWidget(self.ppbTOpromile_res, 5, 2)
		output_grid.addWidget(self.ppbTOppm_res,     5, 3)
		output_grid.addWidget(self.ppbTOppb_res,     5, 4)

		output_group.setLayout(output_grid)

		self.decimali_LinEd.returnPressed.connect(self.decimalTO_fun)
		self.percenti_LinEd.returnPressed.connect(self.percentTO_fun)
		self.promilei_LinEd.returnPressed.connect(self.promileTO_fun)
		self.ppmi_LinEd.returnPressed.connect(self.ppmTO_fun)
		self.ppbi_LinEd.returnPressed.connect(self.ppbTO_fun)

		return output_group

	def decimalTO_fun(self):
		try:
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
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def percentTO_fun(self):
		try:
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
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()
	

	def promileTO_fun(self):
		try:
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
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ppmTO_fun(self):
		try:
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
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def ppbTO_fun(self):
		try:
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
		
		except:
			zprava = QtWidgets.QMessageBox()
			zprava.setIcon(QtWidgets.QMessageBox.Warning)
			zprava.setWindowTitle("Error input")
			zprava.setText("Number is unknown. Please, check your input.\n" "Allowed variations are eg. 1.1e-2; 1.1E-2; 0.01")
			zprava.setStandardButtons(QtWidgets.QMessageBox.Ok)

			return zprava.exec()


	def main_window(self):
		main_layout = QtWidgets.QHBoxLayout()
		main_layout.addWidget(self.createGroup_input())
		main_layout.addWidget(self.createGroup_output())

		self.setLayout(main_layout)
		self.show()

aplikace = QtWidgets.QApplication(sys.argv)
aplikace.setStyle("Fusion")	
