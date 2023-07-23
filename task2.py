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
#     # options.add_argument("--proxy-server=http://XX X .XX.XX.XX:8080"); 
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
driver = uc.Chrome(options=options)
driver.fullscreen_window()
driver.implicitly_wait(5)
driver.execute_script("window.open('https://www.bet365.com.au/#/AC/B36/C20856562/D48/E360013/F48/')")
time.sleep(2)
driver.execute_script("window.open('https://www.bet365.com.au/#/AC/B36/C20856562/D19/E17358897/F19/I99/');")
time.sleep(5)
driver.delete_all_cookies()
driver.switch_to.window(driver.window_handles[1])
htmlelement= driver.find_element(By.TAG_NAME,'html')

#Scrolls down to the bottom of the page
htmlelement.send_keys(Keys.END)
# wait page to fully load
try:        
  elem = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-MarketGroupButton_Text")))
finally:        
  print('loaded')
time.sleep(2)


# tabs=driver.find_elements(By.CLASS_NAME,'gl-MarketGroupButton_Text')
# # y=1000
# for i in range(len(tabs)):
#   time.sleep(1)
#   tabs[i].click()
#   print(tabs[i].text)
#   time.sleep(2)
 

"""no need of using it. we will directly acess the item through selenium."""
# soup=BeautifulSoup(driver.page_source,'html.parser')
# print(soup)

alltabs= WebDriverWait(driver,50).until(
  EC.presence_of_all_elements_located((By.CLASS_NAME,'gl-MarketGroupButton_Text ')))
print(alltabs)

for tab in alltabs:
  time.sleep(0.5)
  tab.click()



