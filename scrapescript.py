
# import library
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


# Request to website and download HTML contents
#agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
wines = {}

#url = 'https://www.wine-searcher.com/find/riesling/2021'
#req = requests.get(url, headers=agent)
#content = req.text




DRIVER_PATH = r'C:\Users\magnu\Downloads\chromedriver_win32/chromedriver.exe'
options = Options()
options.add_argument("--user-data-dir=chrome-data") 
options.headless = False
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
time.sleep(5)


for i in range(2000,2022):
    driver.get(f"https://www.wine-searcher.com/find/riesling/{i}")
    soup = BeautifulSoup(driver.page_source)
    print('Finding wines')
    cards = soup.findAll(class_='card card-product')

    print('Looping through wines')
    for i in cards:
        name = i.find(class_='card-product__name')
        rating = i.find(class_='badge-rating badge badge-pill')
        try:
            wines[name.text.replace("\n", "")] = rating.text.split('/')[0]
        except:
            wines[name.text.replace("\n", "")] = 0
    print(wines)
    time.sleep(5)

df = pd.DataFrame({'Wines': list(wines.keys()), 'Points': list(wines.values())})

df 