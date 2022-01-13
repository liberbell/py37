from newspaper import Article

URL = "https://diamond-rm.net/management/102956/"
article = Article(URL, memoize_articles = False)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)
print(article.text.replace("\n", ""))