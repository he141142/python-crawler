from googlesearch import search
import requests  # Import thư viện requests
from typing import List
from typing import Dict

from web_crawler.factory import WebSite

root = ['cafef', 'finance.vietstock', 'vnexpress', 'vn.investing.com']


def ProduceWebsite(input: str) -> WebSite:
    if input == 'cafef':
        return WebSite.CAFE_F
    if input == 'vnexpress':
        return WebSite.VN_EXPRESS
    if input == 'finance.vietstock':
        return WebSite.VIET_STOCK
    else:
        return WebSite.NOT_IMPLEMENT


class SearchEngine:
    def produce_output(self) -> Dict[WebSite, List[str]]:
        pass


class GoogleSearchSupporter(SearchEngine):
    def __init__(self):
        self.search_results: Dict[WebSite, List[str]] = {}

        # User-Agent giả mạo để tránh lỗi 429
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

    def search_by_input(self) -> SearchEngine:
        # Tìm kiếm
        query = input()
        gg_rel = self.process_input(query)
        # Kiểm tra và in ra các ktin tết quả chứa từ trong danh sách root
        for _result in gg_rel:
            for _keyword in root:
                if _keyword in _result:
                    webSiteToCraw = ProduceWebsite(_keyword)
                    self.search_results.setdefault(webSiteToCraw, []).append(_result)

        return self

    def produce_output(self) -> Dict[WebSite, List[str]]:
        return self.search_results

    def process_input(self, input: str) -> [str]:
        search_results = []
        # Đặt tùy chọn headers trong yêu cầu
        for j in search(input, tld="com.vn", num=10, stop=10, pause=2):
            # Tạo yêu cầu với User-Agent
            response = requests.get(j, headers=self.headers)

            # Kiểm tra xem yêu cầu thành công
            if response.status_code == 200:
                search_results.append(j)
        return search_results
