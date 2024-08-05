import json
import os

from dotenv import load_dotenv
import splunklib.client as client

class Splunk_indexer:
    load_dotenv()  
    def __init__(self,index_name) -> None:
        self.index_name = index_name
        self.conncetion = client.connect(host=os.getenv("host"), username=os.getenv("username"), password=os.getenv("password"), autologin=True)

    @property
    def create_index(self) -> None:
        """
        This method will create the index , the name of index is the argument
        # """
        if self.index_name not in self.conncetion.indexes:
            self.conncetion.indexes.create(self.index_name)    
                    
    def upload_datas(self, datas_to_upload):
        """
        Upload a json datas to splunk, the argument must be a list of dict
        """
        index = self.conncetion.indexes[self.index_name]

        if self.index_name == "pastefo":
            for datas in datas_to_upload:
                for data in datas.items():

                    json_to_upload = {
                    f"user": data[0],
                    "infos": datas[data[0]]["Infos"],
                    "paste_content": datas[data[0]]["Pastes"],
                    "source": "python_automation",
                    "sourcetype": "python_automation:pastefo"}
                    json_data = json.dumps(json_to_upload)
                    index.submit(json_data)
                    
        elif self.index_name == "pastebin":
            for data in datas_to_upload.items():

                json_to_upload = {
                f"user": data[0],
                "Link": datas_to_upload[data[0]]["Pastes"],
                "source": "python_automation",
                "sourcetype": "python_automation:pastebin"}
                json_data = json.dumps(json_to_upload)
                index.submit(json_data)
