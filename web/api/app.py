import json
from bson import ObjectId
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from os import environ

from lan_monitor.util import read_yaml
from resource import client
from db import close_manager

class CustomJSONEncoder(json.JSONEncoder):
    """ Customized JsonEncoder for deserializing ObjectId """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
api = Api(app, prefix="/api")

CORS(app, resources={r'/*': {"origins": "*"}})

# set configurations
if "FLASK_ENV" not in environ:
    raise RuntimeError("FLASK_ENV is not set")
elif environ["FLASK_ENV"] in ["dev", "test", "prod"]:
    config = read_yaml(f"./instance/api.config.{environ['FLASK_ENV']}.yaml")
else:
    raise RuntimeError("FLASK_ENV is not valid")
app.config.update(config)

# set default JSONEncoder to CustomJSONEncoder
app.config.setdefault("RESTFUL_JSON", {})["cls"] = CustomJSONEncoder

# add callback for closing connection to db on request end
app.teardown_appcontext(close_manager)

# add resource
api.add_resource(client.Client, "/client")
api.add_resource(client.ClientStatus, "/client/status/<string:client_id>")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
