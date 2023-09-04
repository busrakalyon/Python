import time

from kutuphane import *

kutuphane = Kutuphane()

while True:
    print("""
    ***********************************************
    
    
    KÜTÜPHANEYE HOŞGELDİNİZ.
    
    İŞLEMLER:
    
    1. Kitapları Göster
    
    2. Kitap Sorgulama
    
    3. Kitap Ekle
    
    4. Kitap Sil 
    
    5. Baskı Yükselt
    
    Çıkmak için '-1' e basın.
    
    
    ***********************************************
    """)

    islem = int(input("Yapmak istediğiniz işlemi seçiniz -->"))
    print("\n")

    if islem == -1:

        print("Çıkış yapılıyor...")
        time.sleep(2)
        print("Çıkış yapıldı.")
        break

    elif islem == 1:

        kutuphane.kitap_bilgileri()
        time.sleep(2)


    elif islem == 2:
        isim = input("Aradığınız kitabın ismini girin: ")
        time.sleep(2)
        kutuphane.sorgula(isim)
        time.sleep(1)


    elif islem == 3:
        isim = input("Kitap adı: ")
        yazar = input("Yazar adı: ")
        sayfa = int(input("Sayfa sayısı: "))
        basim = int(input("Basım: "))

        kitap = Kitap(isim, yazar, sayfa, basim)
        print("Kitap ekleniyor...")

        kutuphane.kitap_ekle(kitap)
        time.sleep(2)
        print("Kitap eklendi.")

        time.sleep(1)

    elif islem == 4:
        isim = input("Kitabın adını giriniz: ")
        print("Kitap siliniyor...")
        time.sleep(2)
        kutuphane.kitap_sil(isim)
        print("Kitap silindi.")

    elif islem == 5:
        isim = input("Kitabın adını giriniz: ")
        kutuphane.basim_guncelle(isim)
        time.sleep(1)

        print("Basım güncellendi.")




