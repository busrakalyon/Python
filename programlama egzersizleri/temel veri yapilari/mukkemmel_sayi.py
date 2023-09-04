sayi = int(input("Bir sayı giriniz:"))

i = 1
toplam = 0

while i<=sayi/2+1:
    if sayi % i == 0:
        print(i)
        toplam+=i
    i += 1

if toplam == sayi:
    print("\n\n{} bir mükemmel sayıdır.".format(sayi))

else:
    print("\n\n{} bir mükemmel sayı değildir.".format(sayi))
