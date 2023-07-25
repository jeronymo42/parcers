from bs4 import BeautifulSoup
import requests

link = 'https://unsplash.com/t/film'

page = requests.get(link).text
soup = BeautifulSoup(page, 'lxml')
block_list = set(soup.find_all('div', class_='MorZF'))
image_name = 0
for image in block_list:
    if image_name < 21:
        block = str(image)
        img_link_start = block.find('src=')
        img_link_end = block.find('?ixlib')
        img_link = block[img_link_start+5:img_link_end]
        image_res = requests.get(img_link).content
        with open(str(image_name)+'.png', 'wb') as image:
            image.write(image_res)
        print(f'Изображение {image_name}.png успешно скачано!')
        image_name += 1
        continue
print('Хватит пока...')
    