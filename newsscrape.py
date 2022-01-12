# import newspaper
from newspaper import Article

URL = "https://news.yahoo.co.jp/pickup/6415002"
article = Article(URL)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)