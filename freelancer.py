import math
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from saver import collect_zip_file_names
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
    p='C:/Downloads/plugins' # log level    #add you path here
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

def main():
    driver =init('https://www.castrofarmacias.com/')

    time.sleep(10)
    driver.quit()

main()