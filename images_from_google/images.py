import os
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import base64
from io import BytesIO
from PIL import Image





def download_google_images(search_query: str, dic ,number_of_images=500 ) -> None:

    # dic_name=search_query.replace(" " , "_")
    if os.path.exists(f'static/{int(dic)}'):
        return "Already exist"
    else:
        os.mkdir(f'static/{int(dic)}')

    '''Download google images with this function\n
       Takes -> search_query, number_of_images\n
       Returns -> None
    '''
    def scroll_to_bottom():
        '''Scroll to the bottom of the page
        '''
        last_height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

            new_height = driver.execute_script('return document.body.scrollHeight')
            try:
                element = driver.find_element(
                    by=By.CSS_SELECTOR,
                    value='.YstHxe input'
                )
                element.click()
                time.sleep(2)
            except:
                pass

            if new_height == last_height:
                break

            last_height = new_height

    service = Service("C:/Users/Vishal Ghuge/Desktop/chromedriver.exe")

    # This code is useed to keep open the chrome window 
    # from selenium.webdriver.chrome.options import Options
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    # service = Service("C:/Users/Vishal Ghuge/Desktop/chromedriver.exe")
    # driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
 
    service = Service("C:/Users/Vishal Ghuge/Desktop/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    url = 'https://images.google.com/'

    driver.get(
        url=url
    )

    box = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    )

    box.send_keys(search_query)

    box.send_keys(Keys.ENTER)
    time.sleep(2)

    scroll_to_bottom()
    time.sleep(2)

    img_results = driver.find_elements(
        by=By.XPATH,
        value="//img[contains(@class,'rg_i Q4LuWd')]"
    )

    print(f'Totla images -> {len(img_results)}')

    count = 0

    counter = 1
    
    for img_result in img_results:
        try:
            WebDriverWait(
                driver,
                15
            ).until(
                EC.element_to_be_clickable(
                    img_result
                )
            )
            img_result.click()
            time.sleep(2)

            actual_img = driver.find_element(
                by=By.XPATH,
                value="//img[contains(@class,'n3VNCb')]"
            )

            src = actual_img.get_attribute('src')
            width = actual_img.get_attribute('width')
            height = actual_img.get_attribute('height')
            print(src)
            if 'https://' in src:

                try:


                    import requests

                    image_content = requests.get(src).content
                    image_file = BytesIO(image_content)
                    image = Image.open(image_file).convert('RGB')
                   
                    
                    with open(f'static/{int(dic)}/{counter}', "wb") as f:
                        f.write(image)
                        counter+=1

                except:

                    pass


            else:
                print('Base 64 in source.')

                image_data = base64.b64decode(src.split(',')[1])

                with open(f"static/{int(dic)}/{counter}.jpg" , 'wb') as f:
                    f.write(image_data)
                    
                counter += 1



        except:

            print('Image is not clickable.')
        
        count += 1
        if count == number_of_images:
            break


import pickle

with open('movies.pkl' , 'rb') as f:
    movies=pickle.load(f)

movies_list = list(movies['title'].values)
movie_id = list(movies['movie_id'].values)

for tag , dic in zip(movies_list , movie_id):
    
    download_google_images(tag , dic, 10 )




