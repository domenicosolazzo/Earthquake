import unittest
from lib.earthquake import Earthquake
class EarthquakeTestCase(unittest.TestCase):
    def setUp(self):
        self.earthquake = Earthquake(service="fake")
    def test_refresh_exists(self):
        self.assertTrue(callable(getattr(self.earthquake,"refresh")),"True")
    def test_refresh_does_take_at_most_one_parameter(self):
        self.assertRaises(TypeError, getattr(self.earthquake, "refresh"), *("json",2),**{})
    def test_refresh_returns_a_list(self):
        self.assertTrue(type(self.earthquake.refresh("list")) == type([]),"Refresh returns a list")
    def test_earthquake_has_an_items_attribute(self):
        self.assertFalse(callable(getattr(self.earthquake,"items")), "The object has an items attribute.")
    def test_items_attribute_is_a_list(self):
        self.assertTrue(type(self.earthquake.items) == type([]), "The items attribute is a list") 
    def test_earthquake_contains_a_manager_attribute(self):
        self.assertFalse(callable(getattr(self.earthquake,"_Earthquake__manager")),"Earthquake has a manager attribute")
    def test_earthquake_accepts_zero_or_one_paramenter_in_input(self):
        self.assertRaises(AssertionError, self.earthquake, **{"service":"fake", "notvalid":"notvalid"})
        self.assertRaises(AssertionError, self.earthquake, *["fake"],**{"service":"lalala"})
        
        self.assertFalse(callable(getattr(self.earthquake,"_Earthquake__manager")),"Earthquake has a manager attribute")
