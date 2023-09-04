liste = list(range(1,101))

for x in liste:
    if x % 3 != 0:
        continue
    else:
        print(x)