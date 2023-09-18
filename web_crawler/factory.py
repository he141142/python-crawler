from web_crawler.interfaces.crawler import CrawlerEngine
from enum import Enum
from web_crawler.web import cafeF, ExpressVn,viet_stocker


class WebSite(Enum):
    VN_EXPRESS = 1
    CAFE_F = 2
    VIET_STOCK = 3
    NOT_IMPLEMENT = -1


def GetCrawler(wb: WebSite, url: str) -> CrawlerEngine:
    if wb == wb.VN_EXPRESS:
        return ExpressVn.ExpressCrawler(url)
    elif wb == wb.CAFE_F:
        return cafeF.CafeFCrawler(url)
    elif wb == wb.VIET_STOCK:
        return viet_stocker.VietStockCrawler(url)
    else:
        raise Exception('unimplemented')