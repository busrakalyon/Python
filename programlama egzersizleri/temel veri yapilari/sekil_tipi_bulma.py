print("Hangi şeklin tipini bulmak istiyorsunuz?\n")
sekil = input("Üçgen için 1, Dörtgen için 2'ye basın.")

if sekil== '1': # üçgen
    k1=int(input("Üçgenin 1. kenarı:"))
    k2 = int(input("Üçgenin 2. kenarı:"))
    k3 = int(input("Üçgenin 3. kenarı:"))


    if (k1==k2==k3):
       print("Bu bir eşkenar üçgendir.")

    elif (k1==k2 or k1==k3 or k2==k3):
       print("Bu bir ikizkenar üçgendir.")

    else:
        print("Bu bir çeşitkenar üçgendir.")

elif sekil== '2':
    k1=int(input("Dörtgenin 1. kenarı:"))
    k2 = int(input("Dörtgenin 2. kenarı:"))
    k3 = int(input("Dörtgenin 3. kenarı:"))
    k4 = int(input("Dörtgenin 4. kenarı:"))
    if k1==k2==k3==k4:
        print("Bu bir karedir.")
    elif (k1==k3 and k2==k4):
        print("Bu bir dikdörtgendir.")
    else:
        print("Bu bir çeşitkenar dörtgendir.")

else:
    print("Hatalı giriş.")