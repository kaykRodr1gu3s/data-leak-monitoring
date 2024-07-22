import requests
import bs4 
import re


class Pastebin:

    def __init__(self):
        self.endpoint = "https://pastebin.com/"
        self.all_datas = {}

    @property
    def pastes(self):

        req = requests.get(self.endpoint)
        bs = bs4.BeautifulSoup(req.content, "html.parser")
        bs = bs.find("ul", "sidebar__menu")
        pastes = bs.find_all("a", href=re.compile(r"/."))

        paste_link = []

        for paste in pastes:
            paste_link.append(paste["href"])

        return paste_link

    def paste_links(self, paste_link):
        
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
        data_list = []
        for dict_key in content_link:
            print(dict_key)
            for data in content_link[dict_key]["link"]:

                req = requests.get(f"https://pastebin.com/raw{data}")
                data_list.append({f"https://pastebin.com/raw/{data}": req.content.decode("utf-8").replace("\n", " ")})
                self.all_datas[dict_key] = data_list
                
    def main(self):
        self.raw_content(self.paste_links(self.pastes))
        print(self.all_datas)

pastebin = Pastebin()
pastebin.main()