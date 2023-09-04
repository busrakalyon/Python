import time

def asal_sayilar():


    liste = []
    for i in range(2,101):

        bol = 2
        asal = True

        while bol < i:
            if i % bol == 0:
                asal = False
                break

            bol+=1

        if asal:
            yield i



generator = asal_sayilar()

for i in generator:
    print(i)
    time.sleep(1)