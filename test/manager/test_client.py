import unittest
from lan_monitor.model import status
from lan_monitor.util import create_mongo_client, read_yaml
from lan_monitor.manager.client import ClientManager
from lan_monitor.model.status import ClientModel
import datetime

mc = create_mongo_client()
config = read_yaml("config/config.test.yaml")


class TestClientManager(unittest.TestCase):

    def setUp(self):
        self.client_manager = ClientManager(mc, config)
        self.client_manager.client_collection.drop()
        return super().setUp()

    def test_add_client(self):
        # add the first client
        client1 = ClientModel({
            "mac_addr": "ffff:ffff:ffff:ffff",
            "name": "client1"
        })
        client2 = ClientModel({
            "mac_addr": "ffff:ffff:ffff:ffff",
            "name": "client2"
        })
        client3 = ClientModel({
            "mac_addr": "ffff:ffff:ffff:fffe",
            "name": "client3"
        })
        self.client_manager.add_client(client1)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         1)

        # check name of client
        self.assertEqual(self.client_manager.client_collection.find({
            "mac_addr": "ffff:ffff:ffff:ffff",
        })[0]["name"], "client1")

        # add client with same mac_addr but different name
        self.client_manager.add_client(client2)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({
            "mac_addr": "ffff:ffff:ffff:ffff",
        }), 1)
        # check if client name updated
        self.assertEqual(self.client_manager.client_collection.find({
            "mac_addr": "ffff:ffff:ffff:ffff",
        })[0]["name"], "client2")

        self.client_manager.add_client(client3)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         2)
        # check if client name updated
        self.assertEqual(self.client_manager.client_collection.find({
            "mac_addr": "ffff:ffff:ffff:fffe",
        })[0]["name"], "client3")
