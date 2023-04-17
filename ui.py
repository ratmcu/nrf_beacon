#! /opt/homebrew/bin/python3.8

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
import sys
from random import randint
import time
from essential_generators import DocumentGenerator

from multiprocessing.connection import Client

# while True:
#     c = Client(('localhost', 5023))

#     c.send(f'{int(time.time())}')
#     print('Got:', c.recv())

#     c.send({'a': 123})
#     print('Got:', c.recv())
#     time.sleep(1)



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QHBoxLayout(widget)

        self.text = QLabel('------')
        self.text2 = QLabel('------')
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.text2, alignment=Qt.AlignmentFlag.AlignRight)

        # async_trigger = QPushButton(text="What is the question?")
        # async_trigger.clicked.connect(self.async_start)
        # layout.addWidget(async_trigger, alignment=Qt.AlignmentFlag.AlignCenter)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()
        self.client = Client(('localhost', 5023))
# 

    def update_label(self):
        # self.text.setText(f'{gen.sentence()}')
        self.client.send(" ")
        text = self.client.recv()
        text_parts = text.splitlines()
        if len(text) >= 3 and text_parts[0][:3]=='MAC':
            if text_parts[0][-4:-2] == '66':
                self.text.setText(f'{text_parts[0]},\n {text_parts[1]},\n {text_parts[2]}')
            if text_parts[0][-4:-2] == 'CA':
                self.text2.setText(f'{text_parts[0]},\n {text_parts[1]},\n {text_parts[2]}')


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()