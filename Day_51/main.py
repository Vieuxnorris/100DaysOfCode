import os
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISE_DOWN = 150
PROMISE_UP = 10
CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

