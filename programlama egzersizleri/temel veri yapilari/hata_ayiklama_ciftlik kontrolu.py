import time

def cift():

    liste = [2,4,2,4,6,8,8,8,88,84,2,44,24,42,1,3,5]

    for i in liste:
        time.sleep(1)
        if i % 2 != 0:
            raise ValueError("Sayı tek!")

        else:
            print(i)


cift()



#liste2 = [2, 4,3, 7,2, ,34, 6, 8,9, 8,3, 8, 88, 84, 2, 44, 24, 42, 1, 3, 5]

