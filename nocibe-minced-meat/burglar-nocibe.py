from bs4 import BeautifulSoup
import csv

biohrefs = []
cleanhrefs = []
naturalhrefs = []

with open("bio.htm", encoding="utf-8") as fbio:
    biosoup = BeautifulSoup(fbio, "html5lib")
    biolinks = biosoup.find_all("a", {"class": "proditem__link"})
    for link in biolinks:
        biohrefs.append(link["href"])

with open("clean.htm", encoding="utf-8") as fclean:
    cleansoup = BeautifulSoup(fclean, "html5lib")
    cleanlinks = cleansoup.find_all("a", {"class": "proditem__link"})
    for link in cleanlinks:
        cleanhrefs.append(link["href"])

with open("naturelle.htm", encoding="utf-8") as fnatural:
    naturalsoup = BeautifulSoup(fnatural, "html5lib")
    naturallinks = naturalsoup.find_all("a", {"class": "proditem__link"})
    for link in naturallinks:
        naturalhrefs.append(link["href"])

with open("hrefs-nocibe.csv", "w", newline="") as hrefscsv:
    writer = csv.writer(hrefscsv)
    writer.writerow(["url","cat"])
    writer.writerows([item, "bio"] for item in biohrefs)
    writer.writerows([item, "clean"] for item in cleanhrefs)
    writer.writerows([item, "natural"] for item in naturalhrefs)
    hrefscsv.close()
