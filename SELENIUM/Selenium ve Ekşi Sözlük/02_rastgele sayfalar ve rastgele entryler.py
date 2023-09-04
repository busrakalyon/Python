import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

#url değişikliği!!
url = "https://eksisozluk1923.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:

    #Rastgele sayfaya gider
    randomPage = random.randint(1,2657)

    #rastgele sayfa için yeni url oluşturur
    new_url = url + str(randomPage)

    #sayfadaki entryleri çeker
    elements = browser.find_elements(By.CSS_SELECTOR, "div.content")

    #entryleri listeye ekler
    for i in elements:
        entries.append(i.text)

    browser.get(new_url)
    time.sleep(5)
    pageCount+=1

#entryleri yazdır
for j in entries:
    print("****************************")
    print(str(entryCount) + ".")
    print(j)
    entryCount+=1


browser.close()