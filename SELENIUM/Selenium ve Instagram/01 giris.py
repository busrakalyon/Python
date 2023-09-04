from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge()

url = "https://www.instagram.com/"

browser.get(url)
time.sleep(2)

username = " "#kullanıcı adı girilecek
password = " "#şifre girilecek


kull_adi = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
kull_adi.click()
kull_adi.send_keys(username)
time.sleep(5)


sifre = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
sifre.click()
sifre.send_keys(password)
time.sleep(5)


giris_yap = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
giris_yap.click()
time.sleep(5)

browser.close()
