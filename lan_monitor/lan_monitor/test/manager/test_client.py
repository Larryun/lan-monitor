import unittest
from lan_monitor.model import status
from lan_monitor.util import create_mongo_client, read_yaml
from lan_monitor.manager.client import ClientManager
from lan_monitor.model.status import ClientModel
from time import time

mc = create_mongo_client()
config = read_yaml("../config/config.test.yaml")

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


class TestClientManager(unittest.TestCase):

    def setUp(self):
        self.client_manager = ClientManager(mc, config)
        self.client_manager.client_collection.drop()
        self.client_manager.status_collection.drop()
        return super().setUp()

    def test_get_client(self):
        self.client_manager.insert_client(client1)
        res = self.client_manager.get_client({
            "mac_addr": "ffff:ffff:ffff:ffff",
        })
        self.assertEqual(res[0]["name"], "client1")

    def test_insert_client(self):
        # add the first client
        self.client_manager.insert_client(client1)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         1)

        # check name of client
        self.assertEqual(self.client_manager.get_client({
            "mac_addr": "ffff:ffff:ffff:ffff",
        })[0]["name"], "client1")

        # add client with same mac_addr but different name
        self.client_manager.insert_client(client2)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({
            "mac_addr": "ffff:ffff:ffff:ffff",
        }), 1)
        # check if client name updated
        self.assertEqual(self.client_manager.get_client({
            "mac_addr": "ffff:ffff:ffff:ffff",
        })[0]["name"], "client2")

        self.client_manager.insert_client(client3)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         2)
        # check if client name updated
        self.assertEqual(self.client_manager.get_client({
            "mac_addr": "ffff:ffff:ffff:fffe",
        })[0]["name"], "client3")

    def test_insert_client_status(self):
        self.client_manager.insert_client(client1)
        client1_id = self.client_manager.get_client({"name": client1["name"]})[0]["_id"]

        one_minute = 60
        date1 = time()

        client_status1 = status.ClientStatusRecordModel({
            "client_id": client1_id,
            "ip_addr": "1.1.1.1"
        }, timestamp=date1)


        client_status2 = status.ClientStatusRecordModel({
            "client_id": client1_id,
            "ip_addr": "1.1.1.1"
        }, timestamp=date1 + one_minute)

        self.client_manager.insert_client_status(client_status1)
        self.client_manager.insert_client_status(client_status2)
        res = self.client_manager.get_client_status({})

        for i in res:
            self.assertTrue(i["client_id"], client1_id)
            self.assertTrue(i["ip_addr"], "1.1.1.1")
