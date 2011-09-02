import unittest
from lib.earthquake import EarthquakeItem

class EarthquakeItemTestCase(unittest.TestCase):
    def setUp(self):
        self.item = EarthquakeItem()
    def test_item_contains_a_src_attribute(self):
        self.assertFalse(callable(getattr(self.item, "src")), "The EarthquakeItem contains a src attribute")
    def test_src_attribute_is_a_string(self):
        self.assertTrue(type(self.item.src) == type(''), "The src attribute is a string")
    def test_item_contains_a_equid_attribute(self):
        self.assertFalse(callable(getattr(self.item, "eqid")), "The EarthquakeItem contains a equid attribute")
    def test_equid_attribute_is_an_integer(self):
        self.assertTrue(type(self.item.eqid) == type(1), "The equid attribute is an integer")
    def test_item_contains_a_version_attribute(self):
        self.assertFalse(callable(getattr(self.item, "version")), "The EarthquakeItem contains a version attribute")
    def test_version_attribute_is_an_integer(self):
        self.assertTrue(type(self.item.version) == type(1), "The version attribute is an integer")
    def test_item_contains_a_itemDatetime_attribute(self):
        self.assertFalse(callable(getattr(self.item, "itemDatetime")), "The EarthquakeItem contains a itemDatetime attribute")
    def test_itemDatetime_attribute_is_a_datetime(self):
        import datetime
        self.assertTrue(type(self.item.itemDatetime) == type(datetime.datetime.now()), "The src attribute is a string")
    def test_item_contains_a_lat_attribute(self):
        self.assertFalse(callable(getattr(self.item, "lat")), "The EarthquakeItem contains a lat attribute")
    def test_lat_attribute_is_a_float(self):
        self.assertTrue(type(self.item.lat) == type(1.0), "The lat attribute is a float")
    def test_item_contains_a_lon_attribute(self):
        self.assertFalse(callable(getattr(self.item, "lon")), "The EarthquakeItem contains a lon attribute")
    def test_lon_attribute_is_a_float(self):
        self.assertTrue(type(self.item.lon) == type(1.0), "The lon attribute is a float")
    def test_item_contains_a_magnitude_attribute(self):
        self.assertFalse(callable(getattr(self.item, "magnitude")), "The EarthquakeItem contains a magnitude attribute")
    def test_magnitude_attribute_is_a_float(self):
        self.assertTrue(type(self.item.magnitude) == type(1.0), "The magnitude attribute is a float")
    def test_item_contains_a_depth_attribute(self):
        self.assertFalse(callable(getattr(self.item, "depth")), "The EarthquakeItem contains a depth attribute")
    def test_depth_attribute_is_a_float(self):
        self.assertTrue(type(self.item.depth) == type(1.0), "The depth attribute is a float")
    def test_item_contains_a_nst_attribute(self):
        self.assertFalse(callable(getattr(self.item, "nst")), "The EarthquakeItem contains a nst attribute")
    def test_nst_attribute_is_an_integer(self):
        self.assertTrue(type(self.item.nst) == type(1), "The nst attribute is an integer")
    def test_item_contains_a_region_attribute(self):
        self.assertFalse(callable(getattr(self.item, "region")), "The EarthquakeItem contains a region attribute")
    def test_lat_attribute_is_a_string(self):
        self.assertTrue(type(self.item.region) == type(''), "The region attribute is a string")
    def test_item_constructor(self):
        import datetime
        values = dict(src="ci", equid=1, version=1, itemDatetime=datetime.datetime.now, lat=100.23, lon=22.222, magnitude=5.0, depth=1.2, nst=22, region="test valley")
        newItem = EarthquakeItem(**values)
        self.assertEqual("ci" , newItem.src, "The constructor works fine.")  
    
    def test_item_contains_setDate_method(self):
        self.assertTrue(callable(getattr(self.item,"setDate")),"The item contains a setDateMethod") 
