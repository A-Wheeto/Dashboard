# Key a2c546ca84444edd821ca027ff3a84f1
import requests

url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=a2c546ca84444edd821ca027ff3a84f1"
headlines = []


def GetNews():

    print("-GATHERING NEWS")

    response = requests.get(url)
    response_json = response.json()

    for news in response_json['articles']:
        headlines.append(news['title'])

    return headlines
