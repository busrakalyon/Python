
sum = 0

while True:
    sayi = input("-->")

    if sayi != 'q':
        sayi = int(sayi)
        sum += sayi

    else:
        break

print("Toplam = ", sum)