import requests
from bs4 import BeautifulSoup
import re


def GetGames():
    print("-GETTING STEAM TOP SELLING")

    url = 'https://store.steampowered.com/'
    request = requests.get(url)
    response = BeautifulSoup(request.content, 'html.parser')
    response_top_selling = response.find('div', id='tab_topsellers_content')
    response_title = response_top_selling.find_all('div', class_='tab_item_name')
    response_price = response_top_selling.find_all('div', class_='discount_final_price')
    response_imgurl = response_top_selling.find_all('a', class_='tab_item')

    id_list = []

    for x in response_imgurl:
        try:
            if len(x['data-ds-appid']) > 7:
                id_list.append(x['data-ds-appid'].split(',', 1)[0])
            else:
                id_list.append(x['data-ds-appid'])
        except:
            id_list.append(re.findall(r'\[(\d+)\]', x['data-ds-bundle-data'])[0])

    class Game:
        def __init__(self, title, price, imgurl):
            self.title = title
            self.price = price
            self.imgurl = imgurl

    list_games = []

    for a, b, c in zip(response_title, response_price, id_list):
        list_games.append(Game(a.text, b.text, c))

    #for game in list_games:
    #    print(game.title, game.price, game.imgurl)

    return list_games
