import newspaper
import csv
import datetime

URL = "https://www.bloomberg.co.jp/"
response = newspaper.build(URL, memoize_articles = False)

i = 0
# for article in response.articles:
#     article.download()
#     article.parse()
#     article.nlp()
#     print("Content", str(i), ":", article.title)
#     print(article.url)
#     print(article.summary, end="\n\n")

#     if i > 9:
#         break
#     i = i + 1

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "Bloomberg" + csv_date + ".csv"
# print(csv_date)

f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["No", "Title", "URL", "Summary"]