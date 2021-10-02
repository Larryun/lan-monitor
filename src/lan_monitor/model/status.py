from jsonobject import *


class ClientModel(JsonObject):
    mac_addr = StringProperty()
    name = StringProperty(required=False, default="")


class ClientStatusRecordModel(JsonObject):
    client_id = StringProperty()
    timestamp = DateTimeProperty(exact=True)
    ip_addr = StringProperty()
