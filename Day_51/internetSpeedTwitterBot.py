import time

from utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def getInternetSpeed(self) -> dict:
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.maximize_window()

        handleButton = self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
        handleButton.click()

        goButton = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        goButton.click()
        time.sleep(45)

        backResultButton = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/'
                                                                       'div[2]/div[3]/div[3]/div/div[8]'
                                                                       '/div/div/div[2]/a')
        backResultButton.click()
        time.sleep(5)

        self.up = self.driver.find_element(by=By.CSS_SELECTOR, value=".result-data-large.number"
                                                                     ".result-data-value.upload-speed").text
        self.down = self.driver.find_element(by=By.CSS_SELECTOR, value=".result-data-large"
                                                                       ".number.result-data-value.download-speed").text

        return {"down": self.down, "up": self.up}

    def tweetAtProvider(self):
        if float(self.up) < PROMISE_UP or float(self.down) < PROMISE_DOWN:
            self.driver.get(url="https://twitter.com/?logout=1678529873723")
            loginButton = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div[1]/div/div/div/'
                                                                      'div/div/div/div/div[1]/a')
            loginButton.click()
            time.sleep(10)
            emailLogin = self.driver.find_element(by=By.NAME, value="text")
            emailLogin.send_keys(TWITTER_EMAIL)

            nextButton = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/'
                                                                     'div/div/div/div/div/div[2]/div[2]'
                                                                     '/div/div/div[2]/div[2]/div/div/div/div[6]')
            nextButton.click()
            time.sleep(10)
            passwordLogin = self.driver.find_element(by=By.NAME, value="password")
            passwordLogin.send_keys(TWITTER_PASSWORD)
            passwordLogin.send_keys(Keys.ENTER)

            time.sleep(10)

            tweetCompose = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                       'div/div/div/div/div[2]/div/div[2]/div[1]/div/'
                                                                       'div/div/div[2]/div[1]/div/div/div/div/div/div/'
                                                                       'div/div/div/div[1]/div/div/div/div[2]/div/div/'
                                                                       'div/div')
            tweet = f"Hey @VOO, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                f" {PROMISE_DOWN}down/{PROMISE_UP}up"
            tweetCompose.send_keys(tweet)
            time.sleep(3)

            tweetButton = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                      'div/div/div/div/div[2]/div/div[2]/div[1]/'
                                                                      'div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweetButton.click()
            self.driver.quit()
