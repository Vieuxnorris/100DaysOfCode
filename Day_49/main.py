import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.maximize_window()

def loginLinkedin():
    driver.get(url="https://www.linkedin.com/jobs/")

    emailLink = driver.find_element(by=By.NAME, value="session_key")
    emailLink.click()
    emailLink.send_keys(os.getenv("EMAIL"))

    password = driver.find_element(by=By.NAME, value="session_password")
    password.click()
    password.send_keys(os.getenv("PASSWORD"))

    button = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button')
    button.click()

    time.sleep(20)

def searchLinkedin():
    searchjob = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-search-box__inner input[role=combobox]")
    searchjob.click()
    searchjob.send_keys("Python Developer")
    time.sleep(2)
    searchjob.send_keys(Keys.ENTER)
    time.sleep(2)

    easyJobButton = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
    easyJobButton.click()
    time.sleep(3)

def returnlistJobs():
    time.sleep(5)
    listJobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
    for job in listJobs:
        job.click()
        time.sleep(5)
        save = job.find_element(by=By.XPATH, value='//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
        save.click()

        try:
            applyButton = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            applyButton.click()
            time.sleep(5)

            phone = driver.find_element(by=By.CSS_SELECTOR, value="fb-single-line-text__input")
            if phone.text == "":
                phone.send_keys(os.getenv("PHONE"))

            submitButton = driver.find_element(by=By.CSS_SELECTOR, value="footer button")

            if submitButton.get_attribute("data-control-name") == "continue_unity":
                closeButton = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
                closeButton.click()
                time.sleep(2)
                discardButton = driver.find_elements(by=By.CLASS_NAME, value="artdeco-model__confirm-dialog-btn")[1]
                discardButton.click()
                print("Complex application, skipped.")
                continue
            else:
                submitButton.click()

            time.sleep(2)
            closeButton = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            closeButton.click()
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

loginLinkedin()
searchLinkedin()
returnlistJobs()

time.sleep(5)
driver.quit()