#!/usr/bin/env python3
"""
Script that build the cosmetic product database from Nocibe.
It gets the links from a website snapshot and scrape data for every product,
then saves it in a TinyDB for later use.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm
from tinydb import TinyDB
from requests_html import HTML
import requests
import os.path

HEADER = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

def get_links(file):
    """Get links from a webpage snapshot."""
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html5lib')
    links = soup.find_all("a", {"class": "proditem__link"})
    return [link['href'] for link in links]

def load_links(cats=("bio","clean","naturelle"), dpath="product-links/"):
    """Returns a list of links."""
    if not os.path.exists("hrefs.txt"):
        print("Caching links...")
        linkset = set()
        for cat in cats:
            # TO DO
            # make it deterministic 
            linkset.update(set(get_links(dpath+cat+".htm")))
            print(f"Category \"{cat}\" done.")

        with open("hrefs.txt", 'w', newline='\n', encoding='utf-8') as hrefs:
            for link in tqdm(linkset):
                hrefs.write(link+'\n')
        print("Links extracted.")
    else:
        with open("hrefs.txt", 'r', encoding='utf-8') as hrefs:
            linkset = hrefs.read().split()

    return linkset

def scrape(source, url):
    """The exact data scraping."""
    soup = source.find("section.prdct", first=True)

    entry = {}
    entry['url'] = url

    entry['brand'] = soup.find("div.prdct__name", first=True).text
    entry['name'] = soup.find("div[itemprop=name]", first=True).text
    
    try:
      entry['labels'] = soup.find("div.prdct__labels", first=True).text.split('\n')
    except AttributeError as e:
      print("Labels missing!")
      print(str(e))
      return {}

    entry['description'] = soup.find("div[id=description]", first=True).text
    try:
        entry['ingredients'] = soup.find("div[id=ingredients]", first=True).text
    # is not a cosmetic
    except AttributeError:
        print("Not a cosmetic!")
        entry['ingredients'] = "None"

    return entry
    

def get_item(url):
    """Retrieves data from a product page."""
    # setup
    page = requests.get(url, headers=HEADER, timeout=60)

    if page.status_code != 200:
        print(f"Couldn't accces {url}")
        return {}

    try:
      result = scrape(HTML(html=page.text), url)
    except AttributeError:
      print("Something went wrong...?")
      result = {} 
        
    return result
      
# TO DO
# check if it's partially build and keep scrapping from nth link
if os.path.exists('db.json'):
    raise NameError("Database already exists!")

db = TinyDB('db.json')

for link in tqdm(load_links()):
    try:
        item = get_item(link)
    except requests.ConnectionError as e:
        print()
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
    except requests.Timeout as e:
        print()
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print()
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print()
        print("Someone closed the program")
    
    if item:
        db.insert(item)
    else:
        db.insert({"url":link})
