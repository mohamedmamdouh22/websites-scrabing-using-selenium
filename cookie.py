from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
os.environ['PATH'] += r'C:/Users/HP/Desktop/webScraping'
driver=webdriver.Chrome(options=options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(5)
c=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.LINK_TEXT,'Got it!'))
)
c.click()
# time.sleep(30)
eng=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'langSelect-EN'))) 
eng.click()
time.sleep(10)
# cookie=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,'bigCookie')))       
cookie=driver.find_element(By.ID,'bigCookie')
count=driver.find_element(By.ID,'cookies')
actions=ActionChains(driver)
items=[driver.find_element(By.ID,'productPrice'+str(i)) for i in range(1,-1,-1)]

for i in range(500):
    actions.click(cookie)
    actions.perform()
    c=int(count.text.split()[0])
    for item in items:
        if c>= int(item.text):
            actions.move_to_element(item)
            actions.click(item)
            actions.perform()
    
# cookie.click()
time.sleep(5)

# driver.quit()