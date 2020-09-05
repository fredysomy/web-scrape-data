import requests
from bs4 import BeautifulSoup
import html5lib
"""THE  BELOW REQUEST CAN BE MODIFIED TO GET MORE DATA BY CHANGING THE  /page/1 to any page no"""
r=requests.get('https://aglasem.com/category/entrance-exams/page/1')
s=BeautifulSoup(r.content,'html5lib')
j=s.find(class_="jeg_posts jeg_load_more_flag")
for i in range(0,len(j)-2):
    v=j.find_all('article')[i]
    title=v.find('div',class_="jeg_postblock_content").find('h3').find('a').getText()
    link=v.find('div',class_="jeg_postblock_content").find('h3').find('a')['href']
    desc=v.find('div',class_="jeg_post_excerpt").find('p').getText()
    print(title,",",desc,",",link)
    print("-------------------------------------------")

