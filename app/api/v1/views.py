from flask import Flask, Blueprint, request, make_response
from flask_api import FlaskAPI
from flask_restful import Api, Resource
from uuid import uuid1

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

orders = {}

class Orders(Resource):
    def get(self):
        return {'message':'get request'}

    def post(self):
        data = request.get_json()
        order_no = int(uuid1())
        orders[order_no] = [data['name'],data['items']]
        return orders, 201
        
        
        
api.add_resource(Orders, '/orders', )



