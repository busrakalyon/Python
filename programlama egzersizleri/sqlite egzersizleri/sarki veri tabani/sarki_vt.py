import sqlite3
import time

class Sarki():

    def __init__(self, sanatci, sarki, yil):
        self.sanatci = sanatci
        self.sarki = sarki
        self.yil = yil

    def __str__(self):

        return "Sanatçı: {} \nŞarkı: {} \nYıl: {}" .format(self.sanatci, self.sarki, self.yil)


class Playlist():

    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):
        self.baglanti = sqlite3.connect("sarkilar.db")
        self.islem = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar ( sanatci TEXT, sarki TEXT, yil INT)"

        self.islem.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def sarki_ekle(self, single):

        sorgu = "INSERT INTO sarkilar VALUES (?,?,?)"
        self.islem.execute(sorgu, (single.sanatci, single.sarki, single.yil))

        self.baglanti.commit()

    def sarki_sil(self, sarki):

        sorgu = "DELETE FROM sarkilar WHERE sarki = ?"

        self.islem.execute(sorgu, (sarki,))

        self.baglanti.commit()


    def sarki_bul(self, sarki):

        sorgu = "SELECT * FROM sarkilar WHERE sarki = ?"

        self.islem.execute(sorgu, (sarki,))

        music = self.islem.fetchall()

        if len(music) == 0:
            print("Şarkı mevcut değil.")

        else:
            for i in music:
                parcalar = Sarki(i[0], i[1], i[2])
                print(parcalar)

    def listele(self):

        sorgu = "SELECT * FROM sarkilar"

        self.islem.execute(sorgu)

        liste = self.islem.fetchall()

        for i in liste:
            parcalar = Sarki(i[0], i[1], i[2])
            print(parcalar)

    def sanatcinin_sarkilar(self, sanatci):

        sorgu = "SELECT * FROM sarkilar WHERE sanatci = ?"

        self.islem.execute(sorgu, (sanatci,))

        sarkilari = self.islem.fetchall()

        for i in sarkilari:
            parcalar = Sarki(i[0], i[1], i[2])
            print(parcalar)










