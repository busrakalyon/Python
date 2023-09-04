import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = np.arange(2,11,2)

fig = plt.figure()

#grafik ekleme
axes1 = fig.add_axes([0.1, 0.05, 0.3, 0.3])
axes2 = fig.add_axes([0.1, 0.55, 0.3, 0.3])

axes1.plot(y,x) #y x doğrusu çizimi

axes1.set_xlabel("Lower X")
axes1.set_ylabel("Lower Y")
axes1.set_title("Lower Graph")


axes2.plot(x, y) #x y doğrusu çizimi

axes2.set_xlabel("Upper X")
axes2.set_ylabel("Upper Y")
axes2.set_title("Upper Graph")

"""
axesin içine dört farklı değer yazılıyor.
1. değer figürün soldan ne kadar içeride başladığı
2. değer figürün alttan ne kadar yukarıda başladığı
3. değer figürün x düzleminde ne kadar boyutta olacağı
4. değer figürün y düzleminde ne kadar boyutta olacağı
değerler 0-1 aralığında oluyor
"""


plt.show()