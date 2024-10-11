import requests
import os
from twilio.rest import Client

# Let's take Tesla as our stock.
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_API = os.environ.get("STOCK_API")  # Change this to your stock_api
NEWS_API = os.environ.get("NEWS_API") # Change this to your news_api
account_sid = os.environ.get("ACCOUNT_SID")  # Change this to your account_sid
auth_token = os.environ.get("AUTH_TOKEN")  # Change this to your auth_token

# Used https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "full",
    "datatype": "json",
    "apikey": STOCK_API,
}

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']
# print(stock_data)

# Getting the values of the stock price from the JSON file
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
day_before_yesterday_data = (data_list[1])

yesterday_closing_price = float(yesterday_data['4. close'])
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])

difference = (yesterday_closing_price - day_before_yesterday_closing_price)
up_down = ""

# Checking if the stock went up or down
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Getting the percentage change of the stock between yesterday and day before yesterday
percent_change = round((difference / yesterday_closing_price) * 100)

# If the change is more than or less than 3%, the top 3 news will be messaged.
if abs(percent_change) > 3:
    # Used https://newsapi.org
    # Getting the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "apiKey": NEWS_API,
        "language": "en",
        "q": COMPANY_NAME,
        "searchIn": "title",
    }

    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    article = news_response.json()['articles']

    three_articles = article[:3]

# Used https://www.twilio.com
# Sending a separate message with the percentage change and each article's title and description.
    formatted_articles = [(f"{STOCK_NAME} {up_down}{percent_change} "
                           f"\nHeadline: {article[0]['title']} "
                           f"\nBrief: {article[0]['description']} \n") for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=f"article",
            from_="+18774555395",
            to="+15625642005",
        )
