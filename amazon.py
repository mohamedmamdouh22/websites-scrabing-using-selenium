from bs4 import BeautifulSoup
import requests
import random
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# def webdriver_config(raw_options):

#     try:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("excludeSwitches", ["enable-logging"])
#         options.add_experimental_option(
#             "mobileEmulation", {"deviceName": "Nexus 5"})
#         for option in raw_options:
#             options.add_argument(option)

#         return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     except Exception as e:
        
#         sys.exit(e)

# # webdriver options

# # user_agent_list = [ 
# # 	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
# # 	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
# # 	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 
# # ]
# # for i in range(3):
# #     user_agent=random.choice(user_agent_list)
# DRIVER_OPTIONS = [
#     '--start-maximized',
#     '--disable-popup-blocking',
#     "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'",
#     '--headless'
# ]

# driver=webdriver_config(DRIVER_OPTIONS)
# # source=requests.get('https://www.amazon.com/ref=nav_logo',headers=headers)
# # urls=[]
# driver.get('https://www.amazon.com/iPhone-Pro-256GB-Sierra-Blue/product-reviews/B0BGYFDQJX/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1')
# soup=BeautifulSoup(driver.page_source,'html.parser')
# body=soup.find('body')
# n=body.find('h2',{'class','inline-title'})
# # print(n)
# print(body)
base_url="https://www.amazon.in/s?k="
search_query="titan+men+watches"
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
source=requests.get('https://www.amazon.com/',headers=header)
print(source.text)
# cookie={} # insert request cookies within{}
# def getAmazonSearch(search_query):
#     url=base_url+search_query
#     print(url)
#     page=requests.get(url,cookies=cookie,headers=header)
#     if page.status_code==200:
#         return page
#     else:
#         return "Error"
# product_names=[]
# response=getAmazonSearch(search_query)
# soup=BeautifulSoup(response.content)
# for i in soup.findAll("span",{'class':'a-size-base-plus a-color-base a-text-normal'}): # the tag which is common for all the names of products
#     product_names.append(i.text) #adding the product names to the list