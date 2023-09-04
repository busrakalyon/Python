import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menuler = self.menuBar()

        dosya = menuler.addMenu("Dosya")
        duzenle = menuler.addMenu("Düzenle")

        dosya_ac = QAction("Dosya aç", self)
        dosya_ac.setShortcut("Ctrl+A")

        dosya_kaydet = QAction("Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+K")

        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+C")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        temizle = QAction("Temizle", self)
        temizle.setShortcut("Ctrl+T")

        duzenle.addAction(temizle)

        self.setWindowTitle("Menü oluşturma")

        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)

        self.show()

    def cikis_yap(self):
        qApp.quit()


    def response(selfself, action):

        if action.text() == "Dosya aç":
            print("Dosya açılıyor...")

        elif action.text() == "Kaydet":
            print("Kaydediliyor...")



app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())