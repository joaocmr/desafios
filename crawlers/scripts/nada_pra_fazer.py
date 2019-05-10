import sys

sys.path.append("./reddit")

from RedditCrawler import RedditCrawler

if len(sys.argv) != 2:
    print("Incorrent number of arguments")
    print("Script must be executed like: ")
    print("python nada_pra_fazer.py <subreddit1;subreddit2;subreddit3>")

crawler = RedditCrawler()

subreddits = sys.argv[1]
subreddits_list = subreddits.split(";")

for subreddit in subreddits_list:
    top_threads = crawler.get_top_threads(
        subreddit
    )

    top_threads_list = crawler.create_top_threads_list(
        top_threads
    )

    print("-------------------")
    print("TOP THREADS FOR {} SUBREDDIT".format(subreddit))
    print(top_threads_list)
    print("-------------------")
