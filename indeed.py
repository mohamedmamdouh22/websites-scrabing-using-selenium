import math
from getpass import getpass
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options=webdriver.ChromeOptions()
DRIVER_OPTIONS = [
    '--start-maximized',
    "--log-level=3"
    '--disable-popup-blocking',
    "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'",
    # '--headless'
]
for x in DRIVER_OPTIONS:
    options.add_argument(x)
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get('https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flang%3Dar')
inp=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name='text']"))
)
inp.send_keys('mkhalilhoho22@gmail.com')
time.sleep(2)
inp.send_keys(Keys.RETURN)
inp=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name='text']"))
)
inp.send_keys('MohamedKha17347')
time.sleep(2)
inp.send_keys(Keys.RETURN)

pss=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
)
pss.send_keys("iamlegend223mk")
time.sleep(2)
pss.send_keys(Keys.ENTER)
time.sleep(5)
search=driver.find_element(By.XPATH,"//input[@aria-label='Search query']")
search.send_keys('#ahly')
time.sleep(2)
search.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element(By.LINK_TEXT,'Latest').click()
time.sleep(2)
tweets=driver.find_elements(By.XPATH,"//div[@class='css-1dbjc4n r-18u37iz']")

print(tweets[0].find_element(By.CSS_SELECTOR,'.//span').text)
# print(tweets[0].find_element(By.XPATH,"//span[contains(text(),'@')]").text)
time.sleep(2)
driver.quit()