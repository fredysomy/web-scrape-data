import requests
from bs4 import BeautifulSoup
import html5lib
s=requests.get('https://aglasem.com/top-medical-colleges-in-india/')
soup=BeautifulSoup(s.content,'html5lib')
a=soup.find('table')
y=[]
h={}
for i in range(1,40):
  b=a.find_all('tr')[i]
  rank=b.find_all('td')[0].getText()
  college=b.find_all('td')[1].getText()
  state=b.find_all('td')[3].getText()
  da={"rank":rank,"college":college,"state":state}
  y=y+[da]
print(y)
