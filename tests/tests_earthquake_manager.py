import unittest
from lib.earthquake import Manager, Proxy, Parser

class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()
    def test_manager_accepts_zero_or_1_element(self):
        self.assertRaises(AssertionError, Manager, **{"service":"gae","notvalid":"notvalid"})
    def test_manager_throws_an_exception_when_paramenter_is_not_equals_to_service(self):
        self.assertRaises(AssertionError, Manager, **{"notvalid":"gae"})
    def test_manager_contains_a_request_method(self):
        self.assertTrue(callable(getattr(self.manager, "request")),"The manager contains a request method")
    def test_request_method_returns_array(self):
        self.assertEqual(type(self.manager.request()), type([]), "Request returns an array")
    def test_manager_contains_a_proxyService_attribute(self):
        self.assertFalse(callable(getattr(self.manager, "proxyService")), "The manager contains a proxyService attribute")
    def test_proxyService_is_instance_of_Proxy(self):
        self.assertIsInstance(getattr(self.manager, "proxyService"),Proxy, "The proxyService attribute is instance of Proxy")
    def test_manager_contains_a_parser_attribute(self):
        self.assertFalse(callable(getattr(self.manager, "parser")), "The manager contains a parser attribute")
    def test_parser_is_instance_of_Parser(self):
        self.assertIsInstance(getattr(self.manager, "parser"), Parser, "The parser attribute is instance of Parser")
    def test_manager_contains_a_service_attribute(self):
        self.assertFalse(callable(getattr(self.manager, "_Manager__service")), "The manager contains a server attribute")
    def test_service_is_a_string(self):
        self.assertEqual(type(getattr(self.manager, "_Manager__service")),type(''), "The service attribute is a string")
