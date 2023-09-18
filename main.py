from google_engine.google_search import GoogleSearchSupporter
from web_crawler.factory import GetCrawler, WebSite

engine = GoogleSearchSupporter()

# tin tức chứng khoán vingroup hôm nay

# print(engine.search_by_input().produce_output())

out = engine.search_by_input().produce_output()
print(out)

# arrList[CrawlerEngine]
for _website, urls in out.items():
    if _website != WebSite.NOT_IMPLEMENT:
        for url in urls:
            try:
                print("??????")
                crawler = GetCrawler(_website, url)
                # crawler.CrawData()
                print(crawler.CrawData().TextData)
            except Exception as e:
                print(f"An exception of type {type(e).__name__} occurred: {e}")
                continue
