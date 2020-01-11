from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
import time


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(1000, 200, 100, 90)
        self.setWindowTitle("CPS")

        self.click = 0
        self.cps = QLabel("CPS")
        self.cps.setAlignment(Qt.AlignCenter)
        self.timer = QLabel("Time : 0.0")
        tikla = QPushButton("Tıkla")
        sifirla = QPushButton("Sıfırla")

        self.time = None

        v_box = QVBoxLayout()
        v_box.addWidget(self.cps)
        v_box.addWidget(tikla)
        v_box.addWidget(sifirla)
        v_box.addStretch()

        self.setLayout(v_box)

        tikla.clicked.connect(self.clicked)
        sifirla.clicked.connect(self.restarted)

        self.show()

    def clicked(self):
        if self.cps.text() == "CPS":
            self.time = time.time()
            self.click += 1
            self.cps.setText("CPS : 1")

        else:
            self.click += 1
            passtime = (round(time.time(), 3) - round(self.time, 3))
            self.cps.setText("CPS : {} Time : {}".format(str(round(self.click / passtime, 2)), passtime))

    def restarted(self):
        self.time = None
        self.click = 0
        self.cps.setText("CPS")


app = QApplication(sys.argv)
widget = Widget()
sys.exit(app.exec_())
