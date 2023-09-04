# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
while True:
    sayi1 = int(input("Bir sayı giriniz(çıkmak için -1): "))
    if sayi1 == -1:
        break
    sayi = sayi1
    i = 0
    liste = []
    while sayi != 0:
        b1 = sayi % 10
        liste.append(b1)
        sayi = int(sayi/10)
        i += 1

    sum = 0
    for x in liste:
        sum += x**i
        print(sum)

    if sum == sayi1:
        print("\n\n{} bir armstrong sayısıdır\n\n.".format(sayi1))

    else:
        print("\n\n{} bir armstrong sayısı değildir\n\n.".format(sayi1))
