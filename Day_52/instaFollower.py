import time

from utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def findFollowers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header'
                                                                '/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        allButtons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in allButtons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancelButton = self.driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div"
                                                                           "/div/div[3]/button[2]")
                cancelButton.click()
