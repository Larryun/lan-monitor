import argparse
from lan_monitor.monitor import Monitor
from lan_monitor.manager.client import ClientManager
from lan_monitor.util import create_mongo_client, read_yaml
from lan_monitor.model.status import ClientStatusRecordModel, ClientModel
import time
from pprint import pprint
import ipaddress
import logging

logging.basicConfig()
_LOGGER = logging.getLogger("root")


def update_status(client_manager, monitor, sample):
    clients_info = monitor.get_clients(sample=sample)
    _LOGGER.debug("Found " + str(len(clients_info)) + " clients")
    _LOGGER.debug(clients_info)

    now = time.time()

    for cli_info in clients_info:
        # create client if not exsits
        if not client_manager.has_client({"mac_addr": cli_info["mac"]}):
            client_manager.insert_client(ClientModel({
                "ip_addr": cli_info["src_ip"],
                "mac_addr": cli_info["mac"],
                "name": ""
            }))

        # get client_id
        res = client_manager.get_client({"mac_addr": cli_info["mac"]}, include_id=True)[0]
        # insert client status
        client_manager.insert_client_status(ClientStatusRecordModel({
            "client_id": res["_id"],
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

    parser.add_argument("-d", "--debug",
                        help="debug",
                        default=False,
                        action="store_true",
                        dest="debug")

    args = parser.parse_args()

    if args.debug:

        _LOGGER.setLevel(logging.DEBUG)


    _LOGGER.info("Starting lan-monitor")


    config = read_yaml(args.config_path)
    mongo_config = config["mongodb"]

    mc = create_mongo_client(
        mongo_config["host"], mongo_config["port"],
        mongo_config["username"], mongo_config["password"]
    )

    manager = ClientManager(mc, config)
    monitor = Monitor(ipaddress.IPv4Network("10.0.0.0/24"))

    while True:
        update_status(manager, monitor, args.sample)
        time.sleep(args.interval)




if __name__ == "__main__":
    main()
