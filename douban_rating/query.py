import requests
from bs4 import BeautifulSoup
from douban_rating.rating import Rating

query_url = 'https://book.douban.com/j/subject_suggest?q={query}'


def query(title):
    response = requests.get(query_url.format(query=title))
    items = response.json()

    return [get_rating(item) for item in items]


def get_rating(item):
    response = requests.get(item.get('url'))
    beautiful_soup = BeautifulSoup(response.text, 'html.parser')
    rating = beautiful_soup.select_one('.rating_num').text

    return Rating(item.get('title'), rating)
