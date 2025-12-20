import requests
from io import StringIO
import json
import datetime as dt
import pandas as pd

# --- GET THE DATE ---
this_year = dt.datetime.now().year
last_year = this_year - 1
this_month = dt.datetime.now().month
yesterday = (dt.datetime.now() - dt.timedelta(days=1)).date()
today = dt.datetime.now().date()

# --- NATURAL GAS PRICE DATA ---
# replace the 'apikey' below with your own key from https://www.alphavantage.co/support/#api-key
# params = {
#     'function': 'NATURAL_GAS',
#     'interval': 'daily',
#     'datatype': 'csv',
#     'apikey': 'V4WK0D4PPSPXKI43'
# }

# url1 = f'https://www.alphavantage.co/query'
# res1 = requests.get(url1, params=params)

# if res1.status_code == 200:
#     price_df = pd.read_csv(StringIO(res1.text))
    
#     if price_df.empty:
#         print("No data available for the specified date range.")
#     else:
#         print("Data retrieved successfully.")
#         price_df['timestamp'] = pd.to_datetime(price_df['timestamp'])
#         print(price_df.head())
        
#         lastyear_df = price_df[price_df['timestamp'].dt.year == last_year]
#         lastyear_df = lastyear_df[lastyear_df['value'] != '.']
        
#         thisyear_df = price_df[(price_df['timestamp'].dt.year == this_year) & (price_df['timestamp'].dt.month == this_month)]
#         thisyear_df = thisyear_df[thisyear_df['value'] != '.']
        
#         with open(f'./Day36/year{this_year}.csv', 'w', encoding='utf-8') as f:
#             thisyear_df.to_csv(f, index=False)
            
#         with open(f'./Day36/year{last_year}.csv', 'w', encoding='utf-8') as f:
#             lastyear_df.to_csv(f, index=False)
            
# else:
#     print(f"Error of trying to connect alphavantage.co: {res1.status_code}")
    

# --- NEWS RELATED TO NATURAL GAS ---
# replace the 'my_key' below with your own key from https://newsapi.org
my_key = 'b6af45f336fd4a1c88288ec13143bf0a'
result = []

with open('./Day36/keywords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        keyword = line.strip()
        url2 = 'https://newsapi.org/v2/everything'
        res2 = requests.get(url2, params={
            'q': keyword,
            'from': yesterday,
            'to': today,
            'sortBy': 'popularity',
            'apiKey': my_key
        })
        if res2.status_code == 200:
            data = res2.json()
            if data['status'] == 'ok':
                try:
                    if data['articles'][0]:
                        article = data['articles'][0]
                        result.append({
                            'title': article['title'],
                            'description': article['description'],
                            'url': article['url'],
                            'publishedAt': article['publishedAt'],
                            'keyword': keyword})
                except IndexError:
                    print(f"No articles found for keyword: {keyword}")
        else:
            print(f"Error connecting to NewsAPI ({keyword}): {res2.status_code}")

if result:
    with open(f'./Day36/news{this_year}.csv', 'w', encoding='utf-8') as f:
        news_df = pd.DataFrame(result)
        news_df.to_csv(f, index=False)
else:
    print("No news articles found for the specified keywords.")
               