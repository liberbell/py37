import newspaper

URL = "https://www.bloomberg.co.jp/"
response = newspaper.build(URL)

for atticle in response.articles:
    article.download()