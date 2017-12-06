#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QPushButton, QMessageBox, QAction, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from DetectFace import face_detection
from DetectGest import gest_recognition

class App(QMainWindow): #QWidget
	def __init__(self):
		super().__init__()
		self.title = "GestFace - A Gesture/Facial Detector"
		self.left = 400
		self.top = 100
		self.width = 640
		self.height = 480
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.center()

		fd_button = QPushButton("Face Detection", self)
		fd_button.setToolTip("Detect <b>Faces</b> and <b>Eyes</b>")
		fd_button.resize(fd_button.sizeHint())
		fd_button.move(170, 180)
		fd_button.clicked.connect(self.on_click)

		fd_button = QPushButton("Gesture Recognition", self)
		fd_button.setToolTip("Detect <b>Gestures</b>")
		fd_button.resize(fd_button.sizeHint())
		fd_button.move(300, 180)
		fd_button.clicked.connect(self.on_click)

		#fd_button = QPushButton("Train Gesture", self)
		#fd_button.setToolTip("Detect <b>Faces</b> and <b>Eyes</b>")
		#fd_button.resize(fd_button.sizeHint())
		#fd_button.move(330, 200)
		#fd_button.clicked.connect(self.on_click)

		q_button = QPushButton("Exit (Esc)", self)
		q_button.setToolTip("Quit")
		q_button.resize(fd_button.sizeHint())
		q_button.move(220, 300)
		q_button.clicked.connect(QCoreApplication.instance().quit)

		self.quit_shortcut = QShortcut(QKeySequence("Esc"), self)
		self.quit_shortcut.activated.connect(QCoreApplication.instance().quit)

		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	@pyqtSlot()
	def on_click(self):
		sender = self.sender()
		if sender.text() == "Face Detection":
			self.statusBar().showMessage(sender.text())
			face_detection()
		elif sender.text() == "Gesture Recognition":
			self.statusBar().showMessage(sender.text())
			gest_recognition()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Alert', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
