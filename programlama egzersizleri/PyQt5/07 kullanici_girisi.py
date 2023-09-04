import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.baglanti_kur()
        self.init_ui()

    def baglanti_kur(self):
        baglanti = sqlite3.connect("veritabani.db")

        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler(kullanici TEXT, parola TEXT)")
    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        #Parolanın görünmemesi için
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.giris_dogrulama = QtWidgets.QLabel("")
        self.yazi1 = QtWidgets.QLabel("Kullanıcı Adı:")
        self.yazi2 = QtWidgets.QLabel("Parola:")

        verti_box = QtWidgets.QVBoxLayout()
        verti_box.addWidget(self.yazi1)
        verti_box.addWidget(self.kullanici_adi)
        verti_box.addWidget(self.yazi2)
        verti_box.addWidget(self.parola)
        verti_box.addWidget(self.giris_dogrulama)
        verti_box.addStretch()
        verti_box.addWidget(self.giris)

        hori_box = QtWidgets.QHBoxLayout()

        hori_box.addStretch()
        hori_box.addLayout(verti_box)
        hori_box.addStretch()

        self.setLayout(hori_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.giris_yap)

        self.show()

    def giris_yap(self):

        ad = self.kullanici_adi.text()
        sifre = self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE kullanici = ? and parola = ?",(ad, sifre))

        veri = self.cursor.fetchall()

        if len(veri) == 0:
            self.giris_dogrulama.setText("Kullanıcı bulunamadı.")

        else:
            self.giris_dogrulama.setText("Hoşgeldiniz " + ad)





app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())







