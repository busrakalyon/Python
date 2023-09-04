import modul1

s1 = int(input("iki sayı giriniz:"))
s2 = int(input())

print(modul1.ebob(s1, s2))

sayilar = list(range(1,1001))

for x in sayilar:
    if modul1.mukemmel(x) != 0:
        print(modul1.mukemmel(x), " bir mükemmel sayıdır.")