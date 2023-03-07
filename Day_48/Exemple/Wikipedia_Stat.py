import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

articleCount = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# articleCount.click()

EnglishPortal = driver.find_element(by=By.LINK_TEXT, value="English")
# EnglishPortal.click()
time.sleep(5)

search = driver.find_element(by=By.NAME, value="search")
search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)


time.sleep(5)