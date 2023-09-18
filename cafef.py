# Craw dữ liệu Cafef

import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
# from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.service import Service as BaseService

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=r'C:\Users\Admin\Desktop\Project\Craw_Web_Stock\chromedriver.exe')
option = Options()
option.binary_location = r'C:\Users\Admin\Desktop\Project\Craw_Web_Stock\chrome\win64-114.0.5735.133\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=service, options=option)

# Open the URL
driver.get("https://cafef.vn/vinamilk.html")

sleep(1)
# Don't forget to quit the driver when you're done
# time.sleep(random.randint(1,5))

# ====================== get link + title
# elems = driver.find_elements(By.CSS_SELECTOR,".tlitem href")
# titles = [elem.text for elem in elems]
# links = [elem.get_attribute('href') for elem in elems]
# print(links)

# Find all elements with class "tlitem"
limit = 10

# Initialize empty lists to store links and titles
links = []
titles = []

elements = driver.find_elements(By.CLASS_NAME, "tlitem")

# Loop through each element and extract the href and title attributes, limited to 10 elements
for i, element in enumerate(elements):
    if i >= limit:
        break

    link_element = element.find_element(By.TAG_NAME, "a")
    link = link_element.get_attribute("href")
    title = link_element.get_attribute("title")
    # «««««« »»»»»»
    links.append(link)
    titles.append(title)

    # crawl link tiếp theo
    driver.get(link)


    # Print or store the href and title
    # print("Title:", title)
    # print("Href:", href)

    

df1 = pd.DataFrame(list(zip(titles,links)), columns=['Title','Links'])
print(df1)

driver.quit()