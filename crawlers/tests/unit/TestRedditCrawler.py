import sys
import unittest
import json
from unittest.mock import patch, Mock

sys.path.append("./reddit")

from RedditCrawler import RedditCrawler

class TestFormater(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.crawler = RedditCrawler()
        with open("./tests/data/cats_subreddit.txt") as reddit_file:
            self.cats_subreddit = reddit_file.read()
        with open("./tests/data/top_cats_threads.json") as top_threads_json:
            self.top_cats_threads = json.load(top_threads_json)

    @patch.object(RedditCrawler, 'request_page_text')
    def test_create_top_threads(self, mock_request_page):
        mock_request_page.return_value = self.cats_subreddit
        top_threads = self.crawler.get_top_threads("cats")
        top_threads_list = self.crawler.create_top_threads_list(top_threads)

        self.assertEqual(top_threads_list, self.top_cats_threads)
        
if __name__ == '__main__':
    unittest.main()