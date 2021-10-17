from flask_restful import Resource, reqparse
from api.db import get_manager
from bson import ObjectId
from pymongo import DESCENDING


class Client(Resource):

    def get(self):
        manager = get_manager()
        return list(manager.get_client({}))


client_status_parser = reqparse.RequestParser()
client_status_parser.add_argument("limit",
                                  default=10,
                                  type=int)
class ClientStatus(Resource):

    def get(self, client_id):
        """ get recent ClientStatus """
        # TODO add parameters for time range
        manager = get_manager()
        args = client_status_parser.parse_args()
        return list(manager.get_client_status({
            "client_id": ObjectId(client_id)
        }).sort("timestamp", DESCENDING).limit(args.limit))
