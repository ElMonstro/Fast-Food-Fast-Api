from flask import Flask, Blueprint, request, make_response
from flask_api import FlaskAPI
from flask_restful import Api, Resource
from uuid import uuid1

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

orders = {'b194c012-d399-11e8-a4f6-24fd52059abd': ['Jay', [['coke', 4], ['pizza', 5]], False]}

class Orders(Resource):
    def get(self):
        return {'orders': orders}

    def post(self):
        data = request.get_json()
        if data == None:
            return make_response('No Data in request', 400)
        order_no = str(uuid1())
        orders[order_no] = [data['name'],data['items'], False]
        return make_response('Order created', 201)
        
class Order(Resource):
    def get(self, id):
        if str(id) in orders.keys():
            return {'order': orders[id]}
        else:
            return {'message': 'No such order'}
    
    def put(self, id):
        pass

    

        
        
api.add_resource(Orders, '/orders', )
api.add_resource(Order, '/orders/<id>')



