from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username = 0 #changeme
password = 0 #changeme

driver = webdriver.Chrome('chromedriver')
driver.get("https://login.aliexpress.com")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe#alibaba-login-box[src^='https://passport.aliexpress.com/mini_login.htm?']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.fm-text#fm-login-id"))).send_keys(username)
driver.find_element_by_css_selector("input.fm-text#fm-login-password").send_keys(password)
driver.find_elements_by_xpath("//*[contains(text(), 'Sign In')]")[0].click()
time.sleep(5)
# Open deliveries
driver.find_element_by_xpath("//*[@class='order-icon i-order-icon']").click()

time.sleep(2)
pages = driver.find_element_by_xpath("//*[@class='ui-label']").text
number_of_pages = int(pages[2:])
print(number_of_pages)

price=[]
purchase_dates=[]
# First page
for element in driver.find_elements_by_xpath("//*[@class='amount-num']"):
    purchase_dates.append(driver.find_element_by_xpath("//*[@class='info-body']").text)
    price.append(float(element.text[2:].replace(',','.')))
time.sleep(1)
for page in range(number_of_pages-1):
    driver.find_element_by_xpath("//*[@class='ui-pagination-next ui-goto-page']").click()
    time.sleep(1)
    for element in driver.find_elements_by_xpath("//*[@class='amount-num']"):
        price.append(float(element.text[2:].replace(',','.')))
        purchase_dates.append(driver.find_element_by_xpath("//*[@class='info-body']").text)
print ('You have spent a total of' + sum(price) + ' euros between' + purchase_dates[-1] +' and ' + purchase_dates[0])
