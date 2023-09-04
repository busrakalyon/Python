from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




if __name__ == "__main__":
    username = " "#Kullanıcı adı
    password = " "#şifre

    browser = webdriver.Edge()

    url = "https://www.instagram.com/"
    browser.get(url)
    time.sleep(2)

    kull_adi = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    kull_adi.click()
    kull_adi.send_keys(username)
    time.sleep(5)

    sifre = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    sifre.click()
    sifre.send_keys(password)
    time.sleep(5)

    giris_yap = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
    giris_yap.click()
    time.sleep(10)

    # Profil adını belirleyin
    profile_name = " "#takip ettiklerini çekmek istediğiniz profilin kullanıcı adı
    browser.get(url + profile_name)
    time.sleep(10)

    takip = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    takip.click()
    time.sleep(5)

    jscommand = """
    followers = document.querySelector("._aano");
    followers.scrollTo(0, followers.scrollHeight);
    var lenOfPage=followers.scrollHeight;
    return lenOfPage;

    """
    lenOfPage = browser.execute_script(jscommand)
    match = False
    while (match == False):
        lastCount = lenOfPage
        time.sleep(1)
        lenOfPage = browser.execute_script(jscommand)
        if lastCount == lenOfPage:
            match = True
    time.sleep(5)
    followersList = []

    followers = browser.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")

    for follower in followers:
        followersList.append(follower.text)

    with open("followers.txt", "w", encoding="UTF-8") as file:
        for follower in followersList:
            file.write(follower + "\n")

    browser.close()

