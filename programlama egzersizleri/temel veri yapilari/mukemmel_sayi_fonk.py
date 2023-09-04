#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
# Bunun için bir sayının mükemmel olup olmadığını döndüren bir tane fonksiyon yazın.

def mukemmel(x):
    i = 1
    sum = 0
    while i <= x/2+1:
        if x % i == 0:
            sum += i
        i+=1

    if sum == x:
        return x
    else:
        return 0



sayilar = list(range(1,1001))

for x in sayilar:
    if mukemmel(x) != 0:
        print(mukemmel(x), " bir mükemmel sayıdır.")




