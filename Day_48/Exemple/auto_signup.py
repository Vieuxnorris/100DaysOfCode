import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(url="https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element(by=By.NAME, value="fName")
firstName.click()
firstName.send_keys("Test")
firstName.send_keys(Keys.ENTER)

lastName = driver.find_element(by=By.NAME, value="lName")
lastName.click()
lastName.send_keys("Test2")
lastName.send_keys(Keys.ENTER)

email = driver.find_element(by=By.NAME, value="email")
email.click()
email.send_keys("Test3@gmail.com")
email.send_keys(Keys.ENTER)

button = driver.find_element(by=By.TAG_NAME, value="button")
button.click()

time.sleep(5)
driver.quit()