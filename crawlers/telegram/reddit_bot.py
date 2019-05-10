import sys
import json
from telegram.ext import Updater, CommandHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

sys.path.append("./commom")
sys.path.append("./reddit")

from RedditCrawler import RedditCrawler
import defines

crawler = RedditCrawler()

def prepare_message(list_of_subreddits):
    message = ""
    for subreddit in list_of_subreddits:
        top_threads = crawler.get_top_threads(
            subreddit
        )

        top_threads_list = crawler.create_top_threads_list(
            top_threads
        )
        message += "--------------------------------------\n"
        message += "TOP THREADS FOR {} SUBREDDIT\n".format(subreddit)

        if top_threads_list:

            for thread in top_threads_list:
                message += "\n"
                message += "Subreddit: {}\n".format(thread['subreddit'])
                message += "Título: {}\n".format(thread['title'])
                message += "Link: {}\n".format(thread['thread_link'])
                message += "Comentários: {}\n".format(thread['comments_link'])
                message += "Pontuação: {}\n".format(thread['upvotes'])
                message += "\n"

        else:
            message += "\n"
            message += "Nenhuma thread com mais de {} upvotes encontrado".format(
                defines._MIN_SCORE_
            )
            message += "\n"

        message += "--------------------------------------\n"

    return message

def send_top_threads(bot, update):
    args = update.message.text.split(" ")

    if len(args) == 1:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Ops, faltou informar os subreddits"
        )
        return

    subreddits = args[-1]
    list_of_subreddits = subreddits.split(";")

    message_to_send = prepare_message(
        list_of_subreddits
    )

    bot.send_message(
        chat_id=update.message.chat_id,
        text=message_to_send
    )


updater = Updater(
    token=defines._BOT_TOKEN_
)
dp = updater.dispatcher
dp.add_handler(CommandHandler('NadaPraFazer', send_top_threads))
updater.start_polling()
updater.idle()