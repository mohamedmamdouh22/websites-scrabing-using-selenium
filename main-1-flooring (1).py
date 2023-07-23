import argparse
import csv
import re
import time
import os
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from colorama import Fore, init
import requests
init(True)

# argparse config
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', metavar="INPUT_PATH",
                    help="input csv file absolute path", required=True)
parser.add_argument('-o', '--output', metavar="OUTPUT_PATH",
                    help="output csv file absolute path (default is output.csv in the current folder)", default=os.path.join(os.getcwd(), 'output.csv'), required=False)
parsed_args = parser.parse_args()

#handle errors in the initial arguments
def parser_error(type):
    parser.print_help()
    if type == 'input':
        sys.exit(Fore.RED+'\n[ERROR] The input file dont exist!')
    if type == 'output':
        sys.exit(Fore.RED+'\n[ERROR] The output file already exists or the path is invalid!')


# read parsed_args
INPUT_PATH = parsed_args.input if os.path.exists(
    parsed_args.input) else parser_error('input')
OUTPUT_PATH = parsed_args.output if os.path.exists(os.path.dirname(parsed_args.output)) and not os.path.exists(
    parsed_args.output) else parser_error('output')


# read input file function
def read_input(path):

    try:
        place_list = []
        input_file = open(path, 'r', encoding='utf8')
        raw_data = csv.reader(input_file, delimiter=";")
        for index, row in enumerate(raw_data):
            place_list.append(row)
        csv_header = place_list[0]
        place_list.remove(place_list[0])
        input_file.close()
        return place_list, csv_header

    except Exception as e:
        print(Fore.RED + "[ERROR] Error occurred during the input file reading.")
        sys.exit(e)


