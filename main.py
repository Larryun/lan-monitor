import argparse
import lan_monitor
from lan_monitor.monitor import Monitor
from lan_monitor.manager.client import ClientManager
from lan_monitor.util import create_mongo_client, read_yaml
from lan_monitor.model.status import ClientStatusRecordModel, ClientModel
from pymongo import MongoClient
import time
import datetime
from bson.objectid import ObjectId


def update_status(client_manager, monitor, sample):
    clients_info = monitor.get_clients(sample=sample)
    print(len(clients_info))

    now = datetime.datetime.utcnow()

    for cli_info in clients_info:
        # create client if not exsits
        if not client_manager.has_client({"mac_addr": cli_info["mac"]}):
            client_manager.insert_client(ClientModel({
                "mac_addr": cli_info["mac"],
                "name": ""
            }))

        # get client_id
        res = client_manager.get_client({"mac_addr": cli_info["mac"]})[0]
        # insert client status
        client_manager.insert_client_status(ClientStatusRecordModel({
            "client_id": res["_id"],
            "ip_addr": cli_info["src_ip"],
        }, timestamp=now))


def main():
    parser = argparse.ArgumentParser("LAN Monitor")
    parser.add_argument("-c", "--config",
                        help="path to config.yaml",
                        required=True,
                        dest="config_path")

    parser.add_argument("-i", "--interval",
                        help="update interval (s)",
                        required=True,
                        type=int,
                        dest="interval")

    parser.add_argument("-s", "--sample",
                        help="number of sample in each update",
                        default=1,
                        type=int,
                        dest="sample")

    args = parser.parse_args()

    config = read_yaml(args.config_path)
    mongo_config = config["mongodb"]

    mc = create_mongo_client(
        mongo_config["host"], mongo_config["port"],
        mongo_config["username"], mongo_config["password"]
    )

    manager = ClientManager(mc, config)
    monitor = Monitor("10.0.0.0/24")

    while True:
        update_status(manager, monitor, args.sample)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
