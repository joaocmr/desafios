import requests
import sys

sys.path.append("./commom")

import defines
from bs4 import BeautifulSoup

class RedditCrawler:

    def __init__(self):
        self.url = defines._REDDIT_URL_

    def request_page_text(self, url):
        res = requests.get(
            url=url,
            headers={'User-agent': 'Bot'}
        )

        if res.status_code != 200:
            raise ValueError(
                "Unable to request from page {} \n Error: {}".format(
                    url, res.text
                )
            )
        return res.text

    def get_page_parser(self, url):
        soup = BeautifulSoup(
            self.request_page_text(url),
            'html.parser'
        )

        return soup

    def get_top_threads(self, subreddit_name):
        url = "{}/r/{}".format(
            self.url,
            subreddit_name
        )
        top_threads = []
        parser = self.get_page_parser(url)

        subredit_threads = parser.find_all(
            "div", attrs={"class": "thing"}
        )

        return [
            thread for thread in subredit_threads if int(thread['data-score']) > defines._MIN_SCORE_
        ]

    def create_top_threads_list(self, top_threads):
        top_threads_list = []
        for thread in top_threads:
            top_threads_list.append(
                {
                    "title": thread.find("a", attrs={"class": "title"}).get_text(),
                    "upvotes": thread['data-score'],
                    "subreddit": thread['data-subreddit'],
                    "thread_link": thread['data-url'],
                    "comments_link": "{}/{}".format(self.url, thread['data-permalink'])
                }
            )

        return top_threads_list