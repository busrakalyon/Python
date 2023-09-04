# Real Madrid, Manchester United, Paris Saint-Germain
def futbolcular(satir):
    satir = satir[:-1]

    liste = satir.split(",")
    isim = liste[0]
    takim = liste[1]

    return isim + "--->" + takim + "\n"

with open("futbolcular.txt","r", encoding="utf-8") as file:
    ekle = []

    for i in file:
        ekle.append(i)

    with open("real_madrid.txt", "w", encoding="utf-8") as file2, \
            open("manchester_united.txt","w", encoding="utf-8") as file3, \
            open("psg.txt", "w", encoding="utf-8") as file4:

 
        for i in ekle:
            if "Real Madrid" in i:
                file2.write(i)

            elif "Manchester United" in i:
                file3.write(i)

            else:
                file4.write(i)


