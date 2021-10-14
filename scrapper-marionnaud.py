from bs4 import BeautifulSoup
import requests

headers = {
  'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
  'sec-ch-ua-platform': '"Windows"',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Dest': 'document'
}


def extract_data(url):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    temp = soup.select(".productInformationSection > .row")
    data = [x.text.strip("\n\r\t\f\\") for x in temp]
    elem = {}
    for y in data:
        if y.startswith("DESCRIPTION"):
            elem.update({"DESCRIPTION": y.replace("DESCRIPTION","").strip()})
        if y.startswith("INGRÉDIENTS"):
            elem.update({"INGRÉDIENTS": y.replace("INGRÉDIENTS", "").strip()})
    elem.update({"BRAND_NAME": soup.select(".productBrandName")[0].text.strip(),
                 "RANGE": soup.select(".producRangeName")[0].text.strip(),
                 "NAME": soup.select(".productName")[0].text.strip(),
                 "ID": soup.select(".product-code")[0].text.strip().replace("Ref: ","")
                 })
    return elem


def extract_product_link(index):
    url = 'https://www.marionnaud.fr/tous-les-produits?q=%3Arank-desc&page={}&pageSize=100'.format(index)
    prod = BeautifulSoup(requests.request("GET", url, headers=headers).text, 'html.parser')
    temp = prod.select('.productMainLink')
    if len(temp) > 100:
        del temp[:len(temp)-100]
    temp = ["https://www.marionnaud.fr" + x.find("a",href=True).attrs['href'] for x in temp]
    return temp


it = []
for i in range(1,77):
    it.extend(extract_product_link(i))

data = [extract_data(x) for x in it]








