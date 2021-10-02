import lan_monitor
from pymongo import MongoClient
from lan_monitor import monitor
from lan_monitor.model import status
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}


# mongod = MongoClient("localhost", 27017,
#                      username="root",
#                      password="root",
#                      authMechanism='SCRAM-SHA-256')
# print(mongod.test.post_collection.insert_one(post).inserted_id)
m = monitor.Monitor("10.0.0.0/24")
print(m.get_clients())
