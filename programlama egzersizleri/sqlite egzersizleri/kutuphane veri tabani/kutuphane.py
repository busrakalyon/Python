import sqlite3

import time

class Kitap():
    def __init__(self, isim, yazar, sayfa, basim):
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.basim = basim

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nSayfa sayısı: {}\nBasım: {}\n".format(self.isim, self.yazar, self.sayfa, self.basim)


class Kutuphane():

    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):

        self.baglanti = sqlite3.connect("kutuphane.db")

        self.imlec = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,sayfa INT,baskı INT)"

        self.imlec.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):

        self.baglanti.close()

    def kitap_bilgileri(self):

        sorgu = "SELECT * FROM kitaplar"

        self.imlec.execute(sorgu)
        kitaplar = self.imlec.fetchall()

        if len(kitaplar) == 0:
            print("Kütüphanede henüz bir kitap bulunmuyor...")

        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3])
                print(kitap)


    def sorgula(self, isim):

        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"

        self.imlec.execute(sorgu,(isim,))

        kitaplar = self.imlec.fetchall()

        if (len(kitaplar) == 0):
            print("Kitap bulunamadı...")

        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3])
            print(kitap)

    def kitap_ekle(self, kitap):
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?)"

        self.imlec.execute(sorgu,(kitap.isim, kitap.yazar, kitap.sayfa, kitap.basim))

        self.baglanti.commit()

    def kitap_sil(self, isim):

        sorgu = "DELETE FROM kitaplar WHERE isim = ?"

        self.imlec.execute(sorgu, (isim,))
        self.baglanti.commit()

    def basim_guncelle(self,isim):

        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"

        self.imlec.execute(sorgu,(isim,))

        kitaplar = self.imlec.fetchall()


        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")

        else:
            basim = kitaplar[0][3]
            basim +=1

            sorgu2 = "UPDATE kitaplar SET basim = ? WHERE isim = ?"

            self.imlec.execute(sorgu2, (basim, isim))

            self.baglanti.commit()

