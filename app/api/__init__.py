from flask import Flask
from app.api.v1.views import v1, api
import os
import sys

file_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(file_dir)

application = Flask(__name__)
application.register_blueprint(v1)
