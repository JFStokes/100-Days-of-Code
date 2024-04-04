import json
import requests
import smtplib

# Set Constants. 
STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft Corp"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "DD0GRN80G5LP5L6W"
NEWS_API_KEY = "3ef7fe62559a4eecae2798f2dfd7d24a"

# Set Stock params.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Get Stock data.
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
daily_stock_data = data["Time Series (Daily)"] # Gets daily data into dict.
latest_stock_data = next(iter(daily_stock_data)) # Gets latest date in daily_stock_data, YYYY-MM-DD.
yesterday_closing = daily_stock_data[latest_stock_data]["4. close"] # Gets last closing price.
print(f"--> Last Closing Price: ${yesterday_closing}")

#TODO 2. - Get the day before yesterday's closing stock price
previous_day = ""
iter = 0
for day in daily_stock_data:
    if iter < 2:
        previous_day = day
        iter += 1
previous_close = daily_stock_data[previous_day]["4. close"]   
print(f"--> Previous Closing Price: ${previous_close}")     

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
close_dif = abs(float(yesterday_closing) - float(previous_close)) # Gets absolute value using abs().
print(f"--> Close Difference: ${close_dif}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_change = close_dif / float(previous_close) * 100
print(f"--> Percent Change: {percent_change}")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_change > 0.1:
    print("Get news!")
else:
    print("All is normal...")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": "microsoft"
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

with open("news.json", mode="a") as file:
    json.dump(news_data, file, indent=4)

# Email data to myself.
my_email = 'joshua.f.stokes.mil@gmail.com'
password = 'cgfhzcjcgcazjvoo'
to_email = 'joshua.stokes1617@yahoo.com'
email_body = json.dumps(news_data, indent=4)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg=f'Subject:Microsoft News\n\n{email_body}.'
    )

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

