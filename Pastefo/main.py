import requests
import bs4


class Pastefo:
    def __init__(self):
        self.url_base = "https://paste.fo/recent"
        
    @property
    def content(self):
        req = requests.get(self.url_base)
        bs = bs4.BeautifulSoup(req.content, "html.parser")


pastefo =  Pastefo()
pastefo.content