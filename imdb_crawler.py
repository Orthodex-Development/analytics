import requests
from bs4 import BeautifulSoup
import json
from score import *
from label import *

title = ""
dic = {'title': 'value'}


def movie_review(moviename):
    str(moviename)
    mname = moviename.replace(" ", "+")
    url = 'https://www.bing.com/search?q=' + str(mname) + '+imdb'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup1 = BeautifulSoup(plain_text, "lxml")
    i = 0
    for link in soup1.findAll("cite"):
        if i > 0:
            break
        else:
            title = link.get_text()
            i += 1
    return title


def getuser_review(mr):
    global review
    url1 = movie_review(mr)
    mr = mr.replace(" ", "+")
    url3 = 'http://www.omdbapi.com/?t=' + mr
    url2 = 'http://{0}'.format(str(url1))
    source_code = requests.get(url2)
    source_code1 = requests.get(url3)
    plain_text = source_code.text
    plain_text1 = source_code1.text
    test = json.loads(plain_text1)
    dic.update({'Title': test['Title']})
    dic.update({'Runtime': test['Runtime']})
    dic.update({'Actors': test['Actors']})
    dic.update({'Genre': test['Genre']})
    dic.update({'Plot': test['Plot']})
    dic.update({'Metascore': test['Metascore']})
    dic.update({'imdbRating': test['imdbRating']})

    soup2 = BeautifulSoup(plain_text, "lxml")
    i = 0
    for link in soup2.findAll('p', {'itemprop': 'reviewBody'}):
        if i > 0:
            break
        else:
            review = link.get_text()
            i += 1
    dic.update({'Review': review})
    senscore = get_score(review)
    dic.update({'SentimentScore' : float(senscore)})
    nature = get_label(review)
    dic.update({'Nature' : nature})
    return dic