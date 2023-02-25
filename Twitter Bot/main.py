import tweepy
from datetime import datetime
import requests

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
current_price = response.text[49:-3]

x = datetime.now()
weekday = x.strftime("%A")
day = x.strftime("%d")
month = x.strftime("%B")
year = x.year

status = f"On {weekday}, {month} {day} of the year {year} the price of 1 Bitcoin is ${current_price}"

api.update_status(status)