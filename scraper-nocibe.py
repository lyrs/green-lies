#!/usr/bin/env python3

"""
Scraper for nocibe.fr for a single product
"""

import json
import urllib.request
from bs4 import BeautifulSoup

# setup
URL = "https://www.nocibe.fr/seem-soap-studio-strata-stone-savon-parfume-160g-solide-s263599"
with urllib.request.urlopen(URL) as page_source:
    page = page_source.read().decode('utf-8')
    soup = BeautifulSoup(page, features="html.parser").find('section', id='productPage')

# scraping
entry = {}

title = soup.find(class_='prdct__designation')
entry['brand'] = title.find(class_='prdct__name').text
entry['name'] = title.find(attrs={'itemprop':'name'}).text

entry['labels'] = [label.text.strip() for label in soup.find(class_="prdct__labels").find_all('li')]

details = soup.find(class_="prdct__details-wrap")
entry['description'] = details.find(id='description').text
entry['ingredients'] = details.find(id='ingredients').text

print(json.dumps(entry, indent=2, ensure_ascii=False))
