from lan_monitor.manager.base import BaseManger
from lan_monitor.model import status
from bson import ObjectId
import datetime
import pymongo


class ClientManager(BaseManger):

    def __init__(self, mongo_client, config):
        super().__init__(mongo_client, config)
        self.db = self.mc[self.config["mongodb"]["db"]]
        self.client_collection = self.db["client"]
        self.status_collection = self.db["status"]

    def has_client(self, client_id: str):
        return self.client_collection.count_documents({"client_id": ObjectId(client_id)}) > 0

    def _get_client(self, query: dict, include_id=False):
        if include_id:
            return self.client_collection.find(query)
        else:
            return self.client_collection.find(query, {"_id": False})

    def _get_client_status(self, query: dict, include_id=False):
        if include_id:
            return self.status_collection.find(query)
        else:
            return self.status_collection.find(query, {"_id": False})

    def get_all_clients(self, include_id=False):
        return self._get_client({}, include_id)

    def get_client_by_id(self, client_id: str, include_id=False):
        query = {"_id": client_id}
        return self._get_client(query, include_id)

    def get_client_by_mac_addr(self, mac_addr: str, include_id=False):
        query = {"mac_addr": mac_addr}
        return self._get_client(query, include_id)

    def get_client_status_by_id(self, client_id: str, include_id=False):
        query = {"client_id": ObjectId(client_id)}
        return self._get_client_status(query, include_id)

    def get_client_status_by_time_range(self, client_id: str, start_time: float, end_time: float):
        query = {
            "client_id": ObjectId(client_id),
            "timestamp": {
                "$gte": start_time,
                "$lt": end_time,
            }
        }
        return self._get_client_status(query)


    def insert_client(self, client: status.ClientModel):
        """Add a client to client collection, update if exists

        Args:
            client (ClientModel): client to be insert
        """
        # create if not exists
        self.client_collection.replace_one(
            {"mac_addr": client.mac_addr},
            client.to_json(),
            upsert=True
        )

    def insert_client_status(self, client_status: status.ClientStatusRecordModel):
        """Insert a stutus of client to client collection

        Args:
            client_status (ClientStatusRecordModel): client status to be insert
        """
        self.status_collection.insert_one(client_status.to_json())
