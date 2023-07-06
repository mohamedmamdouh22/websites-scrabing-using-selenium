import argparse
import csv
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from colorama import Fore, init
from time import sleep

init(True)


# webdriver options
DRIVER_OPTIONS = [
    '--start-maximized',
    '--disable-popup-blocking',
    "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'",
    '--headless'
]

# webdriver configuration function
def webdriver_config(raw_options):

    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option(
            "mobileEmulation", {"deviceName": "Nexus 5"})
        for option in raw_options:
            options.add_argument(option)

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    except Exception as e:
        print(Fore.RED + "[ERROR] Error occurred during the chrome driver configuration.")
        sys.exit(e)


# scraping phase function
def bing_scrape(driver):
    
    try:

        query = ('https://www.bing.com/search?q=Rollins%20Inc%202170%20Piedmont%20Rd%20NE%20Atlanta%20GA%2030324').replace(' ', '%20').replace('&', '%26')
        print(query)

        driver.get(query)
        sleep(6)

        # soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        soup1 = BeautifulSoup(driver.page_source, 'lxml')
        body = soup1.find("body")
        b_content = body.find("div", {"id": "b_content"})
        b_context = b_content.find("ol", {"id": "b_context"})
        
        title=b_content.find('aside')
        # b_context=body.select_one('div.infoModule  div.b_factrow')

        b_results = b_content.find("ol", {"id": "b_results"})
        print(title)
        # if b_context:
        #     # print("b_context = " + b_context)
        #     print(b_context)
        # else:
        #     print("b_context not found")

        if b_results:
            print("b_results found")
        else:
            print("b_results not found")

        driver.quit()

    except Exception as e:
        print(Fore.RED + "[ERROR] Error occurred during the scraping process.")
        sys.exit(e)

# MAIN FUNCTION
def main():
    driver = webdriver_config(DRIVER_OPTIONS)
    result = bing_scrape(driver)


if __name__ == "__main__":
    main()
