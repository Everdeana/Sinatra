from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	
from PyQt5.QtGui import *
from memdbAdd import MemDbAdd


memAddMain = uic.loadUiType("ui/mem_add.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MemAddWin(QDialog, memAddMain): # 윈도우, ui파일 둘 다 가져옴 (DIalog로 생성된 ui파일)

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn_add.clicked.connect(self.btn_add_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)

	

	def btn_add_clicked(self):
		if (self.le_mail.text() == '' or 
	  		self.le_name.text() == '' or 
			self.le_telno.text() == '' or
			self.le_addr.text() == '' ):
			QMessageBox.about(self, "에러", "필수 입력사항을 입력해주세요!!!.")
			return
		# 간결함을 위해 else를 쓰지 않고 return 후 바로 나감 --> 한 루틴에선 한 가지만 수행
		
		MemDbAdd(self.le_mail.text(), self.le_name.text(), self.le_telno.text(), self.le_addr.text(), self.le_sns.text())
		'''
		print(self.memMail)
		print(self.memName)
		print(self.memTelno)
		print(self.memAddr)
		print(self.memSns)
		'''
		

	def btn_close_clicked(self):
		self.close() # 자기 자신만 종료
	
	def showModal(self):
		return super().exec_() # 화면 출력
