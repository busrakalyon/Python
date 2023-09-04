import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 3")

    #Buton ekleme
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("BUTON")

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Butona tıklayın...")

    etiket.move(400,100)
    buton.move(400,150)

    #başlangıç en, başlangıç yükseklik, en, boy
    pencere.setGeometry(0,100,900,600)

    pencere.show()

    sys.exit(app.exec_())  ## bu satır çarpıya basmadan programın sonlanmaması için gerekli


Pencere()