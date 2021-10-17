from flask import Flask
from flask_restful import Api
from os import environ
from lan_monitor.util import read_yaml
from api.db import close_manager
from resource import client
import json
from bson import ObjectId

class CustomJSONEncoder(json.JSONEncoder):
    """ Customized JsonEncoder for deserializing ObjectId """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
api = Api(app)

# set configurations
if "FLASK_ENV" not in environ:
    raise RuntimeError("FLASK_ENV is not set")
elif environ["FLASK_ENV"] == "dev":
    config = read_yaml("api/instance/api.config.dev.yaml")
elif environ["FLASK_ENV"] == "test":
    config = read_yaml("api/instance/api.config.test.yaml")
else:
    raise RuntimeError("FLASK_ENV is not dev/test")

app.config.update(config)
# set default JSONEncoder to CustomJSONEncoder
app.config.setdefault("RESTFUL_JSON", {})["cls"] = CustomJSONEncoder

# add callback for closing connection to db on request end
app.teardown_appcontext(close_manager)

# add resource
api.add_resource(client.Client, "/client")
api.add_resource(client.ClientStatus, "/client/status/<string:client_id>")

if __name__ == "__main__":
    app.run(debug=True)

