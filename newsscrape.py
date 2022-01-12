# import newspaper
from newspaper import Article

URL = "https://www.reuters.com/world/uk/party-over-uk-pm-johnson-faces-crunch-day-parliament-2022-01-12/"
article = Article(URL)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)
print(article.text)
print(article.title)