import yaml

class BaseManger:

    def __init__(self, mongo_client, config):
        self.mc = mongo_client
        self.config = config

 