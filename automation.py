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

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
# print(button.get_attribute('innerHTML'))

user_button2 = chrome_browser.find_element(
    By.CSS_SELECTOR, '#get-input > .btn')
# find all the form with id get-input which btn is its child
print(user_button2)

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()


time.sleep(2)
user_message.send_keys('I am extra cool')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I am extra cool' in output_message.text
