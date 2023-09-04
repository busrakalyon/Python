print("""******************************
Vücut Kitle Endeksi Hesaplama
******************************
""")
kilo = float(input("Kilonuzu girin:"))
boy = float(input("Boyunuzu girin(m):"))

vke = kilo / (boy**2)

if vke < 18.5:
    print("Zayıf!")

elif (vke >= 18.5 and vke <= 25):
    print("Normal")

elif (vke > 25 and vke <= 30):
    print("Kilolu")

elif vke > 30:
    print("Obez")

else:
    print("Geçersiz bir sayı girdiniz.")