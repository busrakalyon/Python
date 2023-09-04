kelimeler ="programlamaödeviileriseviyeveriyapılarıveobjeleripynb"

harf_kümesi = set()

harfler = dict()

for i in kelimeler:
    if (i in harfler):
        harfler[i] += 1

    else:
        harfler[i] = 1


for harf, sayi in harfler.items():
    print("{} harfi {} defa geçiyor....".format(harf, sayi))

    print("--------------------------------------------------")
