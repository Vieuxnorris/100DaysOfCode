import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
itemIds = [item.get_attribute("id") for item in items]

timeOut = time.time() + 5
end = time.time() + 60*5
while True:
    cookie.click()
    if time.time() > timeOut:
        allPrices = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        itemPrices = []

        for price in allPrices:
            elementText = price.text
            if bool(elementText):
                cost = int(elementText.split("-")[1].strip().replace(",", ""))
                itemPrices.append(cost)

        cookieUpgrade = {}
        for n in range(len(itemPrices)):
            cookieUpgrade[itemPrices[n]] = itemIds[n]

        moneyElement = int(driver.find_element(by=By.ID, value="money").text.replace(',', ''))

        affordableUpgrades = {}
        for cost, id in cookieUpgrade.items():
            if moneyElement > cost:
                affordableUpgrades[cost] = id

        try:
            highestPrice = max(affordableUpgrades)
        except ValueError:
            pass
        else:
            purchaseId = affordableUpgrades[highestPrice]
            driver.find_element(by=By.ID, value=purchaseId).click()

        timeout = time.time() + 5

        if time.time() > end:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break
    time.sleep(0.02)
