import urllib.request
from bs4 import BeautifulSoup
from datetime import date
import re
import requests
from datetime import date, timedelta
import urllib3

date_while = date.today()
xx = date_while.strftime('%Y.%m.%d')

# page = urllib3.build_opener()
# page.addheaders = [('User', 'Mozilla/89.0')]
# page1 = page.open("https://ehonews.kz")
# soup = BeautifulSoup(page1)

url = "https://ehonews.kz/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# page = urllib.request.urlopen("https://ehonews.kz")
# soup = BeautifulSoup(page)

h = soup.find_all('h3', {'class': 'jeg_post_title'})
for h1 in h:
    href = h1.find('a').get('href')
#     if re.split('/',h1.get('href'))[1] == xx:
    url = href
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
#     try:
    t = soup.find('div', {'class': 'content-inner '})
    text = soup.find('h1', {'class': 'jeg_post_title'}).text + "\n"
    t1 = t.find_all('p', {'class': ''})
    for t2 in t1:
        text = text + t2.text
        
    try:
        img = soup.find('div', {'class': 'thumbnail-container animate-lazy'}).find('img').get('src')
    except:
        img = None
        
#     date = soup.find('time').text
#     d = re.findall('\d+', date)
#     datetime = d[0]+'.'+d[1]+'.'+d[2]+' '+d[3]+':'+d[4]
    
    print(text)