import urllib.request
from bs4 import BeautifulSoup
import re
from datetime import date

date_while = date.today()
xx = date_while.strftime('%d.%m.%Y')

page = urllib.request.urlopen("https://365info.kz/category/poslednie-novosti")
soup = BeautifulSoup(page, "html.parser")

h = soup.find_all('a', {'class': 'archive__item-link'})
for h1 in h:
#     if re.search(xx, date):
    href = h1.get('href')
    post = "" + href
    page = urllib.request.urlopen(post)
    soup = BeautifulSoup(page)
    
    date = soup.find('time', {'class': 'updated'}).get('datetime')
    dt = re.findall('\d+', date)
    time = soup.find('time', {'class': 'updated'}).text
    t = re.findall('\d+', time)
    datetime = dt[0] + '.' + dt[1] + '.' + dt[2] + ' ' + t[0] + ':' + t[1] + ':' + '00.0'
    
    try:
        title = soup.find('div', {'class': 'singular__content content-typography es-email-subscribe'}).text
        t = soup.find('div', {'class': 'singular__content content-typography none-bold-first-p'})
        text = soup.find('h1', {'class': 'singular__title'}).text + title
        t1 = t.find_all('p', {'': ''})
        for t2 in t1:
            text = text + t2.text
    except:
        title = soup.find('div', {'class': 'singular__content content-typography es-email-subscribe'}).text
        t = soup.find('div', {'class': 'singular__content content-typography es-email-subscribe'})
        text = soup.find('h1', {'class': 'singular__title'}).text + title
        t1 = t.find_all('p', {'': ''})
        for t2 in t1:
            text = text + t2.text
    text = text.replace("\n", " ") + "\n"
    
    try:
        img = soup.find('figure', {'class': 'singular__thumbnail'}).find('img').get('src')
    except:
        img = None
    
    print(img)