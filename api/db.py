from flask import g, current_app
from flask.cli import with_appcontext
from lan_monitor.manager import client
from lan_monitor.util import create_mongo_client

def get_manager():
    if "manager" not in g:
        mongo_config = current_app.config["mongodb"]

        mc = create_mongo_client(
            mongo_config["host"], mongo_config["port"],
            mongo_config["username"], mongo_config["password"]
        )

        g.manager = client.ClientManager(mc, current_app.config)
    
    return g.manager


def close_manager(e=None):
    manager = g.pop("manager", None)

    if manager is not None:
        manager.close_mongo_client()
