import newspaper

URL = "https://www.bloomberg.co.jp/"
response = newspaper.build(URL, memoize_articles = False)

for article in response.articles:
    article.download()
    article.parse()
    article.nlp()
    print(article.title)
    print(article.url)