from CtrlJson import Control_Json

class IndexPage:
    def __init__(self):
        self.index_config = Control_Json("./config/index/config.json")
        self.s3_path = "page/index/config.json"

    def save_data(self):
        self.index_config.save_json_file()
    
    def add_gione(self):
        self.index_config.file_load()
        self.index_config.json_data['talmo_gione'] += 1
        self.save_data()

        return self.index_config.json_data['talmo_gione']
    
    def add_talmo_him(self):
        self.index_config.file_load()
        self.index_config.json_data['talmo_jinhang'] += 1
        self.save_data()

        return self.index_config.json_data['talmo_jinhang']
    
    def get_talmo_him(self):
        self.index_config.file_load()
         
        return self.index_config.json_data['talmo_jinhang']

    def get_talmo_gione(self):
        self.index_config.file_load()
        
        return self.index_config.json_data['talmo_gione']

    def upload_config(self):
        self.index_config.upload_json(self.s3_path)

    def load_config(self):
        self.index_config.json_data = self.index_config.load_json(self.s3_path)
    
    def reset_json_daily(self):
        self.add_gione()
        self.upload_config()
        self.load_config()
    
class HarvestHair:
    def __init__(self):
        pass