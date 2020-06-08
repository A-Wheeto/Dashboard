import requests

url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey="
headlines = []


def GetNews():

    print("-GATHERING NEWS")

    response = requests.get(url)
    response_json = response.json()

    for news in response_json['articles']:
        headlines.append(news['title'])

    return headlines
