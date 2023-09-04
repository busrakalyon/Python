def mukemmmel_sayi(fonk):

    def wrapper(sayilar):

        sonuc = fonk(sayilar)

        print("Listedeki mükemmel sayılar: ")

        liste = list()

        for i in sayilar:
            k = 1
            toplam = 0

            while k <= i / 2 + 1:
                if i % k == 0:
                    toplam += k

                k += 1
            if toplam == i:
                liste.append(i)


        print(liste)

        print("Kareleri: ")



        return sonuc

    return wrapper

@mukemmmel_sayi
def karesini_bul(sayilar):

    karesi = list()

    for i in sayilar:
        karesi.append(i**2)

    return karesi


print(karesini_bul(range(100)))