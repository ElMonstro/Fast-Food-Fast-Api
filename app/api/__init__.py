from flask import Flask
from app.api.v1.views import v1, api
from instance.config import Configuration


application = Flask(__name__, instance_relative_config=True)
application.config.from_object(Configuration)
application.config.from_pyfile('config.py')
application.register_blueprint(v1)
