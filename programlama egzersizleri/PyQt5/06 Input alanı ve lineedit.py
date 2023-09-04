import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): #QWidget içindeki özellikleri miras alıyor

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        baslik = QtWidgets.QWidget()
        baslik.setWindowTitle("PyQt5 Ders 6")

        #İnput alma alanı
        self.yazi_alani = QtWidgets.QLineEdit()

        self.sil = QtWidgets.QPushButton("Temizle")
        self.yaz = QtWidgets.QPushButton("Yazdır")

        verti_box = QtWidgets.QVBoxLayout()

        verti_box.addWidget(self.yazi_alani)
        verti_box.addWidget(self.sil)
        verti_box.addWidget(self.yaz)
        verti_box.addStretch()

        self.setLayout(verti_box)

        self.setGeometry(0, 100, 900, 600)

        self.sil.clicked.connect(self.click)
        self.yaz.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_alani.clear()
        else:
            print(self.yazi_alani.text())



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())