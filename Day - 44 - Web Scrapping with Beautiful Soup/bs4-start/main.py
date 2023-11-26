from bs4 import BeautifulSoup
import requests
'''
content = open(r'D:\Wed Development\Day - 44 - Web Scrapping with Beautiful Soup\bs4-start\website.html',
               encoding='utf-8')
soup = BeautifulSoup(content,"html.parser")
print(soup.body)

content.close()
'''

response = requests.get(url='https://news.ycombinator.com/')
result = response.text

soup = BeautifulSoup(result,"html.parser")
article_text = []
article_link = []
article_tag = soup.find_all(class_="titleline")

for tag in article_tag:
    text = tag.getText('a')
    article_text.append(text)
    link = tag.a.get('href')
    article_link.append(link)

article_score = [int(score.getText().split(' ')[0]) for score in soup.find_all(class_='score')]
max = article_score.index(max(article_score))
print(article_text[max])
print(article_link[max])
print(article_score[max])