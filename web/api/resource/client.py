from bson import ObjectId
from flask_restful import Resource, reqparse
from pymongo import DESCENDING

from db import get_manager

client_status_parser = reqparse.RequestParser()
client_status_parser.add_argument("limit",
                                  default=10,
                                  type=int)


class Client(Resource):

    def get(self):
        manager = get_manager()
        return list(manager.get_client({}, include_id=True))


class ClientStatus(Resource):

    def get(self, client_id):
        """ get recent ClientStatus by mac_addr"""
        # TODO add parameters for time range
        manager = get_manager()
        args = client_status_parser.parse_args()
        return list(
            manager.get_client_status({
                "client_id": ObjectId(client_id)
            }).sort(
                "timestamp", DESCENDING
            ).limit(
                args.limit
            )
        )
