from jsonobject import *
from lan_monitor.model.property import ObjectIdProperty
from bson.objectid import ObjectId


class ClientModel(JsonObject):
    mac_addr = StringProperty()
    name = StringProperty(required=False, default="")


class ClientStatusRecordModel(JsonObject):
    client_id = ObjectIdProperty()
    timestamp = DateTimeProperty(exact=True)
    ip_addr = StringProperty()

