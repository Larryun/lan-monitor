import unittest
from lan_monitor.model import status
import datetime

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
        now = datetime.datetime.utcnow()
        record = status.ClientStatusRecordModel({
            "client": "a1b2",
            "ip_addr": "123.123.123.123"
        }, timestamp=now)

        self.assertEqual(record.client,  "a1b2")
        self.assertEqual(record.timestamp,  now)
        self.assertEqual(record.ip_addr, "123.123.123.123")