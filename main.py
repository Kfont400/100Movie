from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
titles = soup.find_all(name='h3',class_='title')
title = [title.getText() for title in titles]
movies = title[::-1]


with open('movies.txt', 'w') as f:
    for movie in movies:
        f.write(f'{movie}\n')