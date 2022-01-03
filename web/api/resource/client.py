from flask_restful import Resource, reqparse
import pymongo

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
client_status_parser.add_argument("interval",
                                  default=60,
                                  type=int)


class Client(Resource):

    def get(self):
        manager = get_manager()
        return list(manager.get_all_clients(include_id=True))


class ClientStatus(Resource):

    def get(self, client_id):
        """ get recent ClientStatus by client_id"""
        # TODO convert to start_time, duration format
        manager = get_manager()
        args = client_status_parser.parse_args()
        res = list(
            manager.get_client_status_by_time_range(
                client_id, args.start_time, args.end_time
            ).sort(
                "timestamp", pymongo.ASCENDING
            ).limit(
                args.limit
            )
        )

        if len(res) == 0:
            return []

        prev_time = res[0]["timestamp"]
        result = []
        duration = 0
        start = res[0]["timestamp"]
        for status in res[1:]:
            if status["timestamp"] - prev_time <= args.interval:
                duration += status["timestamp"] - prev_time
            else:
                result.append({
                    "start": start,
                    "duration": max(5, duration)
                })
                start = status["timestamp"]
                duration = 0

            prev_time = status["timestamp"]

        result.append({
            "start": start,
            "duration": max(5, duration)
        })
        return result
