bas_harfler = list()

with open("siir.txt", "r+", encoding="utf-8") as file:

    satir = file.readline()

    while satir:
        harf = satir[0]
        bas_harfler.append(harf)
        satir = file.readline()

for i in bas_harfler:
    birlestir = ""
    olustur = birlestir.join(bas_harfler)

print(olustur)

