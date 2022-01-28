from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)

chrome_driver.get('https://www.google.com')
print(chrome_driver.title)
chrome_driver.quit()