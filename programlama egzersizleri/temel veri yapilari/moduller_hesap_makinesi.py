import math

while True:
    print(""""
    *************************************
    YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ
    
    Üslü işlemler: 1
    Köklü işlemler: 2
    Logaritma: 3
    Çıkmak için : 0
    
    *************************************
    """)

    islem = int(input("-->"))

    if islem == 1:
        s1 = int(input("Taban: "))
        s2 = int(input("Üs: "))
        print(math.pow(s1, s2))

    elif islem == 2:
        s1 = int(input("Taban: "))

        print(math.sqrt(s1))

    elif islem == 3:
        s1 = int(input("Değer: "))
        s2 = int(input("Taban: "))
        print(math.log(s1,s2))


    elif islem == 0:
        break

    else:
        print("Geçersiz işlem!")