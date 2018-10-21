import unittest
from app.api import application
import json

class OrdersTestCase(unittest.TestCase):
    """This class represents the orders testcase"""
    def setUp(self):
        """Define test variables"""
        self.app = application
        self.client = self.app.test_client(self)
        self.app.testing = True
        self.order = {"name":"Jay","items":[["coke", 4],["pizza",5]]}



    def test_create_order(self):
        """Test Post request on the api"""
        response = self.client.post('/api/v1/orders', data=json.dumps(self.order),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, b'Order created')
        response =  self.client.post('/api/v1/orders')
        self.assertEqual(response.status, 400)
        self.assertEqual(response.data, b'No data in request')      

    def test_return_list_of_orders(self):
        """Test get all orders request"""
        response = self.client.get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)
        

    def test_get_specific_order(self):
        """Tests if the API can get an order from its id(GET request)"""
        response = self.client.get('/api/v1/orders/b194c012-d399-11e8-a4f6-24fd52059abd')
        data = json.loads(response.data)
        orders = {'order':{'b194c012-d399-11e8-a4f6-24fd52059abd': ['Jay', [['coke', 4], ['pizza', 5]], False]}}
        self.assertEqual(data, orders)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/v1/orders/b194c0d')
        self.assertEqual(json.loads(response.data), {'message': 'No such order'})
        

    def test_edit_order_status(self):
        """Tests if the api can edit the orderstatus(PUT request)"""
        response = self.client.put('/api/v1/orders/b194c012-d399-11e8-a4f6-24fd52059abd')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/v1/orders/b194c0d')
        self.assertEqual(json.loads(response.data), {'message': 'No such order'})
        

if __name__ == '__main__':
    unittest.main()
        
