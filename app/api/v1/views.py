from flask import Flask, Blueprint, request, make_response
from flask_api import FlaskAPI
from flask_restful import Api, Resource
from uuid import uuid1

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

orders = {}

class Orders(Resource):
    def get(self):
        return {'orders': orders}

    def post(self):
        data = request.get_json()
        order_no = str(uuid1())
        orders[order_no] = [data['name'],data['items'], False]
        return orders, 201
        
class Order(Resource):
    def get(self, id):
        if str(id) in orders.keys():
            return {'order': orders[id]}
        else:
            return {'message': list(orders.keys())}

        
        
api.add_resource(Orders, '/orders', )
api.add_resource(Order, '/orders/<id>')



