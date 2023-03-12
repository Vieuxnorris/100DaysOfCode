import os
from selenium.webdriver.chrome.service import Service

CHROME_PATH = Service("F:/chrome_driver/chromedriver.exe")
LINK_GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScM_32FuUncjqySQLbapfHYsLbaJCegwJidbjcVhFNWVnX7yw/viewform?usp=sf_link"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8",
}
