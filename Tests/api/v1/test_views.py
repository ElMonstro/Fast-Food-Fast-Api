import unittest
from app.api import app

class OrdersTestCase(unittest.TestCase):
    """This class represents the orders testcase"""
    def setUp(self):
        """Define test variables"""
        self.app = app
        self.client = self.app.test_client
        self.order = {"name":"Jay","items":[["coke", 4],["pizza",5]]}


    def test_create_order(self):
        """Test Post request on the api"""
        response = self.client().post('/orders', data=self.order)
        self.assertEqual(response.status_code, 201)        

    def test_return_list_of_orders(self):
        """Test get all orders request"""
        pass

    def test_get_specific_order(self):
        """Tests if the API can get an order from its id(GET request)"""
        pass

    def test_edit_order_status(self):
        """Tests if the api can edit the orderstatus(PUT request)"""
        pass

        
