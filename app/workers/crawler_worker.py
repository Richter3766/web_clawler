import time

from app.crawler import Crawler, DataProcessor
from app.dto import CrawledDto

def crawling_worker(crawler: Crawler, data_processor: DataProcessor):
    while True:
        data = crawler.request_html()
        if data is not None:
            crawled_dto: CrawledDto = crawler.parser.parse(data)
            if crawled_dto is None:
                continue
            crawled_dto.set_url(data.url)
            data_processor.append_dto(crawled_dto)

        time.sleep(2)

