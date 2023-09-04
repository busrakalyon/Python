# 0 1 1 2 3 5 8
a = 0
b = 1

sınır = int(input("Üst tabanı girin --> "))
i = 0
print(a)
print(b)


while i <= sınır:
    c = a + b
    print(c)
    a, b = b, c
    i+=1

