import requests
from bs4 import BeautifulSoup
import html5lib
r=requests.get('https://www.successcds.net/examsyllabus/')
s=BeautifulSoup(r.content,'html5lib')
y=s.find(class_="entry clearfix")
for i in range(0,len(y)):
    try:
        desc=y.find_all('p')[i].find('a').text
        link=y.find_all('p')[i].find('a')['href']
        print(desc,'-',link)
    except:
        pass
          
