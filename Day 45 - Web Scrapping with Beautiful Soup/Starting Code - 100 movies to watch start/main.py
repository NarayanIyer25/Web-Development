import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇



response = requests.get(url=URL)
result = response.text
movie_names = []
soup = BeautifulSoup(result,"html.parser")
movies_list = [name.getText() for name in soup.find_all(name="h3",class_="title")][::-1]
for i in movies_list:
    file =  open(r'D:\Wed Development\Day - 44 - Web Scrapping with Beautiful Soup\Starting Code - 100 movies to watch start\file.txt',encoding='utf-8',mode='a+')
    file.writelines(f'{i}\n')
    file.close()


