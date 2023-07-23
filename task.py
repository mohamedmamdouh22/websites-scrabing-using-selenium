import os
from selenium import webdriver
import time
import math
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

DRIVER_OPTIONS = [
        '--start-maximized',
        "--log-level=3"
        '--disable-popup-blocking',
        "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'",
        '--headless'
    ]
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
# for x in DRIVER_OPTIONS:
#     options.add_argument(x)
#     # options.add_argument("--proxy-server=http://XXX.XX.XX.XX:8080");
#     # options.add_argument("--proxy-bypass-list=https://www.bet365.com");
    
#     driver=webdriver.Chrome(options=options)
#     driver.implicitly_wait(5)
#     stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
#     driver.delete_all_cookies()
#     driver.get(link)
    
#     return driver
titles=[]
labels=[]
odds=[]  
reviews=[]
options=uc.ChromeOptions()
# for option in DRIVER_OPTIONS:
#   options.add_argument(option)
# options.add_argument('--headless')
driver = uc.Chrome()
driver.fullscreen_window()
driver.implicitly_wait(5)

driver.execute_script("window.open('https://www.bet365.com.au/#/AC/B36/C20856562/D48/E360013/F48/')")
time.sleep(2)
driver.execute_script("window.open('https://www.bet365.com/#/AC/B1/C1/D1002/E91422157/G40/');")
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])

# Scrolls down to the bottom of the page

# wait page to fully load
# try:        
#   elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-MarketGroupButton_Text")))
# finally:        
#   print('loaded')
# time.sleep(2)


# tabs=driver.find_elements(By.CLASS_NAME,'gl-MarketGroupButton_Text')
# # y=1000
# for tab in tabs:
#   time.sleep(1)
#   tab.click()
#   print(tab.text)
#   time.sleep(2)
#   tab.click()


time.sleep(10)