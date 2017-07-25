import os
import time

from markovbot import MarkovBot

# Create the bot!
JackLondon = MarkovBot()
# Get the current directory's path and point to the book
directory = os.path.dirname(os.path.abspath(__file__))
WhiteFang = os.path.join(directory, 'whitefang.txt')
# Read the book
JackLondon.read(WhiteFang)

# Load API keys and access tokens from separate file
with open('londonbot_login_info') as f:
    lines = f.read().splitlines()

cons_key = lines[0]
cons_secret = lines[1]
access_token = lines[2]
access_token_secret = lines[3]


# Login to Twitter and begin tweeting; wait a week before stopping the script
JackLondon.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

JackLondon.twitter_tweeting_start(days=0, hours=12, minutes=0, keywords=None, prefix=None, suffix=None)


wait_a_week = 7 * 24 * 60 * 60
time.sleep(wait_a_week)

JackLondon.twitter_tweeting_stop()
