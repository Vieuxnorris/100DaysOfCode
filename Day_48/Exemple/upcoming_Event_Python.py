from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

driver.get(url="https://www.python.org/")

menu = driver.find_element(by=By.CSS_SELECTOR, value=".medium-widget.last ul")
years = menu.find_elements(by=By.CSS_SELECTOR, value=".event-widget li time")
events = menu.find_elements(by=By.CSS_SELECTOR, value=".medium-widget li > a")

listEvents = {}

for index in range(0, len(events)):
    tempDico = {
        'time': years[index].get_attribute("datetime").split("T")[0],
        'name': events[index].text
    }
    listEvents.update({index: tempDico})

print(listEvents)
driver.quit()