import requests
from bs4 import BeautifulSoup

page = 1

while page < 10:
    url = 'https://news.ycombinator.com/news?p=' + str(page)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="html.parser")

    for link in soup.find_all('a', {'class': 'titlelink'}):
        if 'github.com' in link['href']:
            print('{} - {}'.format(link.text, link['href']))

    page += 1
