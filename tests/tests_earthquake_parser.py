import unittest
from lib.earthquake import Parser

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
    def test_parser_contains_a_parse_method(self):
        self.assertTrue(callable(getattr(self.parser, "parse")), "Parser contains a parse method")
    def test_parse_method_accepts_a_string_in_input(self):
        self.assertRaises(AssertionError, getattr(self.parser, "parse"), **{"inputToParse":1}) 
    def test_parse_method_returns_a_list(self):
        self.assertEqual(type(self.parser.parse('')), type([]), "Parse returns a list")
