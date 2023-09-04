import sys
from PyQt5 import QtWidgets, QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PYTHON ile PyQt5")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)

    etiket1.setText("RICK")
    etiket2.setPixmap(QtGui.QPixmap("rick.png"))

    etiket1.move(350,40) #etiketlerin sayfanın neresinde yer alacağını belirtiyoruz
    etiket2.move(1,100)


    pencere.setGeometry(500,500,500,500) #Açılan pencerenin konumu

    pencere.show()

    sys.exit(app.exec_())


Pencere()

