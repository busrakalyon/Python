from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Edge()

url = "https://eksisozluk1923.com/mustafa-kemal-ataturk--34712"
browser.get(url)

time.sleep(10)

elements = browser.find_elements(By.CSS_SELECTOR, "div.content")

for i in elements:
    print("****************************************")
    print(i.text)
browser.close()

