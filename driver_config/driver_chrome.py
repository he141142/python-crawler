import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
# from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.service import Service as BaseService

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def GetChromeDriver() -> webdriver.Chrome:
    service = Service(executable_path=r'C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe')
    option = Options()
    option.binary_location = r'C:\Users\Admin\Downloads\Google_Search_Engine-master\Google_Search_Engine-master\chrome\win64-114.0.5735.133\chrome-win64\chrome.exe'

    driver = webdriver.Chrome(service=service, options=option)
    return driver
