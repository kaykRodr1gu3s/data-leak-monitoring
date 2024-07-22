import requests
import bs4
import re

class Pastefo:
    def __init__(self):
        self.url_base = "https://paste.fo/recent"
        self.user_links = []
        self.all_datas = []

    def user_link(self, num_page):
        """
        This method will collect the user and save in a list
        """
        req = requests.get(f"{self.url_base}/{num_page}")
        bs = bs4.BeautifulSoup(req.content, "html.parser")


        def post_href():
            posts = bs.find_all("tr")

            for post in posts:
                if not post.get('class'):
                    links = post.find_all("a", href=re.compile(r"/user/."))
                    for link in links:
                        if link.attrs['href'] not in self.user_links:
                            self.user_links.append(link.attrs['href'])
            
        post_href()


    def content_tracker(self, links=list):
        all_datas = {}
        for link in links:
            req = requests.get(f"https://paste.fo/{link}")
            bs = bs4.BeautifulSoup(req.content, "html.parser")

            def data_details():
                """
                this function will collect the user that post. The datas are: views, created at and contact
                """    

                data = bs.find("div", class_="profileattributes")
                statistics = data.find_all("h4", class_="paste-info")
                
                for statistic in statistics:

                    all_datas[link] = {"Infos": {}}
                
                    if statistic.text.strip().split(" ")[0] == "Views":
                        all_datas[link]['Infos']["Views"] = statistic.text.strip().split(" ")[-1]
                    try:
                        contact = bs.find("div", class_="profilecontact")
                        
                        contact = contact.find("a", href=re.compile(r"http."))['href']

                        all_datas[link]["Contact"] = contact
                        
                    except AttributeError:
                        all_datas[link]["Contact"] = "None"            
        
            self.all_datas.append(all_datas)
            data_details()

        return all_datas


    @property
    def main(self):
        for num_page in range(1,6):
            self.user_link(num_page)
            self.content_tracker(self.user_links)
            

pastefo = Pastefo()
pastefo.main    
print(pastefo.all_datas)