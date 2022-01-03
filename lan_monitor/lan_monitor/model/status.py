from jsonobject import *
from lan_monitor.model.property import ObjectIdProperty


class ClientModel(JsonObject):
    mac_addr = StringProperty()
    ip_addr = StringProperty()
    name = StringProperty(required=False, default="")


class ClientStatusRecordModel(JsonObject):
    client_id = ObjectIdProperty()
    timestamp = FloatProperty()

