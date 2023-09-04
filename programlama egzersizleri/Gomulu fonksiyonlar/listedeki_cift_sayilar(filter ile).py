"""
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*
"""

def cift_mi(sayi):

    if sayi % 2 == 0:
        return True

    else:
        return False

cift = list(filter(cift_mi, range(1,101)))

print(cift)