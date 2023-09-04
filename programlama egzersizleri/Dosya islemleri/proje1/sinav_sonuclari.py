def notlar(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1*(3/10) + not2*(3/10) + not3*(4/10)

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"

with open("ogrenciler.txt", "r", encoding="utf-8") as file:
    ekle = []
    for i in file:
        ekle.append(notlar(i))

    with open("notlar.txt", "w", encoding="utf-8") as file2:
        for i in ekle:
            file2.write(i)

    with open("AA_alanlar.txt", "w", encoding="utf-8") as file3, \
            open("gecenler.txt", "w", encoding="utf-8") as file4, \
            open("kalanlar.txt", "w", encoding="utf-8") as file5:

        for i in ekle:
            if "AA" in i:
                file3.write(i)
            elif "BA" in i or "BB" in i or "CB" in i or "CC" in i:
                file4.write(i)
            else:
                file5.write(i)
