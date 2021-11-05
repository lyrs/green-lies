import urllib.request
from bs4 import BeautifulSoup
from tinydb import TinyDB
import csv

def item(url):
    with urllib.request.urlopen(url) as page_source:
        page = page_source.read().decode('utf-8')
        soup = BeautifulSoup(page, features="html.parser").find('section', id='productPage')

    # scraping
    entry = {}

    title = soup.find(class_='prdct__designation')
    entry['brand'] = title.find(class_='prdct__name').text
    entry['name'] = title.find(attrs={'itemprop': 'name'}).text

    entry['labels'] = [label.text.strip() for label in soup.find(class_="prdct__labels").find_all('li')]

    details = soup.find(class_="prdct__details-wrap")
    entry['description'] = details.find(id='description').text
    entry['ingredients'] = details.find(id='ingredients').text

    return entry


db = TinyDB('db.json')

with open('nocibe-minced-meat/hrefs-nocibe.csv', newline='') as csvfile:
    nocibe_csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    nocibe_csv_reader.__next__() #Removing the headers 
    skiped = 0
    for row in nocibe_csv_reader:
        print(row[0])
        try:
            db.insert(item(row[0]))
        except AttributeError:
            print("No information for this item")
            skiped = skiped +1
        print(nocibe_csv_reader.line_num)
    print("Skipped items : ",skiped)


