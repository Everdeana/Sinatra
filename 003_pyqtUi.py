import sys # PyQt는 시스템 정보를 사용
from PyQt5.QtWidgets import * # 윈도우 메인(CORE)
from PyQt5 import uic # ui파일 open	


form_main = uic.loadUiType("main.ui")[0] # 여러 개의 윈도우가 생길 수 있으므로 첫 번째 윈도우라는 표시([0]) 필수

class MyWindow(QMainWindow, form_main): # 윈도우, ui파일 둘 다 가져옴
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btn1_clicked)
		self.btn2.clicked.connect(self.btn2_clicked)
		self.btn3.clicked.connect(self.btn3_clicked)
		self.btn4.clicked.connect(self.btn4_clicked)

	def btn1_clicked(self):
		print("버튼 1을 눌렀습니다.")
		QMessageBox.about(self, "message", "button1 clicked")
	def btn2_clicked(self):
		print("버튼 2를 눌렀습니다.")
		QMessageBox.about(self, "message", "button2 clicked")
	def btn3_clicked(self):
		print("버튼 3을 눌렀습니다.")
		QMessageBox.about(self, "message", "button3 clicked")
	def btn4_clicked(self):
		print("버튼 4를 눌렀습니다.")
		QMessageBox.about(self, "message", "button4 clicked")
	
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
	
