import yaml
from pymongo import MongoClient

class BaseManger:

    def __init__(self, mongo_client: MongoClient, config):
        self.mc = mongo_client
        self.config = config

    def close_mongo_client(self):
        self.mc.close()

 