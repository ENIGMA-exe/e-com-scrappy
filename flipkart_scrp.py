import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('driver/chromedriver.exe')

obj = "C++ book"

link = "https://www.flipkart.com/search?q="

driver.get(link+obj)
time.sleep(2)

# driver.page_source
soup = BeautifulSoup(driver.page_source,'html.parser')

a = soup.find_all("a",class_="_2rpwqI")
if(a == []):
    a = soup.find_all("a",class_="s1Q9rs")

for i in a:
    r = requests.get("https://www.flipkart.com"+i['href'])
    soup_1 = BeautifulSoup(r.text,'html.parser')
    
    try:
        print("Name:-"+ soup_1.find("span",class_="_35KyD6").getText())
    except:
        try:
            print("Name:-"+ soup_1.find("span",class_="B_NuCI").getText())
        except:
            print("Name:-"+ soup_1.find("span",class_="yhB1nd").getText())
    
    
    try:
        print("Price:-"+ soup_1.find("div",class_="_1vC4OE _3qQ9m1").getText())
    except:
        try:
            print("Price:-"+ soup_1.find("div",class_="_1vC4OE _2Q57Ls").getText())
        except:
            print("Price:-"+ soup_1.find("div",class_="_25b18c").getText())
    try:    
        print("Ratting:-"+ soup_1.find("div",class_="hGSR34").getText() +" out of 5")
    except:
        print("Ratting:- Not mention")
        
    print("Highlights:-")
    for k in soup_1.find_all("li",class_="_2-riNZ"):
        print("           "+k.getText())
        
    print("_________________________________________________________________________________________________")