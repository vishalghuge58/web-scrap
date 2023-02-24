from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/Vishal Ghuge/Desktop/chromedriver.exe")


# This code is useed to keep open the chrome window 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)




driver.get('http://google.com')

time.sleep(2)

#fetch the input search box by xpath

user_input=driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
user_input.send_keys('Campusx')
user_input.send_keys(Keys.ENTER)
time.sleep(1)

link=driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3')
link.click()
time.sleep(1)

link2=driver.find_element(by=By.XPATH,value='//*[@id="1668425005116"]/span[2]/a')

link2.click()


