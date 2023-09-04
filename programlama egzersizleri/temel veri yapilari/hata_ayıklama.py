liste = ["345", "sadas", "324a", "14", "kemal", "2345", "3ed", "23","2"]

while True:

    for i in liste:
        try:
            i = int(i)
            print(i)
        except ValueError:
            continue

    break
