import requests
from bs4 import BeautifulSoup
import sys, os


def movie_list(city):
    mlist = []
    url = 'http://www.bing.com/search?q=movies+' + str(city)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup1 = BeautifulSoup(plain_text, "lxml")
    for link in soup1.findAll('div', {'class': 'tit'}):
        title = link.get_text()
        mlist.append(title)

    return mlist
