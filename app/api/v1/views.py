from flask import Flask, Blueprint
from flask_api import FlaskAPI
from flask_restful import Api, Resource

v1 = Blueprint('v1', __name__, url_prefix='/api/v1/')
api = Api(v1)

class Orders(Resource):
    def get(self):
        return {'message':'get request'}

    def post(self):
        pass
        

api.add_resource(Orders, '/orders')



