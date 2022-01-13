import newspaper
import csv
import datetime

URL = "https://www.bloomberg.co.jp/"
response = newspaper.build(URL, memoize_articles = False)

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "Bloomberg" + csv_date + ".csv"

f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["No", "Title", "URL", "Summary"]
writer.writerow(csv_header)

i = 0
for article in response.articles:
    csvlist = []
    article.download()
    article.parse()
    article.nlp()
    # print("Content", str(i), ":", article.title)
    # print(article.url)
    # print(article.summary, end="\n\n")
    csvlist.append(str(i))
    csvlist.append(article.title)
    csvlist.append(article.url)
    csvlist.append(article.summary)

    if i > 9:
        break
    i = i + 1


# print(csv_date)
