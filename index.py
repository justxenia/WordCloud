import requests
import urllib.request
import time
import spacy
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

topic="putin"
url ="https://www.google.com/search?q="+topic+"&tbm=nws&hl=en-US&gl=US""&as_qdr=w4"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('div', attrs = {'class': 'ZINbbc'})
descriptions = []
for result in results:
    try:
        description = result.find('div', attrs={'class':'s3v9rd'}).get_text()
        if description != '':
            descriptions.append(description)
    except:
        continue
text = ''.join(descriptions)

sp = spacy.load('en_core_web_sm')
doc = sp(text)
newText =''
for word in doc:
 if word.pos_ in ['ADJ', 'NOUN']:
  newText = " ".join((newText, word.text.lower()))
wordcloud = WordCloud(background_color='pink', max_words=50, relative_scaling=0.21, stopwords=STOPWORDS).generate(newText)
plt.figure(figsize=(10,10), facecolor = "None")
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()