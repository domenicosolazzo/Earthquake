import unittest
from lib.earthquake import Earthquake
class EarthquakeTestCase(unittest.TestCase):
    def setUp(self):
        self.earthquake = Earthquake()
    def test_refresh_exists(self):
        self.assertTrue(callable(getattr(self.earthquake,"refresh")),"True")
    def test_refresh_does_take_any_parameter(self):
        self.assertRaises(TypeError, getattr(self.earthquake, "refresh"), *(1,),**{})
    def test_refresh_returns_a_boolean(self):
        self.assertTrue(type(self.earthquake.refresh()) == type(True),"Refresh returns a boolean")
    def test_earthquake_has_an_items_attribute(self):
        self.assertFalse(callable(getattr(self.earthquake,"items")), "The object has an items attribute.")
    def test_items_attribute_is_a_list(self):
        self.assertTrue(type(self.earthquake.items) == type([]), "The items attribute is a list") 
