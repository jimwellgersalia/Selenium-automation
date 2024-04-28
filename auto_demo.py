from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# to prevent chrome from automatic closing
options.add_experimental_option("detach", True)
# we also dont need to defined the exe_path, just make sure that driver is in the System PATH
service = ChromeService(executable_path='./chromedriver.exe')
chrome_browser = webdriver.Chrome(service=service, options=options)

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")


get_total_button = chrome_browser.find_element(
    By.CSS_SELECTOR, '#gettotal > .btn')
value1 = chrome_browser.find_element(By.ID, 'value1')
value2 = chrome_browser.find_element(By.ID, 'value2')
value1.clear()
value2.clear()

time.sleep(2)
value1.send_keys('100')
value2.send_keys('250')
get_total_button.click()

chrome_browser.close()
