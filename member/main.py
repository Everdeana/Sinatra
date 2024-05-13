'''
DS
1. AI-HUB
2. Google Dataset Search
3. Roboflow
'''

import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	

from memAdd import MemAddWin
from memdbAdd import MemDbAdd

form_main = uic.loadUiType("ui/main.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수


class MyWindow(QMainWindow, form_main): # 윈도우, ui파일 둘 다 가져옴
	
	searchKin = ''

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.tableWidget = QTableWidget(self.tw_member)
		self.tableWidget.resize(500, 300)
		self.tableWidget.setRowCount(8)
		self.tableWidget.setColumnCount(12)
		self.btn_search.clicked.connect(self.btn_search_clicked)
		self.btn_add.clicked.connect(self.btn_add_clicked)
		self.btn_modify.clicked.connect(self.btn_modify_clicked)
		self.btn_delete.clicked.connect(self.btn_delete_clicked)
		self.btn_close.clicked.connect(self.btn_close_clicked)


	def btn_search_clicked(self):
		if self.le_search.text() == '':
			QMessageBox.about(self, "에러", "입력 값이 존재하지 않습니다.")
			return
		# 간결함을 위해 else를 쓰지 않고 return 후 바로 나감 --> 한 루틴에선 한 가지만 수행
		
		self.searchKin = self.le_search.text()
		print(self.searchKin)
	
	def btn_add_clicked(self):
		memaddWin = MemAddWin()
		memaddWin.showModal()
	def btn_modify_clicked(self):
		print("수정")
	def btn_delete_clicked(self):
		print("삭제")
	def btn_close_clicked(self):
		exit()

		
			
			
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()