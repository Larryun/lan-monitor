from flask_restful import Resource, reqparse
from pymongo import DESCENDING

from db import get_manager

client_status_parser = reqparse.RequestParser(bundle_errors=True)
client_status_parser.add_argument("limit",
                                  default=10,
                                  type=int)
client_status_parser.add_argument("start_time",
                                  required=True,
                                  type=int)
client_status_parser.add_argument("end_time",
                                  required=True,
                                  type=int)


class Client(Resource):

    def get(self):
        manager = get_manager()
        return list(manager.get_all_clients(include_id=True))


class ClientStatus(Resource):

    def get(self, client_id):
        """ get recent ClientStatus by client_id"""
        # TODO add parameters for time range
        # TODO convert to start_time, duration format
        manager = get_manager()
        args = client_status_parser.parse_args()
        return list(
            manager.get_client_status_by_id(
                client_id
            ).sort(
                "timestamp", DESCENDING
            ).limit(
                args.limit
            )
        )
