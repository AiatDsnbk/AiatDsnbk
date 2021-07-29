import urllib.request
from bs4 import BeautifulSoup
from datetime import date

date_while = date.today()
xx = date_while.strftime('%Y.%m.%d')

page = urllib.request.urlopen("https://ehonews.kz")
soup = BeautifulSoup(page)

h = soup.find_all('h3', {'class': 'jeg_post_title'})
for h1 in h:
    href = h1.get('href')
#     if re.split('/',h1.get('href'))[1] == xx:
#     post = "https://kapital.kz" + href
#     page = urllib.request.urlopen(post)
#     soup = BeautifulSoup(page)
#     try:
#         t = soup.find('div', {'class': 'article__body'})
#         text = soup.find('h1', {'class': 'article__title'}).text + "\n"
#         t1 = t.find_all('p', {'class': ''})
#     for t2 in t1:
#         text = text + t2.text
        
#     try:
#         img = soup.find('img', {'class': ''})
#     except:
#         img = None
        
#     date = soup.find('time').text
#     d = re.findall('\d+', date)
#     date_time = d[0]+'.'+d[1]+'.'+d[2]+' '+d[3]+':'+d[4]
    
    print(href)