from  urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
texts=[]
#1번기사.

url='https://www.samsungsds.com/kr/insights/1232584_4627.html'
html = requests.get(url)
html.raise_for_status()
html.encoding='UTF-8' 
soup = BeautifulSoup(html.text, 'html.parser')
text=soup.select('div.txt_wrap')
texts.append(text[0].text)

#2번기사
url='https://www.hins.or.kr/menu.es?mid=a20801000000'
html = requests.get(url)
html.raise_for_status()
html.encoding='UTF-8' 
soup = BeautifulSoup(html.text, 'html.parser')
text=soup.find_all('td',{'colspan':'3'})
for i in text:
    texts.append(i.text)

#3번기사
url='https://www.hins.or.kr/menu.es?mid=a20804000000'
html = requests.get(url)
html.raise_for_status()
html.encoding='UTF-8' 
soup = BeautifulSoup(html.text, 'html.parser')
text=soup.find_all('td',{'colspan':'3'})

for i in text:
    texts.append(i.text)


#4번기사
url='https://www.codingworldnews.com/news/articleView.html?idxno=14870'
html = requests.get(url)
html.raise_for_status()
html.encoding='UTF-8' 
soup = BeautifulSoup(html.text, 'html.parser')
text=soup.select('article#article-view-content-div>p')
for i in text:
    texts.append(i.text)

#5번기사
url='http://www.monews.co.kr/news/articleView.html?idxno=216194'
html = requests.get(url)
html.raise_for_status()
html.encoding='UTF-8' 
soup = BeautifulSoup(html.text, 'html.parser')
text=soup.select('article#article-view-content-div>p')
for i in text:
    texts.append(i.text)

# with open('texts.csv','w',encoding='UTF-8') as f:
#     for name in texts:
#         f.write(name+'\n')

df=pd.read_csv("D:\WEB_CRAWLING\texts.csv",encoding='UTF-8')
content_all=''
for i in range(len(df)):
    content_all=content_all+' '+df.loc[i]
import re
content_all=re.sub('[^ㄱ-|가-힣]',"",content_all)
content_all=str
    