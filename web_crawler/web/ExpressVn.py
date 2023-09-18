from web_crawler.interfaces.crawler import CrawlerEngine
from web_crawler.dto.crawl_output import CrawlOutput


class ExpressCrawler(CrawlerEngine):
    def __init__(self, url: str):
        self.url: str = url

    def CrawData(self) -> CrawlOutput:
        out = CrawlOutput()
        out.TextData = f'data from express url: {self.url}'
        return out
