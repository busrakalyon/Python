birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def sayi_okunusu(sayi):
    b2 = sayi // 10
    b1 = sayi % 10

    return (onlar[b2]+ " "+ birler[b1])


sayi = int(input("İki basamaklı bir sayı giriniz:"))
print(sayi_okunusu(sayi))