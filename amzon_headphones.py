from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s=Service("C:/Users/Vishal Ghuge/Desktop/chromedriver.exe")

driver=webdriver.Chrome(service=s)

for i in range(1,21):

    driver.get('https://www.amazon.in/s?k=headphones&page={}'.format(i))

    html=driver.page_source

    with open ('amazon_headphones.html','a',encoding='utf-8') as f:
        f.write(html)
