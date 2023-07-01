import math
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += r'C:/Users/HP/Desktop/webScraping'
options = webdriver.ChromeOptions();
options.add_argument("--log-level=3");
browser= webdriver.Chrome(options=options)
browser.maximize_window()
browser.get('https://wuzzuf.net/jobs/egypt')
browser.implicitly_wait(5)
job=input('Enter a job name: ')
# inp=browser.find_element(By.XPATH,"//a[@href='https://wuzzuf.net/login?ref=g_menu']")
inp=browser.find_element(By.CLASS_NAME,'search-bar-input').send_keys(job)
search=browser.find_element(By.XPATH,"//button[@class='btn btn-primary search-btn']")
browser.implicitly_wait(3)
search.click()
job_list=[]
# pages=browser.find_elements(By.CLASS_NAME,'css-1q4vxyr')
n=browser.find_element(By.CLASS_NAME,'css-xkh9ud').find_element(By.TAG_NAME,'strong').text.strip()
n=math.ceil(int(n)/15)

for p in range(n):
    # jobs=browser.find_elements(By.CLASS_NAME,"css-1gatmva e1v1l3u10")
    try:
        titles=[title.text.strip() for title in browser.find_elements(By.XPATH,"//h2[@class='css-m604qf']")]
        posted=[posted.find_element(By.TAG_NAME,'div').text.strip() for posted in browser.find_elements(By.CLASS_NAME,"css-d7j1kk")]
        companies=[comp.text.strip()[:-2] for comp in browser.find_elements(By.XPATH,"//a[@class='css-17s97q8']")]
        types=[t.text.strip() for t in browser.find_elements(By.XPATH,"//span[@class='css-1ve4b75 eoyjyou0']")]
        locations=[l.text.strip() for l in browser.find_elements(By.CLASS_NAME,'css-5wys0k')]
        exps=browser.find_elements(By.CLASS_NAME,'css-y4udm8')
        experience=[]
        for exp in exps:
            e=exp.find_elements(By.TAG_NAME,'div')
            experience.append(
                e[-1].text.strip().strip().replace('\n','|')
            )

        urls=[u.find_element(By.CLASS_NAME,'css-o171kl').get_attribute('href') for u in  browser.find_elements(By.CLASS_NAME,'css-m604qf')]
    except:
        print('error occured')
    for i in range(len(urls)):
        browser.get(urls[i])
        try:
            spcs=browser.find_element(By.XPATH,"//section[@class='css-3kx5e2']").find_elements(By.CLASS_NAME,'css-rcl8e5')
            salary=spcs[-1].find_element(By.CLASS_NAME,'css-4xky9y').text.strip().strip()
        except:
            salary='not mentioned'
        try:
            req=''
            reqs=browser.find_element(By.XPATH,"//div[@class='css-1t5f0fr']").text#.find_elements(By.TAG_NAME,'li')
        except:
            req='not mentioned'
        job_list.append(
            {
                    'Title':titles[i],
                    'Company':companies[i],
                    'Location':locations[i],
                    'Post date':posted[i],
                    'Job_type':types[i],
                    'Salary':salary,
                    'link':urls[i],
                    'Requirments':experience[i],
                    'Skills':reqs.replace('\n','|'),
                    
            }
        )
        browser.back()
        
    time.sleep(5)
    try:
        pages=browser.find_elements(By.CLASS_NAME,'css-1q4vxyr')
        if p==1:
            p+=1
        pages[p+1].find_element(By.TAG_NAME,'button').click()
    
        # WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//h2[@class='css-m604qf']")))
        time.sleep(5)
    except:
        print('skipped')

        

        

df=pd.DataFrame(job_list)
df.to_csv('job_list.csv')
print(job_list)
browser.close()