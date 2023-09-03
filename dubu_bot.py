#!/usr/bin/python
import praw
import re
import random

# Quotes taken from: http://www.imdb.com/character/ch0007553/quotes
dubu_quotes = \
[
" dubu quote 1 ",
" dubu quote 2 ",
" dubu quote 3 ",
" dubu quote 4 ",
" dubu quote 5 ",
" dubu quote 6 ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("insert dubu quote here", comment.body, re.IGNORECASE):
            marvin_reply = "dubu bot says: " + random.choice(dubu_quotes)
            comment.reply(dubu_reply)
            print(dubu_reply)
