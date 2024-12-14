from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, Qwidgets,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButoon,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import*
from second_win import*

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.selfLayput(self.Layout_Line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
