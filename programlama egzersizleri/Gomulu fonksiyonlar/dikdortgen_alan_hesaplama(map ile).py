"""Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]
"""
def alan_hesapla(tuple):

    return tuple[0]*tuple[1]

liste = [(3,4),(10,3),(5,6),(1,9)]


alan = list(map(alan_hesapla, liste))

print(alan)