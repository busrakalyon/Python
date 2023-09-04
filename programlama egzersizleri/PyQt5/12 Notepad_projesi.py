import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        self.setLayout(v_box)

        self.setWindowTitle("Notepad")




class Menu(QMainWindow):

    def __init__(self):

        super().__init__()
        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        self.setWindowTitle("Metin Editörü")

        menuler = self.menuBar()
        dosya = menuler.addMenu("Dosya")

        dosya_ac = dosya.addAction("Dosya aç")
        kaydet = dosya.addAction("Kaydet")
        temizle = dosya.addAction("Temizle")

        cikis = menuler.addMenu("Çıkış")

        cikis1 = cikis.addAction("Çıkış")
        cikis2 = cikis.addAction("Kaydet ve Çık")

        dosya.triggered.connect(self.dosya_islemleri)
        cikis.triggered.connect(self.cikis_islemleri)

        self.show()
    def dosya_islemleri(self, action):
        if action.text() == "Dosya aç":

            dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya aç", os.getenv("DESKTOP"))

            with open(dosya_ismi[0], "r") as file:
                self.pencere.yazi_alani.setText(file.read())

        elif action.text() == "Kaydet":

            dosya_ismi = QFileDialog.getSaveFileName(self, "Kaydet", os.getenv("DESKTOP"))

            with open(dosya_ismi[0], "w") as file:
                file.write(self.pencere.yazi_alani.toPlainText())

        elif action.text() == "Temizle":
            self.pencere.yazi_alani.clear()

    def cikis_islemleri(self, action):

        if action.text() == "Çıkış":

            qApp.quit()

        elif action.text() == "Kaydet ve Çık":

            dosya_ismi = QFileDialog.getSaveFileName(self, "Kaydet", os.getenv("DESKTOP"))

            with open(dosya_ismi[0], "w") as file:
                file.write(self.pencere.yazi_alani.toPlainText())

            qApp.quit()





app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())