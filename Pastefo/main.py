import requests
import bs4
import re
import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Splunk.main import Splunk_indexer

class Pastefo(Splunk_indexer):
    def __init__(self, index_name):
        """
        index_name = index name to create on splunk or an existent index
        """
        super().__init__(index_name)

        self.url_base = "https://paste.fo"
        self.user_links = []
        self.all_datas = []


    def user_link(self, num_page) -> None:
        """
        This method will collect the user and save in a list
        """
        req = requests.get(f"{self.url_base}/recent/{num_page}")
        bs = bs4.BeautifulSoup(req.content, "html.parser")


        def post_href() -> None:
            """
            This function collect all the user link on https://paste.fo/recent 
            """
            posts = bs.find_all("tr")

            for post in posts:
                if not post.get('class'):
                    links = post.find_all("a", href=re.compile(r"/user/."))
                    for link in links:
                        if link.attrs['href'] not in self.user_links:
                            self.user_links.append(link.attrs['href'])
            
        post_href()

    def content_tracker(self, links: list) -> None:
        """
        This method will request the user and collect all the paste available on the https://paste.fo/<user>

        links = user_link()
        """

        all_datas = {}
        for link in links:
            req = requests.get(f"{self.url_base}/{link}")
            bs = bs4.BeautifulSoup(req.content, "html.parser")
            all_datas[link] = {"Infos" : {}}

            def data_details(link=link) -> None:
                """
                this function will collect the user that post. The datas are: views, created at and contact
                """    

                statistics = bs.find("div", class_="paste-about")
                infos = statistics.find_all("h4")
                
                for info in infos:
                    if info.text.strip().split(" ")[0] == "Pastes":
                        all_datas[link]["Infos"]["Pastes"] = info.text.strip().split(" ")[-1] 
                        
                    else:
                        all_datas[link]["Infos"]["Views"] = info.text.strip().split(" ")[-1] 
                        
                try:
                    contact = bs.find("div", class_="profilecontact")
                    contact_links = contact.find_all("a", href=re.compile(r"\."))
                    for contact_link in contact_links:
                        all_datas[link]["Infos"]["Contact"] = contact_link["href"]
                       
                except:
                    all_datas[link]["Infos"]["Contact"] = "None"

            def paste_href():
                """
                This function collect the content of the paste
                """

                table_href = bs.find("table", class_="pastelist profilepastelist")
                table_href = table_href.find_all("tr")
                paste_data = []

                del table_href[0]

                for table in table_href:

                    datas = table.find_all("td")
                    content = requests.get(f"{self.url_base}/raw/{datas[0].find("a")["href"]}").content.decode("utf-8").replace("\r\n", " ")
                    paste_data.append({"Link": f"https://paste.fo/{datas[0].find("a")["href"]}", "View": datas[1].text, "Paste Content": content})

                all_datas[link][f"Pastes"] = paste_data

            data_details()
            paste_href()

        self.all_datas.append(all_datas)

    @property
    def main(self):
        """
        the main method joins all other methods with their respective arguments
        """
        
        for num_page in range(1,6):     
            self.user_link(num_page)
            self.content_tracker(self.user_links)

pastefo = Pastefo("pastefo")
pastefo.main    
pastefo.create_index
pastefo.upload_datas(pastefo.all_datas)