# webdriver options
DRIVER_OPTIONS = [
    '--start-maximized',
    '--disable-popup-blocking',
    "--user-agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36'",
    '--headless'
]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

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
def bing_scrape(driver, place_list):
    
    try:

        result = place_list[0:2]

        for index, place in enumerate(place_list[:2]):

            data = [None] * 29

            try:
                data[2] = False
                data[3] = False
                data[4] = False
                data[5] = False
                data[6] = False
                data[7] = False
                data[8] = False
                data[9] = False
                data[10] = False
                data[11] = False
                data[12] = False
                data[13] = False
                data[14] = False
                data[15] = False            	
                data[16] = False
                data[17] = False
                data[18] = False
                data[19] = False
                data[20] = False
                data[21] = False
                data[22] = False
                data[23] = False
                data[24] = False
                data[25] = False
                data[26] = False
                data[27]=None
                data[28]=None

                query = 'http://{}'.format(place[6])
                # print(query)

                driver.get(query)

                # wait page to fully load or past 6 seconds
                timer = time.time()
                while time.time() - timer < 6:
                    try:
                        if driver.find_element(By.XPATH, '//*[@id="mHamburger"]'):
                            break
                    except:
                        pass

                soup1 = BeautifulSoup(driver.page_source, 'html.parser')
                body = soup1.find("body")

                title_tag = soup1.find('title')
                title = title_tag.text.strip() if title_tag else  None
                data[0] = title
                
                try:
                    description_tag = soup1.find('meta', attrs={'property': 'og:description'})
                    if description_tag:
                        description=description_tag.get('content')
                except:
                    try:
                        description_tag2=soup1.find('meta',{'name':'description'})
                        description=description_tag2.get('content')
                    except:
                        pass
                data[1] = description if description else None
                
                    
                
                try:
                    phone_cap=soup1.find("a", href=re.compile("tel:"))
                     # search for a tag with tel in its href
                    phone=phone_cap.text.strip()
                    phone=re.search('\(?\d{3}\)?[-\.\s]?\d{3}[-\.]\d{4}',phone).group()
                    
                except:
                    ## if not found then grab it from body
                    phone_cap= title_tag.find(string=re.compile('\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}'))
                    if phone_cap:
                        phone=re.search('\(?\d{3}\)?[-\.\s]?\d{3}[-\.]\d{4}',phone_cap).group()
                    elif description_tag.find(string=re.compile('\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}')):
                        phone_cap=description_tag.find(string=re.compile('\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}'))
                        phone=re.search('\(?\d{3}\)?[-\.\s]?\d{3}[-\.]\d{4}',phone_cap).group()
                    else:
                        phone_cap=body.find(string=re.compile('\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}'))
                        phone=re.search('\(?\d{3}\)?[-\.\s]?\d{3}[-\.]\d{4}',phone_cap).group()
                if phone_cap and not re.match('^\([0-9]{3}\)?\s?[0-9]{3}-[0-9]{4}$',phone): ## adjust format
                    phone=f"({phone[0:3]}) {phone[4:7]}-{phone[8:]}"
                # print(phone)
                data[27]=phone


                name_list=place[0].split()
                comp_name=place[0]
                company_name=soup1.find(string=re.compile(comp_name,re.IGNORECASE))
                if company_name: ## excact match
                    data[28]=comp_name
                    # print(comp_name)
                else: 
                    comp_name=' '.join(name_list[:-1])
                    i=2
                    while comp_name:
                        company_name=soup1.find(string=re.compile(comp_name.strip(),re.IGNORECASE)) ## reomve last word and search
                        if company_name:
                            data[28]=comp_name
                            break
                        comp_name=' '.join(name_list[:-i])
                        i+=1

                email=body.find(string=re.compile('\S{1,}@\S{1,}.\S{1,3}'))
                
                #\S{1,}@\S{1,}.\S{1,3}
                
                s1 = soup1.find_all(string=  re.compile('Hardwood',re.IGNORECASE))
                s2 = soup1.find_all(string = re.compile('Unfinished',re.IGNORECASE))
                s3 = soup1.find_all(string = re.compile('Sanding',re.IGNORECASE))
                s4 = soup1.find_all(string = re.compile('Refinishing',re.IGNORECASE))
                s5 = soup1.find_all(string = re.compile('Engineered',re.IGNORECASE))
                s6 = soup1.find_all(string = re.compile('Laminate',re.IGNORECASE))
                s7 = soup1.find_all(string = re.compile('Bamboo',re.IGNORECASE))
                s8 = soup1.find_all(string = re.compile('Cork',re.IGNORECASE))
                s9 = soup1.find_all(string = re.compile('Vinyl Flooring',re.IGNORECASE))
                s10 = soup1.find_all(string = re.compile('PVC',re.IGNORECASE))
                s11 = soup1.find_all(string = re.compile('Luxury Vinyl',re.IGNORECASE))
                s12 = soup1.find_all(string = re.compile('LVP',re.IGNORECASE))
                s13 = soup1.find_all(string = re.compile('LVT',re.IGNORECASE))
                s14 = soup1.find_all(string = re.compile('Tile',re.IGNORECASE))
                s15 = soup1.find_all(string = re.compile('Ceramic',re.IGNORECASE))
                s16 = soup1.find_all(string = re.compile('Porcelain',re.IGNORECASE))
                s17 = soup1.find_all(string = re.compile('Natural Stone',re.IGNORECASE))
                s18 = soup1.find_all(string = re.compile('Carpet',re.IGNORECASE))
                s19 = soup1.find_all(string = re.compile('Rugs',re.IGNORECASE))
                s20 = soup1.find_all(string = re.compile('Concrete',re.IGNORECASE))
                s21 = soup1.find_all(string = re.compile('Polishing',re.IGNORECASE))
                s22 = soup1.find_all(string = re.compile('Installation',re.IGNORECASE))
                s23 = soup1.find_all(string = re.compile('Commercial',re.IGNORECASE))

                if s1:
                    data[2] = True
                if s2:
                    data[3] = True
                if s3:
                    data[4] = True
                if s4:
                    data[5] = True
                if s5:
                    data[6] = True
                if s6:
                    data[7] = True
                if s7:
                    data[8] = True
                if s8:
                    data[9] = True
                if s9:
                    data[10] = True
                if s10:
                    data[11] = True
                if s11:
                    data[12] = True
                if s12:
                    data[13] = True
                if s13:
                    data[14] = True
                if s14:
                    data[15] = True
                if s15:
                    data[16] = True
                if s16:
                    data[17] = True
                if s17:
                    data[18] = True
                if s18:
                    data[19] = True
                if s19:
                    data[20] = True
                if s20:
                    data[21] = True
                if s21:
                    data[22] = True
                if s22:
                    data[23] = True
                if s23:
                    data[24] = True

                requery = soup1.find('div', {"id": "sp_requery"})
                data[25] = "" if not requery else requery.text
            except:
                data[26] = True

            result[index].append(data[0])
            result[index].append(data[1])
            result[index].append(data[2])
            result[index].append(data[3])
            result[index].append(data[4])
            result[index].append(data[5])
            result[index].append(data[6])
            result[index].append(data[7])
            result[index].append(data[8])
            result[index].append(data[9])
            result[index].append(data[10])
            result[index].append(data[11])
            result[index].append(data[12])
            result[index].append(data[13])
            result[index].append(data[14])
            result[index].append(data[15])
            result[index].append(data[16])
            result[index].append(data[17])
            result[index].append(data[18])
            result[index].append(data[19])
            result[index].append(data[20])
            result[index].append(data[21])
            result[index].append(data[22])
            result[index].append(data[23])
            result[index].append(data[24])
            result[index].append(data[25])
            result[index].append(data[26])
            result[index].append(data[27])
            result[index].append(data[28])
            print(Fore.BLUE + f'[+] {index+1}/{len(result)} business scraped.', end='\r')
            # print(Fore.BLUE + f'[+] {index+1}/{len(result)} business scraped.')
        driver.quit()
        return result

    except Exception as e:
        print(Fore.RED + "[ERROR] Error occurred during the scraping process.")
        sys.exit(e)


