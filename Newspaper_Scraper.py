#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import time
import newspaper
from newspaper import Article
from IPython.display import display

url='https://vnexpress.net/vi-sao-nuoc-my-nhu-thung-thuoc-sung-4107997.html'

# article = Article(url)
# article.download()
# article.parse()
# display(article.text)
# print(article.text)


vep_paper = newspaper.build('https://dantri.com.vn/')
# vep_paper
# art=[]
# for article in vep_paper.articles:
#     print(article.url)
#     art.append(article)
# print('The number of Articles on the vnexpress website: %d'%len(art))


# import sys
corpus = []
# corpus.append(article.text)

count = 0
for article in vep_paper.articles:
    time.sleep(1)
    article.download()
    article.parse()
    text = article.text
    corpus.append(text)
    if count % 2 == 0 and count != 0:
        print('Obtained {} articles'.format(count))
    count += 1
    if count > 5:
        sys.exit()
print(corpus)
# In[ ]:




