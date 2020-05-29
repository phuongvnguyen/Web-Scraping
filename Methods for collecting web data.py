#!/usr/bin/env python
# coding: utf-8

# $$\Large \color{green}{\textbf{Several Mothod for collecting data from social media and newspaper}}$$
# 
# 
# 
# $$\large \color{blue}{\textbf{Phuong Van Nguyen}}$$
# $$\small \color{red}{\textbf{ phuong.nguyen@summer.barcelonagse.eu}}$$
# 
# https://ieeexplore.ieee.org/document/7023973

# https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/
# 
# https://github.com/clips/pattern
# 
# https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3

# # Accessing Web Pages

# In[2]:


from pattern.web import download


# In[3]:


page_html = download('https://en.wikipedia.org/wiki/Artificial_intelligence', unicode=True)


# In[8]:


file = open(page_html)
file.write(page_html.download())
file.close()


# In[7]:


file


# # Attempt 1: With request and BeautifulSoup

# Here are three approaches (i.e. Python libraries) for web scraping which are among the most popular:
# 
# 1. Sending an HTTP request, ordinarily via **Requests**, to a webpage and then parsing the HTML (ordinarily using **BeautifulSoup**) which is returned to access the desired information. Typical Use Case: Standard web scraping problem, refer to the case study.
# 
# 2. Using tools ordinarily used for automated software testing, primarily **Selenium**, to access a websites‘ content programmatically. Typical Use Case: Websites which use Javascript or are otherwise not directly accessible through HTML.
# 
# 3. **Scrapy**, which can be thought of as more of a general web scraping framework, which can be used to build spiders and scrape data from various websites whilst minimizing repetition. Typical Use Case: Scraping Amazon Reviews.

# ## Calling packages

# In[2]:


import requests
from bs4 import BeautifulSoup


# ## Not real time

# ### Requests

# In[3]:


import requests


# #### Sending the HTTP request
# HTTP request types:
# 
# **get**
# 
# **put**
# 
# **delete**
# 
# **head** and **options**

# In[4]:


# Defined the targe webpage
url='https://vietnamnet.vn/vn/giao-duc/tuyen-sinh/bo-truong-phung-xuan-nha-giai-thich-nhung-thay-doi-cua-ky-thi-tot-nghiep-thpt-637129.html'
# Scraping or sending a HTTP request via the Requests lib
response=requests.get(url)


# #### Response Status Codes
# Checking the status of sending a HTTP request

# In[5]:


response.status_code


# #### Response Content
# read the content of the server’s response.

# In[6]:


#scrap.content
response.text


# **Warming**
# 
# After executing these lines, you still only have the raw HTML with all tags included. This is usually not very useful, since most of the time when scraping with Requests, we are looking for specific information and text only, as human readers are not interested in HTML tags or other markups. This is where BeautifulSoup comes in.
# 
# ### BeautifulSoup for parsing
# 
# **BeautifulSoup** is a Python library used for parsing documents (i.e. mostly HTML or XML files). Using Requests to obtain the HTML of a page and then parsing whichever information you are looking for with BeautifulSoup from the raw HTML is the quasi-standard web scraping „stack“ commonly used by Python programmers for easy-ish tasks.

# In[8]:


from bs4 import BeautifulSoup


# #### html.parser

# In[9]:


soup = BeautifulSoup(response.text, 'html.parser')
soup
#print(soup.prettify())


# #### lxml’s HTML parser

# In[10]:


soup_lxml = BeautifulSoup(response.text, 'lxml')
soup_lxml#.get_text()


# ### Collecting the target content
# Here is the main content of article. To do that, you have to combine with the inspector on this website. This is because it lets you know which class does the content of the article on this website locate.
# 
# For example, using the inspector, I know that the main content of the article is located in the **ArticleContent** class

# In[11]:


#soup_lxml.contents
text = [p.text for p in soup_lxml.find(class_="ArticleContent").find_all('p')]
text


# In[12]:


len(text)


# In[13]:


text[0]


# ### Cleaning the raw data
# It is optional in this case

# In[30]:


import string
def phuong_clean_text_norm(text):
    """
    1. Make text lowercase, 
    2. remove text in square brackets, 
    3. remove punctuation 
    4. remove numbers.
    5. Remove whitespaces
    6. remove some additional punctuation 
    7. remove non-sensical text
    """
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text=  text.strip()
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text  


# In[53]:


cleaned_text=phuong_clean_text_norm(text[0])
cleaned_text


# # Real time
# Stock price

# https://github.com/Pavneet-Sing/Demos/blob/master/Python3/PS_scraping_bs4.py
# 
# 
# https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
# 
# https://stackoverflow.com/questions/20522820/how-to-get-tbody-from-table-from-python-beautiful-soup

# In[3]:


url_hsx ='https://www.hsx.vn/Modules/Rsde/RealtimeTable/LiveSecurity'
response_hsx=requests.get(url_hsx)
if response_hsx.status_code==200:
    print('Successfully connected to the HSX site')
soup_hsx_lxmlparse = BeautifulSoup(response_hsx.text,'html.parser')# 'html.parser')


# ## Table

# In[24]:


table= soup_hsx_lxmlparse.find_all('table')
print(table)


# ## Table Deal Stock
# ### General

# In[62]:


table_deal_Stock= soup_hsx_lxmlparse.find_all('table',{'class':'table-deal-stock'})
print(table_deal_Stock)


# ### Body of Table

# In[74]:


body_table=table_deal_Stock[0].find_all('tr')


# In[75]:


print(body_table)


# In[ ]:





# In[ ]:





# # Attempt 2: The newspaper package
# https://pypi.org/project/newspaper3k/
# 
# This package is much more convenient and powerfull than the previous two packages
# Features
# 1. Multi-threaded article download framework
# 2. News url identification
# 3. Text extraction from html
# 4. Top image extraction from html
# 5. All image extraction from html
# 6. Keyword extraction from text
# 7. Summary extraction from text
# 8. Author extraction from text
# 9. Google trending terms extraction
# 10. Works in 10+ languages (English, Chinese, German, Arabic, …)

# ## An gentle introduction

# In[57]:


import json
import time
import newspaper
from newspaper import Article


# **Language supported**
# Newspaper can extract and detect languages seamlessly. If no language is specified, Newspaper will attempt to auto detect a language.

# In[58]:


newspaper.languages()


# ## Downloading the specific article
# Now we want to extract the content of the article from the same URL as before. By using the **newpaper** package, it can be done within 4 code lines as follows

# In[62]:


#url = 'https://www.breitbart.com/politics/'
article = Article(url)
article.download()
article.parse()
article.text


# **Comments:**
# 
# Ok now, you can see how different, convenient, and powerful the **newspaper** package compared to the **Request** and **BeautifulSoup** packages are. Let's see the convenience and power of this package as follows.

# ## Scraping all articles and categories
# Let's download all categories from the ***vnexpress.net***

# ### Collecting to the webpage

# In[138]:


vep_paper = newspaper.build('https://kenh14.vn/')
vep_paper


# ### Explore all url links

# In[139]:


art=[]
for article in vep_paper.articles:
    print(article.url)
    art.append(article)
print('The number of Articles on the vnexpress website: %d'%len(art))


# ### Explore all categories

# In[140]:


cat=[]
for category in vep_paper.category_urls():
    print(category)
    cat.append(category)
print('The number of categories on the vnexpress website: %d'%len(cat))


# ### Creating the corpus

# In[136]:


import sys
corpus = []
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


# In[137]:


corpus[1]


# In[ ]:





# In[ ]:





# In[ ]:





# Now we can actually download them
# ## downloading them
# Since this type of scraping can lead to your IP address getting flagged by some news sites, I've added a small sleep of 1 second between each article download. Just in case we get flagged, make sure to save our corpus. 

# In[97]:


breitbart = newspaper.build('http://www.breitbart.com/big-government/')


# In[99]:


len(breitbart.articles)


# In[100]:


corpus = []
count = 0
for article in breitbart.articles:
    time.sleep(1)
    article.download()
    article.parse()
    text = article.text
    corpus.append(text)
    if count % 10 == 0 and count != 0:
        print('Obtained {} articles'.format(count))
    count += 1


# # Attempt 3: alpha_vantage
# 
# https://github.com/Derrick-Sherrill/DerrickSherrill.com/blob/master/stocks.py
# 
# https://github.com/RomelTorres/alpha_vantage
# 
# https://github.com/RomelTorres/alpha_vantage
# 
# 
# https://medium.com/@samanamp/fetching-live-stock-market-data-with-python-and-alphavantage-7d0ff8a8d2e4

# ## Installation

# In[162]:


get_ipython().system('pip install alpha_vantage')


# ## Prepration

# In[163]:


import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


# In[164]:


api_key = 'EQ66HWXJM8SYO3XY'


# In[165]:


ts = TimeSeries(key=api_key, output_format='pandas')


# ## Stock prices

# ### Havesting

# In[166]:


data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')


# ### Showing data

# In[181]:


from pprint import pprint
print('The information on data:')
pprint(meta_data )


# In[172]:


print('The observation in the head:')
display(data.head(5))
print('The observation in the tail:')
display(data.tail(5))


# ### Creating a live plot
# 
# https://gist.github.com/nikhilkumarsingh/1dcec96a1eb0aeb8975fc13ec5825d43
# 
# https://www.youtube.com/watch?v=Ercd-Ip5PfQ
# 
# https://www.udemy.com/course/plotly-dash/
# 
# https://pythonprogramming.net/live-graphs-matplotlib-tutorial/
# 
# https://saralgyaan.com/posts/python-realtime-plotting-matplotlib-tutorial-chapter-9-35-36/

# #### Tutorials

# In[258]:


import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1


# In[259]:


#from pylive import live_plotter
import numpy as np

size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []
while True:
    rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)


# In[249]:


get_ipython().system('python Live_plot.py')


# In[251]:


import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_values, y_values)


# In[252]:


ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()


# In[232]:


import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_values, y_values)


ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()


# #### API

# In[234]:


get_ipython().system('pip install nsetools')


# In[235]:


import csv
import time
import pandas as pd
from nsetools import Nse
from pprint import pprint
from datetime import datetime

nse = Nse()

while True:
    q = nse.get_quote('infy')
    now = datetime.now().strftime("%H:%M:%S")
    row = [now, q['lastPrice']]

    with open('python_live_plot_data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    time.sleep(1)


# In[236]:


import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate():
    data = pd.read_csv('python_live_plot_data.csv')
    x_values = data['Time']
    y_values = data['Price']
    plt.cla()
    plt.plot(x_values, y_values)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Infosys')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, 5000)

plt.tight_layout()
plt.show()


# In[214]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Live plot

# In[24]:


style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# In[ ]:


def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


# ## The exchagne rates

# In[12]:


from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt
cc = ForeignExchange(key='YOUR_API_KEY',output_format='pandas')
data, meta_data = cc.get_currency_exchange_intraday(from_symbol='CAD',to_symbol='USD')
print(data)


# ### Live plot
# 

# In[29]:


import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

i = 0
x, y = [], []

while True:
    #stockchart(symbol)

    ts = TimeSeries(key='EQ66HWXJM8SYO3XY', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='full')
    #data['4. close'].plot()
    #plt.title('Stock chart')
    #plt.show()
    x.append(i)
    y.append(data['4. close'])
    
    ax1.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax1.set_xlim(left=max(0, i-50), right=i+50)
    time.sleep(0.1)
    i += 1


# In[ ]:





# In[13]:


data['4. close'].plot()
plt.tight_layout()
plt.title('Intraday CAD/USD')
plt.show()


# # Attempt 4
# 
# https://www.edureka.co/blog/web-scraping-with-python/#whyweb

# In[2]:


get_ipython().system('pip install selenium')


# In[5]:


from selenium import webdriver
from bs4 import BeautifulSoup
# from BeautifulSoup import BeautifulSoup
import pandas as pd


# In[ ]:





# In[ ]:




