
def ebob(s1, s2):
    i = 1
    j = 1
    l1 = []
    l2 = []
    l3 = []

    while i <= s1:
        if s1 % i == 0:
            l1.append(i)
        i += 1

    while j <= s2:
        if s2 % j == 0:
            l2.append(j)
        j += 1

    for x in l1:
        for y in l2:
            if x == y:
                l3.append(x)

    print("EBOB: ")
    return l3[-1]


s1 = int(input("iki sayı giriniz:"))
s2 = int(input())

print(ebob(s1, s2))