# file writing function
def write_csv(arr, path, header):
    try:
        output_file = open(path, 'w', newline='', encoding='utf-8')
        writer = csv.writer(output_file, delimiter=';')

        header.append('Address')
        header.append('City')
        header.append('State')
        header.append('Zip')
        header.append('Phone')
        header.append('Website')
        header.append('Meta Title')
        header.append('Meta Description')
        header.append('Hardwood')
        header.append('Unfinished')
        header.append('Sanding')
        header.append('Refinishing')
        header.append('Engineered')
        header.append('Laminate')
        header.append('Bamboo')
        header.append('Cork')
        header.append('Vinyl Flooring')
        header.append('PVC')
        header.append('Luxury Vinyl')
        header.append('LVP')
        header.append('LVT')
        header.append('Tile')
        header.append('Ceramic')
        header.append('Porcelain')
        header.append('Natural Stone')
        header.append('Carpet')
        header.append('Rugs')
        header.append('Concrete')
        header.append('Polishing')
        header.append('Installation')
        header.append('Commercial')
        header.append('Requery')
        header.append('Error')
        header.append('Phone')
        header.append('Company name')

        writer.writerow(header)

        for row in arr:
            writer.writerow(row)

        print(Fore.GREEN + f"[+] File stored at {path}")
        output_file.close()

    except Exception as e:
        print(Fore.RED + "[ERROR] Error occurred during the csv writing process.")
        sys.exit(e)


# MAIN FUNCTION
def main():
    driver = webdriver_config(DRIVER_OPTIONS)
    content, csv_header = read_input(INPUT_PATH)
    result = bing_scrape(driver, content)
    write_csv(result, OUTPUT_PATH, csv_header)

if __name__ == "__main__":
    main()
