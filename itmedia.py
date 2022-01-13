import newspaper

URL = "https://www.itmedia.co.jp/"
article = newspaper.build(URL, momoize_articles=False)

i = 1
for i in article.articles:
    article.download()