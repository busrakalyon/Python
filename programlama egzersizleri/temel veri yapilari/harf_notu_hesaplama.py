vize1 = int(input("1. vize notunuzu giriniz:"))
vize2 = int(input("2. vize notunuzu giriniz:"))
final = int(input("Final notunuzu giriniz:"))

t_not = (vize1*30)/100 + (vize2*30)/100 + (final*40)/100

print("Harf notunuz: ")

if t_not >= 90:
    print("AA")

elif t_not >= 85:
    print("BA")

elif t_not >= 80:
    print("BB")

elif t_not >= 75:
    print("CB")

elif t_not >= 70:
    print("CC")

elif t_not >= 65:
    print("DC")

elif t_not >= 60:
    print("DD")

elif t_not >= 55:
    print("FD")

elif t_not > 50:
    print("FF")



