import newspaper

# URL = "https://www.itmedia.co.jp/"
URLs = ["https://www.itmedia.co.jp/", "https://thebridge.jp/"]
# webdata = newspaper.build(URL, memoize_articles = False)

# i = 1
# for article in webdata.articles:
#     article.download()
#     article.parse()
#     article.nlp()
#     print("Content:", str(i), ":", article.title)
#     print(article.url)
#     print(article.summary, end="\n\n")

#     if i > 9:
#         break
#     i = i + 1

for url in URLs:
    webdata = newspaper.build(URL, memoize_articles = False, language="ja")