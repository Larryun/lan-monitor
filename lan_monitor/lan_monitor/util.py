import yaml
from pymongo import MongoClient


def create_mongo_client(host="localhost", port=27017,
                        username="root", password="root"):
    mongod = MongoClient(host, port,
                         username=username,
                         password=password,
                         authMechanism='SCRAM-SHA-1')
    # authMechanism = 'SCRAM-SHA-256')
    return mongod


def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)
