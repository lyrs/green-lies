import requests
from bs4 import BeautifulSoup
import json

# Header for the GET
headers = {
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document'
}
# Max number of pages
NB_PAGES = 15
# Number of element by pages
NB_ELEMENT_PAGE = 100

def extract_data(url):
    """
    This method get an url and return the associated data from the element
    :param url: the url to get the data from
    :return: the item's information
    """
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    elem = {"BRAND_NAME": soup.select(".brand-name")[0].text.strip(),
            "RANGE": soup.select(".product-name")[1].text.strip(),
            "NAME": soup.select(".product-name-bold")[0].text.strip(),
            'DESCRIPTION': soup.select(".product-description-box")[0].text.strip(),
            "INGREDIENTS": soup.select("#tab-ingredients")[0].findChildren()[3].text.strip()
            }
    return elem


def extract_product_link(index):
    """
    This method gather all the item in the product page, use pagination.
    Use the internal API for gathering information
    :param index: The index of the page
    :return: list of item's URL
    """
    url = 'https://www.sephora.fr/good-for-soin-eco-responsable/?srule=GoLiveSortingRule&sz={}&format=page-element&start={}'.format(NB_ELEMENT_PAGE,index*NB_ELEMENT_PAGE)
    prod = BeautifulSoup(requests.request("GET", url, headers=headers).text, 'html.parser')
    items = prod.select('.product-tile')
    jsons = [json.loads(item.attrs['data-tcproduct']) for item in items]
    link_list = [item.product_url_page for item in jsons]
    return link_list


all_link = []
for page_nb in range(1, NB_PAGES):
    all_link.extend(extract_product_link(page_nb))

all_data = [extract_data(item) for item in all_link]
