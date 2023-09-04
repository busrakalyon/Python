import time
class Kare():

    def __init__(self, limit):
        self.maxi = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.maxi < self.limit:
            self.maxi += 1
            return self.maxi**2



        else:
            raise StopIteration("Sınır aşıldı.")


obje = Kare(5)

iterator = iter(obje)

for i in iterator:
    print(i)
    time.sleep(1)


