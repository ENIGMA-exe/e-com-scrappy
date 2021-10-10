import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('driver/chromedriver.exe')

obj = "java book"

link = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw="

driver.get(link+obj)
time.sleep(2)

soup = BeautifulSoup(driver.page_source,'html.parser')

for i in soup.find_all("a",class_="s-item__link"):
    r = requests.get(i['href'])
    soup_1 = BeautifulSoup(r.text,'html.parser')
    
    print("Name:-"+ soup_1.find("h1",class_="it-ttl").getText())
    try:
        print("Price:- "+ soup_1.find("span",id="convbidPrice").getText())
    except:
        try:
            print("Price:- "+ soup_1.find("span",id="prcIsum").getText())
        except:
            print("Price:- "+ soup_1.find("span",class_="notranslate").getText())
    print(" ")    