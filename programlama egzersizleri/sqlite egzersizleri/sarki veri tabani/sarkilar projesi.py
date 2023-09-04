import time

from sarki_vt import *

beste = Playlist()

while True:
    print("""
    *****************************************
    
    PLAYLIST
    
    1. ŞARKI EKLE
    2. ŞARKI SİL
    3. ŞARKI BUL
    4. PLAYLIST'İ LİSTELE
    5. SANATÇI
    6. ÇIKIŞ İÇİN "-1"    
    
    *****************************************
    \n""")

    islem = int(input("Seç-->"))

    if islem == -1:

        print("Çıkış yapılıyor...")
        time.sleep(2)
        print("Çıkış yapıldı.")
        break

    elif islem == 1:

        sanatci = input("Sanatçının adı: ")
        sarki = input("Şarkı adı: ")
        yil = input("Çıkış yılı: ")

        yeni_single = Sarki(sanatci, sarki, yil)
        print("Yeni eser ekleniyor...")
        time.sleep(1)

        beste.sarki_ekle(yeni_single)

        print("Eser eklendi.")

    elif islem == 2:

        isim = input("Eser ismini girin: ")
        print("Eser siliniyor.")
        time.sleep(1)

        beste.sarki_sil(isim)
        print("Eser silindi.")


    elif islem == 3:

        isim = input("Eser ismini girin: ")
        beste.sarki_bul(isim)


    elif islem == 4:
        beste.listele()

    elif islem == 5:
        sanatci = input("Sanatçının adı: ")

        beste.sanatcinin_sarkilar(sanatci)
    else:
        print("Geçersiz işlem...")

    time.sleep(1)
