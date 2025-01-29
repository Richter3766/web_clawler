import os
from urllib.parse import urlparse

from app.crawler import github_blog_crawler
from app.crawler.url_selector import UrlSelector


def url_distribution_worker(url_selector: UrlSelector):
    while True:
        url = url_selector.select_url()
        print("url 선택: ", url)
        prefix = urlparse(url).netloc
        if prefix == os.getenv('HYEONSOO_BLOG_URL'):
            github_blog_crawler.add_url(url)
