import requests
import sys
from bs4 import BeautifulSoup

class RedditCrawler:

    def __init__(self):
        self.url = defines._REDDIT_URL_

    def __request_page_text(self, url):

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

    def __get_page_parser(self, url):
        soup = BeautifulSoup(
            self.__request_page_text(url),
            'html.parser'
        )

        return soup

    def get_top_threads(self, subreddit_name):
        url = "{}/r/subreddit_name".format(self.url)
        top_threads = []
        parser = self.__get_page_parser(url)

        subredit_threads = parser.find_all(
            "div", attrs={"class": "thing"}
        )

        return [
            thread for thread in subredit_threads if thread['data-score'] > defines._MIN_SCORE_
        ]

    def create_top_threads_list(self, subreddit_name, top_threads):
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