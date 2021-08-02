import urllib.request
from bs4 import BeautifulSoup
import re
import requests
from datetime import date, timedelta
import urllib

date_while = date.today()
xx = date_while.strftime('%d.%m.%Y')

page = urllib.build_opener()
page.addheaders = [('User', 'Mozilla/89.0')]
page1 = page.open("https://www.levada.ru")
soup = BeautifulSoup(page1)

h = soup.find_all('li', {'class': 'acf-rpw-li acf-rpw-clearfix'})
for h1 in h:
    href = h1.find('a').get('href')
    page = urllib2.build_opener()
    page.addheaders = [('User', 'Mozilla/89.0')]
    page1 = page.open(href)
    soup = BeautifulSoup(page1)
    
    t = soup.find('div', {'class': 'entry-content'})
    text = soup.find('h2', {'': ''}).text + "\n"
    t1 = t.find_all('p', {'class': ''})
    for t2 in t1:
        text = text + t2.text
            
    date = soup.find('time').get('datetime')
    d = re.findall('\d+', date)
    date_time = d[0]+'-'+d[1]+'-'+d[2]+' '+d[3]+':'+d[4]
    print(date_time + "\n")