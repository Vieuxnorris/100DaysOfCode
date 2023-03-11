import os

from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
