import time

print("""
****************************
PYTHON BANKASINA HOŞGELDİNİZ
****************************
\n\n""")

class Musteri():

    def __init__(self, isim, tc, bakiye, borc, limit):
        self.isim = isim
        self.tc = tc
        self.bakiye = bakiye
        self.borc = borc
        self.limit = limit

    def para_yatirma(self, y_tutar):
        self.bakiye += y_tutar
        print("Para yatırılıyor...")
        time.sleep(3)
        return "İşleminiz tamamlandı."

    def para_cekme(self, c_tutar):
        self.bakiye -= c_tutar
        print("Hazırlanıyor...")
        time.sleep(3)
        return "Paranızı alabilirsiniz."

    def borc_odeme(self, o_tutar):
        self.borc -= o_tutar
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(3)
        return "İşleminiz tamamlandı."


    def __str__(self):

        return "Hesap Sahibi: {} \nTc: {} \nBakiye: {} \nBorç: {} \nKredi limiti: {}".format(self.isim, self.tc, self.bakiye, self.borc, self.limit)


musteri1 = Musteri("Murat Duysak", 1234, 80000, 500, 45000)
musteri2 = Musteri("Büşra Duysak", 6789, 90000, 2000, 48000)
musteri3 = Musteri("Deniz Bulut", 1230,  2000, 20000,10000)
musteri4 = Musteri("Dursun Durmasın", 4567, 1000, 5000, 30000)

mus = int(input("TC numaranızı giriniz: "))

if mus == musteri1.tc:
    mus = musteri1

elif mus == musteri2.tc:
    mus = musteri2

elif mus == musteri3.tc:
    mus = musteri3

elif tc == musteri4.tc:
    mus = musteri4

else:
    print("Kullanıcı bulunamadı.")

while True:
    print("""
    \nYapmak istediğiniz işlemi seçiniz:
    
    1. Para yatırma
    2. Para çekme
    3. Kredi borcu ödeme
    4. Hesap bilgileri
    5. Çıkış
    
    
    """)

    islem = int(input("-->"))

    if islem == 1:
        y_tutar = int(input("Yatırmak istediğiniz tutarı girin: "))
        print(mus.para_yatirma(y_tutar))

    elif islem == 2:
        c_tutar = int(input("Çekmek istediğiniz tutarı girin: "))
        print(mus.para_cekme(c_tutar))

    elif islem == 3:
        o_tutar = int(input("Ödemek istediğiniz miktarı girin:"))
        print(mus.borc_odeme(o_tutar))

    elif islem == 4:
        print(mus.__str__())
        time.sleep(3)

    elif islem == 5:
        print("İyi günler dileriz.")
        break
    else:
        print("Geçersiz işlem.")
