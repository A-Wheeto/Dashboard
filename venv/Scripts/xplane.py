import requests
from bs4 import BeautifulSoup
import re


def getheadlines():
    print("-GETTING THRESHOLD HEADLINES")

    url = "https://www.thresholdx.net/news"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all("div", class_="t-invert")
    date = soup.find_all('div', class_='_15px-text inverted')
    img = soup.find_all('div', class_='tile')

    urllist = []
    for imgurl in img:
        urllist.append(re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', imgurl['style']))

    class NewsPackage:
        def __init__(self, headline, date, url):
            self.headline = headline
            self.date = date
            self.url = url

    return_list = []
    for a, b, c in zip(headlines, date, urllist):
        return_list.append(NewsPackage(a.text, b.text, c[0]))

    return return_list
