import newspaper

URL = "https://www.itmedia.co.jp/"
webdata = newspaper.build(URL, momoize_articles=False)

i = 1
for article in webdata.articles:
    article.download()
    article.perse()
    article.nlp()