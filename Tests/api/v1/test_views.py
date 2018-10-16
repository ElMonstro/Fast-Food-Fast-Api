from app.api.v1.views import Order, Orders
import unittest
from app.api import app

class OrdersTestCase(unittest.TestCase):
    """This class represents the orders testcase"""
    def setUp(self):
        """Define test variables"""
        self.app = app
        self.client = self.app.test_client
        self.order = {"name":"Jay","items":[["coke", 4],["pizza",5]]}
        

    def 
        
