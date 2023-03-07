from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = Service("F:/chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

driver.get("https://www.amazon.com/ASUS-Maximus-Z790-Hero-ThunderboltTM/dp/B0BG6M53DG/ref=pd_rhf_d_gw_s_pd_crcd_sccl_1_3/146-5057496-5518856?pd_rd_w=c0VhN&content-id=amzn1.sym.840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_p=840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_r=52MG2TR908696XKKD20Q&pd_rd_wg=CfQ62&pd_rd_r=ac4fc71c-ef51-4406-a339-338d707dd9b3&pd_rd_i=B0BG6M53DG&psc=1")
# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(price.text)

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")

# document_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(document_link.text)

# bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()
driver.quit()
