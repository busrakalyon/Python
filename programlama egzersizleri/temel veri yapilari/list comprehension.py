liste1 = list(range(1,101))

liste2 = list()  # veya liste2 = [] ikisi de boş liste oluşturur.

for i in liste1:
    if i % 2 == 0:
        liste2.append(i)  # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.

print(liste2)