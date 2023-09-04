from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge()

url = "https://twitter.com"

browser.get(url)

time.sleep(3)


giris = browser.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div/span/span")

giris.click()
time.sleep(5)



username = " "#kullanıcı adı

passwrd = " " #şifre

input_ad = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

input_ad.send_keys(username)
time.sleep(3)

ileri = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")

ileri.click()
time.sleep(3)

sifre_gir = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
sifre_gir.send_keys(passwrd)
time.sleep(5)

gir = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")

gir.click()
time.sleep(5)


#arama yap
arama_alani = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
arama_alani.send_keys("@muratduysak_")
time.sleep(5)


arama_butonu = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[2]/div")
arama_butonu.click()
time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

count = 0
while(count <= 3):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    count+=1
time.sleep(5)
tweets = []



elements = browser.find_elements(By.CSS_SELECTOR, '[data-testid="like"]')

for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("Bir sorun oluştu...")


browser.close()








