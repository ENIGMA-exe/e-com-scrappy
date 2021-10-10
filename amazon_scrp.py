import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('driver/chromedriver.exe')

driver.get('https://www.amazon.in')

elm = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
elm.click()

elm.send_keys("assus zenphon")

driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0);")

main=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results sg-row']")))

driver.get(driver.current_url)
html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'html.parser')

#link:-
a = soup.find_all("a",class_="a-link-normal a-text-normal")
link_list =[]
for i in a:
    link_list.append("https://www.amazon.in"+i['href'])

for i in link_list:
    driver.get(i)
    doc = driver.page_source
    soup = BeautifulSoup(doc, 'html.parser')
    
    #name:-
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@id='productTitle']")))
        a = driver.find_element_by_xpath("//span[@id='productTitle']")
        
    except:
        continue
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@id='productSubtitle']")))
        d = driver.find_element_by_xpath("//span[@id='productSubtitle']").text 
        
    except:
        d = " "    
        
    print("product name:- " + a.text + " " + d)
    
    #price:-
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@id='priceblock_ourprice']")))
        b = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']")
        print("price:- " + b.text)
        
    except:
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P']")))
            b = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P']")
            print("price:- " + b.text)
            
        except:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-price']")))
            b = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-price']")
            print("price:- " + b.text)
    
    #status:-
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-success']")))
        c = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-success']")
        print("status:- " + c.text)
        
    except:
        print("status:- not mentioned" )
    
    print(" ")
    

    