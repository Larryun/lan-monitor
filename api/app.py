from flask import Flask
from flask_restful import Api
from os import environ
from lan_monitor.util import read_yaml
from api.db import close_manager


app = Flask(__name__)
api = Api(app)

if environ["FLASK_ENV"] == "dev":
    config = read_yaml("api/instance/api.config.dev.yaml")
elif environ["FLASK_ENV"] == "test":
    config = read_yaml("api/instance/api.config.test.yaml")

app.config.update(config)

app.teardown_appcontext(close_manager)

if __name__ == "__main__":
    app.run(debug=True)

