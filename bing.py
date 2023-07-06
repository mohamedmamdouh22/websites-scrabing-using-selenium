import requests
from bs4 import BeautifulSoup

l=[]
o={}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

for i in range(0,100,10):
    target_url="https://www.bing.com/search?q=sydney&rdr=1&first={}".format(i+1)

    print(target_url)

    resp=requests.get(target_url,headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')

    completeData = soup.find_all("li",{"class":"b_algo"})

    for i in range(0, len(completeData)):
         o["Title"]=completeData[i].find("a").text
         o["link"]=completeData[i].find("a").get("href")
         o["Description"]=completeData[i].find("div",
       {"class":"b_caption"}).text
         o["Position"]=i+1
         l.append(o)
         print(o)
         o={}

# print(l)