
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
import csv
from PIL import Image
text = open('texts.txt', encoding='utf-8').read()
okt = Okt()
sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []
for word, tag in sentences_tag:
    if tag in ['Noun']:   
        noun_adj_list.append(word)

remove_set = {'및','등','대한','수','위','데이터','모델','개발','공통','병원','기반','환자','통한','것','예후','더','후','임','활용','서울','기관'}

noun_adj_list = [i for i in noun_adj_list if i not in remove_set]

with open('texts_to_csv.csv','w',newline='\n',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(noun_adj_list)
        
counts = Counter(noun_adj_list)
tags = counts.most_common(40)
if platform.system() == 'Windows':
    path = r'c:\\Windows\\Fonts\\malgun.ttf'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'


wc = WordCloud(font_path=path, background_color="white", max_font_size=60)


cloud = wc.generate_from_frequencies(dict(tags))
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()




