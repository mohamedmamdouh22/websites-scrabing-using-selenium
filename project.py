import math
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
def init(link):                         # driver initialization
    options=webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--log-level=3")
    preferences = {
                    "profile.default_content_settings.popups": 0,
                    "download.default_directory": os.getcwd(),
                    "directory_upgrade": True
                }
    options.add_experimental_option("prefs", preferences)
    # options.add_argument("--headless")
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(link)
    return driver


# def login(email,user,password,driver):
#     inp=WebDriverWait(driver,20).until(
#         EC.presence_of_element_located((By.XPATH,"//input[@name='text']"))
#     )
#     inp.send_keys(email)
#     time.sleep(2)
#     inp.send_keys(Keys.RETURN)
#     try:
#         inp=WebDriverWait(driver,10).until(
#             EC.presence_of_element_located((By.XPATH,"//input[@name='text']"))
#         )
#         inp.send_keys(user)
#         time.sleep(2)
#         inp.send_keys(Keys.RETURN)
#     except:
#         pass

#     pss=WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
#     )
#     pss.send_keys(password)
#     time.sleep(2)
#     pss.send_keys(Keys.ENTER)
#     time.sleep(5)


# def scrape_tweet(card):
#     print(card.find_element(By.XPATH,'.//span').text)
#     print(card.find_element(By.XPATH,".//span[contains(text(),'@')]").text)
#     try:
#         date=card.find_element(By.XPATH,'.//time').get('datetime')
#     except:
#         date='not mentioned'
#     comment=card.find_element(By.XPATH,'.//div[2]').text
#     time.sleep(2)
# driver.execute_script('window.scrollTo(0,doucument.body.scrollHieght)')
def main():
    driver =init('https://gpldeveloper.com/wordpress/wordpress-themes/consultio-consulting-corporate/')
    time.sleep(5)

try:
    main()
except:
    print('Something went wrong while scraping')
