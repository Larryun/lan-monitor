from lan_monitor.manager.base import BaseManger
from lan_monitor.model import status

class ClientManager(BaseManger):

    def __init__(self, mongo_client, config):
        super().__init__(mongo_client, config)
        self.db = self.mc[self.config["mongodb"]["db"]]
        self.client_collection = self.db["client"]
        self.status_collection = self.db["status"]

    def add_client(self, client: status.ClientModel):
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
