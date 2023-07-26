import requests
from bs4 import BeautifulSoup

url = 'https://mp3uks.ru/'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

requsites = soup.find_all('a', class_='track-desc')
res_links = []
titles = []
artists = []

for req in requsites:
    titles.append(req.find('div', 'track-title').text)
    artists.append(req.find('div', 'track-subtitle').text)
links = soup.find_all('a', title="Скачать трек")
for link in links:
    res_links.append(' https://' + link['href'][2:])
for track in zip(res_links, titles, artists):
    track_name = track[2] + '_'+ track[1] + '.mp3'
    with open(track_name, 'wb') as file:
        mp3 = requests.get(track[0]).content
        file.write(mp3)
    print(f'{track_name} успешно скачан! =)')