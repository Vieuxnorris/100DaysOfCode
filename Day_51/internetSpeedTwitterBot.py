from Utils import *
from selenium import webdriver
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def getInternetSpeed(self) -> tuple:
        return (self.down, self.up)

    def tweetAtProvider(self) -> str:
        return f"#VOO my internet speed Down -> {self.down} and my Up -> {self.up}"