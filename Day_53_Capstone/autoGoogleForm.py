import time

from zillowBot import ZyllowBot

from utils import CHROME_PATH, LINK_GOOGLE_FORM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoGoogleForm:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_PATH)

    def processAuto(self, bot: ZyllowBot):
        self.driver.get(url=LINK_GOOGLE_FORM)
        self.driver.maximize_window()
        time.sleep(5)

        for index in range(len(bot.prices)):
            address = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.click()
            address.send_keys(bot.address[index])

            price = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.click()
            price.send_keys(bot.prices[index])

            link = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.click()
            link.send_keys(bot.links[index])

            buttonValid = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            buttonValid.click()
            time.sleep(5)
            newButton = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            newButton.click()
            time.sleep(5)
