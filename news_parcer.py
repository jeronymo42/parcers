import requests
from bs4 import BeautifulSoup
from config import RAPID_KEY, VOICE_KEY

page = requests.get('https://www.reuters.com/').text
soup = BeautifulSoup(page, 'lxml')
headings = soup.find_all('a', class_='text__text__1FZLe text__dark-grey__3Ml43 text__inherit-font__1Y8w3 text__inherit-size__1DZJi link__underline_on_hover__2zGL4 media-story-card__heading__eqhp9')
result = []
for head in headings:
    url = "https://just-translated.p.rapidapi.com/"
    querystring = {"lang":"ru","text":head.get_text()}
    headers = {
        "X-RapidAPI-Key": RAPID_KEY,
        "X-RapidAPI-Host": "just-translated.p.rapidapi.com"
    }
    header_tr = requests.get(url, headers=headers, params=querystring).json()['text']
    result.extend(header_tr)
print(*result, sep='\n')

with open('news.wav', 'wb') as file:
    all_headers = '\n Следующая новость: '.join(result)
    url = "https://voicerss-text-to-speech.p.rapidapi.com/"
    querystring = {"key":VOICE_KEY}
    payload = {
        "src": all_headers,
        "hl": "ru-ru",
        "v": "Peter",
        "r": "0",
        "c": "WAV",
        "f": "uLaw, 44 kHz, Stereo"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": RAPID_KEY,
        "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers, params=querystring).content
    file.write(response)
    print('Файл успешно записан!=)')

