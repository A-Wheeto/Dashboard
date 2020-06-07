import pihole as ph
import requests
from bs4 import BeautifulSoup
import time


def GetData():
    print("-CALLING RASPBERRY PI")

    pihole = ph.PiHole('192.168.0.37')

    url = 'http://192.168.0.37/admin/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    soup_temp = soup.find('a', id='temperature')
    temp = str(soup_temp.text).replace('Temp:', '').replace('°C', '')
    temp = temp.replace('°C', '')
    temp = temp.replace(' ', '')
    temp = temp.replace(' ', '')

    soup_memory = soup_temp.find_next_siblings()
    memory = list(soup_memory)[3].text
    memory = str(memory).replace('Memory usage:', '')
    memory = str(memory).replace('%', '')
    memory = str(memory).replace(' ', '')
    memory = str(memory).replace(' ', '')
    memory = str(memory).replace(' ', '')

    data_return = [pihole.status, pihole.ads_percentage, pihole.blocked,
                   pihole.gravity_last_updated['relative']['days'],
                   pihole.gravity_last_updated['relative']['hours'], temp, memory]

    return data_return
