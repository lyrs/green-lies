#!/usr/bin/env python3
"""
Script that build the cosmetic product database from Nocibe.
It gets the links from a website snapshot and scrape data for every product,
then saves it in a TinyDB for later use.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm
from tinydb import TinyDB
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
    """The exact data scraping.
    
    Returns: a dict with a product attributes
    """

    soup = BeautifulSoup(source, features="html.parser").find('section', id='productPage')

    entry = {}
    entry['url'] = url

    title = soup.find(class_='prdct__designation')
    entry['brand'] = title.find(class_='prdct__name').text
    entry['name'] = title.find(attrs={'itemprop':'name'}).text
    
    try:
        entry['labels'] = [label.text.strip() for label in soup.find(
            class_="prdct__labels").find_all('li')]
    # is out of stock
    except AttributeError:
        print("Labels missing!")
        entry['in_stock'] = False
        return entry

    details = soup.find(class_="prdct__details-wrap")
    entry['description'] = details.find(id='description').text
    
    try:
        entry['ingredients'] = details.find(id='ingredients').text
        if len(entry['ingredients']) > 36: # arbitrary number
            entry['is_cosmetic'] = True
        else:
            entry['is_cosmetic'] = False
    # is not a cosmetic
    except AttributeError:
        entry['ingredients'] = "None"
        entry['is_cosmetic'] = False

    entry['in_stock'] = True
    
    return entry
    

def get_item(url):
    """Retrieves data from a product page."""
    # setup
    result = {"url": url}
    try:
        page = requests.get(url, headers=HEADER, timeout=60)
    except requests.ConnectionError as e:
        print("Connection Error.")
        print(e)
        return result
    except requests.Timeout as e:
        print("Timeout Error.")
        print(e)
        return result
    except requests.RequestException as e:
        print("General Error.")
        print(e)
        return result


    if page.status_code != 200:
        print("Couldn't fetch the page.")
        return result

    try:
        result = scrape(page.text, url)
    except AttributeError:
        print("Couldn't scrape.")
        pass 
        
    return result
      
# TO DO
# check if it's partially build and keep scrapping from nth link
if os.path.exists('db.json'):
    raise NameError("Database already exists!")

db = TinyDB('db.json')

for link in tqdm(load_links()):
    item = get_item(link)
    db.insert(item)
