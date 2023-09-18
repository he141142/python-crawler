from web_crawler.interfaces.crawler import CrawlerEngine
from web_crawler.dto.crawl_output import CrawlOutput
from driver_config.driver_chrome import GetChromeDriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd


class CafeFCrawler(CrawlerEngine):
    def __init__(self, link: str):
        self.link = link
        self.limit = 10
        #clone driver for cafeF
        # self.cafeF_driver = GetChromeDriver()

        self.links = []
        self.titles = []

    def CrawData(self) -> CrawlOutput:
        # self.cafeF_driver.get(self.link)
        # sleep(1)
        #
        # elements = self.cafeF_driver.find_elements(By.CLASS_NAME, "tlitem")
        # # Loop through each element and extract the href and title attributes, limited to 10 elements
        # for i, element in enumerate(elements):
        #     if i >= self.limit:
        #         break
        #
        #     link_element = element.find_element(By.TAG_NAME, "a")
        #     link = link_element.get_attribute("href")
        #     title = link_element.get_attribute("title")
        #     # «««««« »»»»»»
        #     self.links.append(link)
        #     self.titles.append(title)
        #
        #     # crawl link tiếp theo
        #     self.cafeF_driver.get(link)
        #
        #     # Print or store the href and title
        #     # print("Title:", title)
        #     # print("Href:", href)
        # df1 = pd.DataFrame(list(zip(self.titles, self.links)), columns=['Title', 'Links'])
        #
        # out_put = CrawlOutput()
        # out_put.SetDataFrame(df1)

        out = CrawlOutput()
        out.TextData = f'data from cafeF url: {self.link}'
        return out

