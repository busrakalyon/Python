import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    tamam = QtWidgets.QPushButton("Tamam")
    iptal = QtWidgets.QPushButton("İptal")

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")

    #yatay ve dikey düzen için nesneleri tanımlıyoruz
    hori_box = QtWidgets.QHBoxLayout()
    verti_box = QtWidgets.QVBoxLayout()

    #addStretch boşluk kontrolü için, üste veya alta yazmak sonucu değiştirir
    hori_box.addStretch()

    hori_box.addWidget(tamam)
    hori_box.addWidget(iptal)
    hori_box.addStretch()

    verti_box.addStretch()
    verti_box.addLayout(hori_box)
    verti_box.addStretch()

    pencere.setLayout(verti_box)

    pencere.setGeometry(0, 100, 900, 600
                        )
    pencere.show()

    sys.exit(app.exec_())  ## bu satır çarpıya basmadan programın sonlanmaması için gerekli


Pencere()