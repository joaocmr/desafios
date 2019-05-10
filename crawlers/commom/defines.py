import os
import sys


def get_environ(tag):
    _TAG_ = os.environ.get(tag)
    if not _TAG_:
        print(tag + " not defined on ENVIRON")
        print("finalizando...")
        sys.exit()

    return _TAG_

_REDDIT_URL_ = get_environ('REDDIT_URL')
_MIN_SCORE_ = int(get_environ('MIN_SCORE'))