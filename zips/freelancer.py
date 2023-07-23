import sys
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from colorama import Fore, init
init(True)
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
    options.add_argument("--headless")
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(link)
    
    return driver
plugins_title=[] 
plugins_version=[]
plugins_last_update=[]
plugins_links=[]
plugins_file_names=[]
themes_title=[] 
themes_version=[]
themes_last_update=[]
themes_links=[]
themes_file_names=[]
# method to get the downloaded file name
def getDownLoadedFileName(driver):
    

    tabs=driver.window_handles
    driver.switch_to.window(tabs[1])
    while True:
        try:
            # get downloaded percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
            # check if downloadPercentage is 100 (otherwise the script will keep waiting)
            if downloadPercentage == 100:
                # return the file name once the download is completed
                return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
        except:
            pass

    # return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")

def scrape_plugin(driver,url,type): # scraping plugin info
    try:
        driver.get(url)
        time.sleep(5)
        try:
            Ptitle=WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.CLASS_NAME,'edd_download_title'))
            )
            if not Ptitle:
                Ptitle='Not Found'
        except:
            Ptitle='Not found'
        try:
            Pversion=driver.find_element(By.XPATH,'//span[@class="pp-list-item-text"]').text.split(':')[1].strip()
            if not Pversion:
                Pversion='Not Found'
        except:
            Pversion='Not found'
        try:
            Pdate=driver.find_element(By.XPATH,'//*[@id="main"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/ul/li[2]/span[2]').text.split(':')[1].strip()
            if not Pdate:
                Pdate='Not found'
        except:
            Pdate='Not found'
        Plink=driver.find_element(By.XPATH,'//a[@aria-label="View Original Product & Demo"]').get_attribute('href')                  
        if not Plink:
            Plink='Not Available'
        #download part#########################################
        # download_btn=driver.find_element(By.XPATH,'//div[@class="edd_download_buy_button"]')
        # download_btn.click()
        try:
            dn=driver.find_element(By.ID,'uc-download-link') ## for page appears when size is too large
            dn.click()
            time.sleep(2)
            # driver.back()
        except:
            pass
            time.sleep(2)
        # get file name #############
        ###################################################
        # file_name=getDownLoadedFileName(driver)
        # time.sleep(2)
        # tabs=driver.window_handles
        # driver.switch_to.window(tabs[0])
        # time.sleep(5)
################################################################
        # print(download_btn.text)
        if type=='plugin':
            
            plugins_title.append(Ptitle.text.strip())
            plugins_version.append(Pversion)
            plugins_last_update.append(Pdate)
            plugins_links.append(Plink)
            # plugins_file_names.append(file_name) uncomment when ready for scraping
        else:
            themes_title.append(Ptitle.text.strip())
            themes_version.append(Pversion)
            themes_last_update.append(Pdate)
            themes_links.append(Plink)
            # themes_file_names.append(file_name) uncomment when ready for scraping
        # driver.back()
    except:
        pass




def scrape_whole_page(driver,inp_list,type):
    for i in range(2):
        scrape_plugin(driver,inp_list[i],type)
        # time.sleep(2)
        
        time.sleep(3)

def scrape_all_pages(driver,type):
    if type=='plugin':
        print(Fore.BLUE + f'[+] {1}/150 plugins page scraped.', end='\r')
        driver.get(f'https://worldpressit.com/plugins-page/page/1/')
        for i in range(2,3): # if number of pages cahanged just change 150 here 
            plugins=[x.get_attribute('href') for x in driver.find_elements(By.XPATH,'//a[@class="pp-post-link"]')]
            scrape_whole_page(driver,plugins,type)
            try:
                driver.get(f'https://worldpressit.com/plugins-page/page/{i}/')
                time.sleep(5)
            except:
                print('finish scrape_all_pages')
                break
            print(Fore.BLUE + f'[+] {i}/150 plugins page scraped.', end='\r')
        print('finish scrape_all_pages')
    else:
        print(Fore.BLUE + f'[+] {1}/65 themes page scraped.', end='\r')
        driver.get(f'https://worldpressit.com/themes-page/page/1/')
        for i in range(2,3):
            themes=[x.get_attribute('href') for x in driver.find_elements(By.XPATH,'//a[@class="pp-post-link"]')]
            scrape_whole_page(driver,themes,type)
            try:
                driver.get(f'https://worldpressit.com/themes-page/page/{i}/')
                time.sleep(5)
            except:
                print('finish scrape_all_pages')
                break
            print(Fore.BLUE + f'[+] {i}/65 themes page scraped.', end='\r')
        print('finish scrape_all_pages')


def main():
    driver =init('https://worldpressit.com/zivdszeb5045yksndcnu/?loggedout=true&wp_lang=en_US')
    driver.execute_script("window.open()")
    tabs=driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.get('chrome://downloads')
    driver.switch_to.window(tabs[0])
    time.sleep(5)
    # myAcc_button=WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/header/div/div[2]/div/div[4]/ul/li[1]/div/a/span'))
    # )
    # myAcc_button.click()
    # time.sleep(3)
    # login_button=driver.find_element(By.CLASS_NAME,'fl-button')
    # login_button.click()
    # time.sleep(5)
    email=driver.find_element(By.ID,'user_login')
    email.send_keys('Pallanti2020@gmail.com')
    time.sleep(2)
    password=driver.find_element(By.ID,'user_pass')
    password.send_keys('Des041122@')
    time.sleep(2)
    sub=driver.find_element(By.ID,'wp-submit')
    sub.click()
    driver.refresh()
    print('logged in successfully')
    time.sleep(5)
    scrape_all_pages(driver,'plugin')
    scrape_all_pages(driver,'themes')

    time.sleep(5)

    df=pd.DataFrame(
        {
            'Category':'plugin',
            'Title':plugins_title,
            'Version':plugins_version,
            'Update Date':plugins_last_update,
            'Links':plugins_links,
            # 'File Name':plugins_file_names
        }
    )
    df.to_csv('plugins.csv',index=False)
    df=pd.DataFrame(
        {
            'Category':'theme',
            'Title':themes_title,
            'Version':themes_version,
            'Update Date':themes_last_update,
            'Links':themes_links,
            # 'File Name':themes_file_names
        }
    )
    df.to_csv('themes.csv',index=False)
    time.sleep(5)
    driver.quit()

# try:
#     main()
# except:
#     print('Something went wrong while scraping')
main()