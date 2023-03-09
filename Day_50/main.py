import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(url="https://tinder.com/app/recs")
time.sleep(5)

def loginTinder():
    try:
        login = driver.find_element(by=By.XPATH,
                                value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
        login.click()
        time.sleep(1)

        loginFacebook = driver.find_element(by=By.XPATH,
                                        value='/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]')
        loginFacebook.click()
        time.sleep(1)
    except NoSuchElementException:
        print("No application button, skipped.")

def facebookLogin():
    fbLoginWindow = driver.window_handles[1]
    driver.switch_to.window(fbLoginWindow)

    time.sleep(5)
    fbEmail = driver.find_element(by=By.NAME, value="email")
    fbEmail.click()
    fbEmail.send_keys("vieuxnorris@gmail.com")

    fbPassword = driver.find_element(by=By.NAME, value="pass")
    fbPassword.click()
    fbPassword.send_keys("ZiAzEgFnjToozRV3OFpR")

    fbLoginButton = driver.find_element(by=By.NAME, value="login")
    fbLoginButton.click()

    time.sleep(10)

    fbContinue = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div")
    fbContinue.click()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(200)

def tinderSwap():
    allowLocationButton = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    allowLocationButton.click()
    notificationButton = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    notificationButton.click()
    cookies = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    cookies.click()

    for n in range(100):
        time.sleep(1)

        try:
            print('called')
            likeButton = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            likeButton.click()
        except ElementClickInterceptedException:
            try:
                matchPopup = driver.find_element(by=By.CSS_SELECTOR, value=".itsAMatch a")
                matchPopup.click()
            except NoSuchElementException:
                time.sleep(2)


loginTinder()
facebookLogin()
driver.quit()
