import unittest
from lan_monitor.model import status
from time import time
from bson.objectid import ObjectId


class TestClientModel(unittest.TestCase):

    def test_no_name_client(self):
        client = status.ClientModel({
            "mac_addr": "test_mac",
        })

        self.assertEqual(client.mac_addr, "test_mac")
        self.assertEqual(client.name, "")

    def test_client(self):
        client = status.ClientModel({
            "mac_addr": "test_mac",
            "name": "name1"
        })

        self.assertEqual(client.mac_addr, "test_mac")
        self.assertEqual(client.name, "name1")


class TestClientStatusRecordModel(unittest.TestCase):

    def test_status(self):
        obj_id = ObjectId("61595e74695979fbbd6bfc83")
        now = time()
        record = status.ClientStatusRecordModel({
            "client_id": obj_id,
            "ip_addr": "123.123.123.123"
        }, timestamp=now)

        self.assertEqual(record.client_id,  obj_id)
        self.assertEqual(record.timestamp,  now)
        self.assertEqual(record.ip_addr, "123.123.123.123")
