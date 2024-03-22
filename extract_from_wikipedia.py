from bs4 import BeautifulSoup
import requests
import re

def extract_from_text(text, n_words):
    words = text.split(" ")
    return [' '.join(chunk) for chunk in zip(*[iter(words)]*n_words)]

pattern = re.compile(r'\[\d+\]')
wikipedia_pages = []

for _ in range(20):
    page = requests.get("https://es.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find_all('p')
    text = p[1].get_text() if len(p) > 2 else ""
    while len(text) < 50 or "\\" in text.replace("\n","").replace("\u200b",""):
        page = requests.get("https://es.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(page.content, 'html.parser')
        p = soup.find_all('p')
        text = p[1].get_text() if len(p) > 2 else ""

    text = re.sub(pattern, '', text.replace("\n","").replace("\u200b","").replace("\xa0","").replace("\ufeff",""))
    wikipedia_pages.extend( extract_from_text(text, 10) )

