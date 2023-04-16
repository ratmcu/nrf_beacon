#! /opt/homebrew/bin/python3.8

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
import sys
from random import randint
import time
from essential_generators import DocumentGenerator
gen = DocumentGenerator()
print(gen.sentence())
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

        layout = QVBoxLayout(widget)

        self.text = QLabel(f'{gen.sentence()}')
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

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
        self.text.setText(f'{self.client.recv()}')


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()