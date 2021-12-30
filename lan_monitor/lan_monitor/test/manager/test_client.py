import unittest

from lan_monitor.manager.client import ClientManager
from lan_monitor.model.status import ClientModel, ClientStatusRecordModel
from lan_monitor.util import create_mongo_client, read_yaml

TIME1 = 100

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
        self.client_manager.insert_client(client1)
        self.client_manager.insert_client(client2)
        self.client_manager.insert_client(client3)

        one_minute = 60
        self.client1_id = self.client_manager.get_client_by_mac_addr(client1["mac_addr"],
                                                                     include_id=True)[0]["_id"]
        client_status1 = ClientStatusRecordModel({
            "client_id": self.client1_id,
        }, timestamp=TIME1)

        client_status2 = ClientStatusRecordModel({
            "client_id": self.client1_id,
        }, timestamp=TIME1 + one_minute)

        client_status3 = ClientStatusRecordModel({
            "client_id": self.client1_id,
        }, timestamp=TIME1 + one_minute * 5)

        self.client_manager.insert_client_status(client_status1)
        self.client_manager.insert_client_status(client_status2)
        self.client_manager.insert_client_status(client_status3)

        return super().setUp()

    def test_get_client(self):
        self.client_manager.insert_client(client1)
        res = self.client_manager.get_client_by_mac_addr("ffff:ffff:ffff:ffff")
        self.assertEqual(res[0]["name"], "client1")

    def test_get_client_status_time_range(self):
        res = list(self.client_manager.get_client_status_by_time_range(self.client1_id, TIME1, TIME1 + 120))
        self.assertEqual(res[0]["client_id"], self.client1_id)
        self.assertEqual(res[1]["client_id"], self.client1_id)

        self.assertEqual(res[0]["timestamp"], TIME1)
        self.assertEqual(res[1]["timestamp"], TIME1 + 60)

    def test_insert_client(self):
        # add the first client
        self.client_manager.insert_client(client1)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         2)

        # check name of client
        res = self.client_manager.get_client_by_mac_addr("ffff:ffff:ffff:ffff")
        self.assertEqual(res[0]["name"], "client1")

        # add client with same mac_addr but different name
        self.client_manager.insert_client(client2)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({
            "mac_addr": "ffff:ffff:ffff:ffff",
        }), 1)
        # check if client name updated
        res = self.client_manager.get_client_by_mac_addr("ffff:ffff:ffff:ffff")
        self.assertEqual(res[0]["name"], "client2")

        self.client_manager.insert_client(client3)

        # check client counts
        self.assertEqual(self.client_manager.client_collection.count_documents({}),
                         2)
        # check if client name updated
        res = self.client_manager.get_client_by_mac_addr("ffff:ffff:ffff:fffe")
        self.assertEqual(res[0]["name"], "client3")

    def test_insert_client_status(self):
        res = self.client_manager.get_client_status_by_id(self.client1_id)

        for i in res:
            self.assertTrue(i["client_id"], self.client1_id)
