import requests
from pyquery import PyQuery
from lxml import etree
import urllib
from douban_rating.rating import Rating

query_url = 'https://book.douban.com/j/subject_suggest?q={query}'

def query(title):
    response = requests.get(query_url.format(query=title))
    items = response.json()

    return [get_rating(item) for item in items]

def get_rating(item):
    document = PyQuery(url=item.get('url'))
    rating = document('.rating_num').text()

    return Rating(item.get('title'), rating)
