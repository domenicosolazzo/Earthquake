import unittest
from lib.earthquake import Proxy, FakeProxy

class ProxyTestCase(unittest.TestCase):
    def setUp(self):
        self.proxy = Proxy()
    def test_Proxy_contains_a_makeRequest_method(self):
        self.assertTrue(callable(getattr(self.proxy, "makeRequest")), "Proxy contains a makeRequest method")
    def test_Proxy_contains_a_addressEndpoint_attribute(self):
        self.assertFalse(callable(getattr(self.proxy, "_Proxy__addressEndpoint")), "Proxy contains a addressEndpoint attribute")
    def test_addressPoint_value(self):
        self.assertEqual(self.proxy._Proxy__addressEndpoint, "http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt","The address value is correct.")
    def test_makeRequest_returns_a_string(self):
        proxy = FakeProxy()
        self.assertEqual(type(proxy.makeRequest()), type(''), "makeRequest returns a string")
