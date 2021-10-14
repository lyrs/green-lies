import requests
from bs4 import BeautifulSoup

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
NB_PAGES = 77


def extract_data(url):
    """
    This method get an url and return the associated data from the element
    :param url: the url to get the data from
    :return: the item's information
    """
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    infos = soup.select(".productInformationSection > .row")
    elem = {}
    for row in infos:
        elem.update({row.select_one('h3').text.strip(): "".join([p.text.strip() for p in row.select('p')])})
    elem.update({"BRAND_NAME": soup.select(".productBrandName")[0].text.strip(),
                 "RANGE": soup.select(".producRangeName")[0].text.strip(),
                 "NAME": soup.select(".productName")[0].text.strip(),
                 "ID": soup.select(".product-code")[0].text.strip().replace("Ref: ", "")
                 })
    return elem


def extract_product_link(index):
    """
    This method gather all the item in the product page, use pagination.
    :param index: The index of the page
    :return: list of item's URL
    """
    url = 'https://www.marionnaud.fr/tous-les-produits?q=%3Arank-desc&page={}&pageSize=100'.format(index)
    prod = BeautifulSoup(requests.request("GET", url, headers=headers).text, 'html.parser')
    items = prod.select('.productMainLink')
    if len(items) > 100:  # Sometimes advertisement popup on the top of the page and use the same template
        del items[:len(items) - 100]  # For showing items, so we remove it for not having duplicate data
    link_list = ["https://www.marionnaud.fr" + item.find("a", href=True).attrs['href'] for item in items]
    return link_list


all_link = []
for page_nb in range(1, NB_PAGES):
    all_link.extend(extract_product_link(page_nb))

all_data = [extract_data(item) for item in all_link]