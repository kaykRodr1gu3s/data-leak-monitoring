import bs4
import os
import requests
import re
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Splunk.main import Splunk_indexer

print()
class Pastebin(Splunk_indexer):
    def __init__(self, index_name):
        "index_name = name for create on splunk, if you already have an index, just pass as argument."

        super().__init__(index_name)

        self.endpoint = "https://pastebin.com/"
        self.all_datas = {}

    @property
    def pastes(self):
        """
        This method will collect the links of the pastes
        """
        req = requests.get(self.endpoint)
        bs = bs4.BeautifulSoup(req.content, "html.parser")
        bs = bs.find("ul", "sidebar__menu")
        pastes = bs.find_all("a", href=re.compile(r"/."))

        paste_link = []

        for paste in pastes:
            paste_link.append(paste["href"])

        return paste_link

    def paste_links(self, paste_link):
        """
        This method will collect the user link and all the paste available on their profile
        """

        user_href = {}

        for paste in paste_link:

            req = requests.get(f"{self.endpoint}/{paste}")
            bs = bs4.BeautifulSoup(req.content, "html.parser")
            username = bs.find("div", class_="username").text.replace("\n", "")
            
            def user_creator():
                links = []
                user_req = requests.get(f"https://pastebin.com/u/{username}")

                bs = bs4.BeautifulSoup(user_req.content, "html.parser")

                all_href = bs.find_all("tr")
                del all_href[0]

                for href in all_href:
                    href = href.find("a")["href"]
                    if href not in links:
                        
                        links.append(href)
                    user_href[username] = {"link": links}

            user_creator()
        return user_href


    def raw_content(self, content_link: dict):
        """
        This method will collect the paste content
        """
        data_list = {}
        cont = 0
        for dict_key in content_link:
            self.all_datas[dict_key] = {"paste": {}}

            for data in content_link[dict_key]["link"]:
                req = requests.get(f"https://pastebin.com/raw{data}")
                if req.status_code == 200:
                    data_list[f"https://pastebin.com/{data}"] = req.content.decode("utf-8").replace("Guide:", " ").replace("\n", "")

                    self.all_datas[dict_key]["Pastes"] = data_list
                    print(f"https://pastebin.com/raw{data}")
                    cont += 1
                    print(cont)

    @property
    def main(self):
        self.raw_content(self.paste_links(self.pastes))

pastebin = Pastebin("pastebin")
pastebin.main
pastebin.create_index
pastebin.upload_datas(pastebin.all_datas)   