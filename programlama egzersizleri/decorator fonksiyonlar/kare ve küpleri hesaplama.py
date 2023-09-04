import time

def kareleri_hesapla(fonksiyon):
    def wrapper(sayılar):
        liste = []

        sonuç = fonksiyon(sayılar)

        for i in sayılar:
            liste.append(i ** 2)
        print("Kareler")
        print(liste)
        print("Küpler")
        return sonuç

    return wrapper


@kareleri_hesapla
def küpleri_hesapla(sayılar):
    sonuç = []

    for i in sayılar:
        sonuç.append(i ** 3)
    return sonuç


print(küpleri_hesapla(range(10)))
