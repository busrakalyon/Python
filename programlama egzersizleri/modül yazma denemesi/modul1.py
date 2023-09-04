def mukemmel(x):
    i = 1
    sum = 0
    while i <= x/2+1:
        if x % i == 0:
            sum += i
        i+=1

    if sum == x:
        return x
    else:
        return 0


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

