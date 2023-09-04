import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = QLabel("Hangi dili daha çok seviyorsun?")
        self.python = QRadioButton("Python")
        self.java = QRadioButton("Java")
        self.c = QRadioButton("C")
        self.yazdir = QLabel("")
        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.c)
        v_box.addWidget(self.yazdir)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(
            lambda: self.click(self.python.isChecked(), self.java.isChecked(), self.c.isChecked(), self.yazdir))

        self.setWindowTitle("Radio Button")

        self.show()

    def click(self, python, java, c, yazdir):
        if python:
            yazdir.setText("Python")

        elif java:
            yazdir.setText("Java")

        elif c:
            yazdir.setText("C")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
