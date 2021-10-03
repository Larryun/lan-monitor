from jsonobject import JsonProperty
from bson.objectid import ObjectId

class ObjectIdProperty(JsonProperty):
    def wrap(self, obj):
        return ObjectId(obj)

    def unwrap(self, obj): 
        return obj, obj