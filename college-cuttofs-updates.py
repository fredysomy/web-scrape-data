import requests
from bs4 import BeautifulSoup
import html5lib
"""THE  BELOW REQUEST CAN BE MODIFIED TO GET MORE DATA BY CHANGING THE  /page/1 to any page no"""
r=requests.get('https://cutoffs.aglasem.com/page/1')
s=BeautifulSoup(r.content,'html5lib')
jc=s.find(class_="jeg_posts jeg_load_more_flag")
for i in range(0,len(jc)-2):
    v=jc.find_all('article')[i]
    t=v.find('div',class_="jeg_postblock_content")
    title=t.find('h3').find('a').getText()
    link=t.find('h3').find('a')['href']
    print(title,link)
    
