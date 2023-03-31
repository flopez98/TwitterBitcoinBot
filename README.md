Twitter Bot

This Python script uses the Tweepy and Requests libraries to fetch the current price of Bitcoin from Coinbase's API, and post it as a tweet on Twitter using the user's API credentials.
Requirements

    Python 3
    Tweepy
    Requests

Installation

    Clone this repository or download the bitcoin_price_tweet.py file.
    Install the required libraries using pip:

    pip install tweepy requests

    Replace the empty api_key, api_key_secret, access_token, and access_token_secret variables with your own Twitter API credentials. You can obtain these by creating a Twitter Developer account and creating an app.
    Run the script using python bitcoin_price_tweet.py or your preferred method.

Usage

When the script is run, it will fetch the current Bitcoin price from Coinbase's API, format the price and current date into a tweet, and post it to the authenticated user's Twitter account. The tweet will include the current day of the week, the day of the month, the month name, the year, and the current price of 1 Bitcoin in US dollars.

To customize the tweet message, modify the status variable near the end of the script to include your desired text and formatting.

Please note that Twitter's API rate limits are respected by setting the wait_on_rate_limit parameter to True. This may cause the script to pause execution if the rate limit is reached, but will resume automatically when the limit resets.
Disclaimer

This script is provided for educational and informational purposes only. The author is not responsible for any losses or damages incurred as a result of using this script or relying on the information it provides. Please use at your own risk.
