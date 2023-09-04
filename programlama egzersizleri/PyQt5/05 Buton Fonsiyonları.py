import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): #QWidget içindeki özellikleri miras alıyor

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        baslik = QtWidgets.QWidget()
        baslik.setWindowTitle("PyQt5 Ders 5")

        self.buton = QtWidgets.QPushButton("Bana Tıkla")
        self.say = 0

        verti_box = QtWidgets.QVBoxLayout()
        verti_box.addWidget(self.buton)
        verti_box.addStretch()

        hori_box = QtWidgets.QHBoxLayout()
        hori_box.addLayout(verti_box)
        hori_box.addStretch()

        self.setLayout(hori_box)

        self.setGeometry(0, 100, 900, 600)

        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):

        self.say += 1
        self.buton.setText(str(self.say) + " kez tıklandı.")

        if self.say == 50:
            self.buton.setText("BOZDUN BOZDUN YETER! ")
            self.say = 0



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())