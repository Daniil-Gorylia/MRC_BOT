import requests
import html.parser
from bs4 import BeautifulSoup as bs
import database
import re


def MRC_primen():
    url = requests.get("https://nalog.gov.by/actual/cigarettes/")
    soup = bs(url.text, 'html.parser')
    card = soup.find_all(href=re.compile('/upload/iblock/'), download=re.compile('применяемых'))
    a = []
    for links in card:
        if links not in a:
            try:
                a.append(links.get('href'))
            except:
                continue
    return a


def MRC_zayav():
    url = requests.get("https://nalog.gov.by/actual/cigarettes/")
    soup = bs(url.text, 'html.parser')
    card = soup.find_all(href=re.compile('/upload/iblock/'), download=re.compile('заявленных'))
    b = []
    for links in card:
        if links not in b:
            try:
                b.append(links.get('href'))
            except:
                continue
    return b
