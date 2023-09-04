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

while pageCount <= 11:

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
    time.sleep(3)
    pageCount+=1


#Dosya açma ve yazdırma
with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry  + "\n")
        file.write("*******************************************\n")
        entryCount += 1



browser.close()