#!/usr/bin/env python3

"""
Simple script downloading page source.
"""

import requests

URLS = ["https://www.sephora.fr/", "https://www.marionnaud.fr/", "https://www.nocibe.fr/"]
HEADER = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

for url in URLS:
    try:
        response = requests.get(url, headers={}, timeout=5)
    except requests.Timeout:
        print("Didn't manage to connect to", url, "without a header!")
        response = requests.get(url, headers=HEADER, timeout=5)
    print("Got", response)
