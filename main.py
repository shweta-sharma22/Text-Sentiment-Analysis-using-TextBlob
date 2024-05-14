from textblob import TextBlob
from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Abraham_Lincoln'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)