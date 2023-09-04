"""
Checkbox (Onay Kutusu):

- Checkbox, kullanıcının bir ya da birden fazla seçeneği işaretleyebileceği bir kontrol öğesidir.
- Bir listede ya da formda birden fazla seçeneği belirlemek ya da birden fazla seçenek arasından tercih yapmak için kullanılır.
- Seçenekleri bağımsız olarak işaretleyebilir ve işaretsiz bırakabilirsiniz.
- Checkbox, genellikle "evet/hayır" veya "onayla/onaylama" gibi ikili seçenekler için kullanılır.
"""

import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkboxes = []

        self.yaz = QLabel("Yapılacaklar:")
        self.buton = QPushButton("Checkbox ekle")

        v_box = QVBoxLayout()
        v_box.addWidget(self.yaz)
        v_box.addStretch()
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Yapılacaklar Listesi")

        self.buton.clicked.connect(self.checkbox_ekle)

        self.show()


    def checkbox_ekle(self):
        checkbox = QCheckBox("Checkbox", self)
        self.checkboxes.append(checkbox)

        self.layout().addWidget((checkbox))


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())