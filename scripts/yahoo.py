import requests
from bs4 import BeautifulSoup
url = "https://news.yahoo.co.jp/topics"
response = requests.get(url)
bs = BeautifulSoup(response.content,"lxml")

topics = bs.select('.fr, .fl')
news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

news_topics['エンタメ']
