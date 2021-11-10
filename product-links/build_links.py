#!/usr/bin/env python3
"""
Script for creating a list of ref links for Nocibe website.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm

def get_links(file):
    """Get links from a webpage snapshot."""
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html5lib')
    links = soup.find_all("a", {"class": "proditem__link"})
    return [link['href'] for link in links]

def build_links(cats=("bio","clean","naturelle")):
    """Saves links to a file."""
    linkset = set()
    for cat in cats:
        linkset.update(set(get_links(cat+".htm")))
        print(f"Category \"{cat}\" done.")

    with open("hrefs.txt", 'w+', newline='\n', encoding='utf-8') as hrefs:
        for link in tqdm(linkset):
            hrefs.write(link+'\n')
    print("Links extracted.")

build_links()
