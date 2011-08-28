import datetime
class Earthquake:
    items = []
    def refresh(self):
        return True

class EarthquakeItem:
    
    def __init__(self, **kwargs):
        self.src = "src" # Source
        self.equid = -1 # ID
        self.version = -1
        self.itemDatetime = datetime.datetime.now()
        self.lat = 0.0
        self.lon = 0.0
        self.magnitude = 0.0
        self.depth = 0.0 # in Km
        self.nst = 0 # Number of reporting stations
        self.region = ""
        args = [(key, value)for (key, value) in kwargs.items() if self.__dict__.get(key)]#filter the args in input.    
        for k, v in args:    
            self.__dict__[k] = v

class Manager:
    proxyService = None
    parser = None 
    def __init__(self, **kwargs):
        self.__service = "console"
        assert len(kwargs.keys()) <= 1, "The Manager expects maximum one paramenter in its constructor (service)"
        if(len(kwargs.keys()) == 1):
            assert kwargs.get("service"), "Service is the only accepted key in input"
            self.__service = kwargs.get("service")
            self.proxyService = Proxy()
    def request(self):
        res = self.proxyService.makeRequest()
        raise Exception("Not implemented yet!")

class Proxy:
    __addressEndpoint = "http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt"
    def makeRequest(self):
        import urllib2
        request = urllib2.urlopen(self._Proxy__addressEndpoint)
        return request.read() 

class FakeProxy(Proxy):
    """
    Fake proxy used for unit tests
    """
    def makeRequest(self):
       return ''

class Parser:
    def parse(self, inputToParse):
        assert type(inputToParse) == type(''), "The input must be a string"
        import csv, datetime
        result = []
        filename = "earthquake_%s.ea.tmp" % (datetime.datetime.now().isoformat(),)
        try:
            fp = open(filename, "w")
            fp.write(inputToParse)
        finally:
            fp.close()
        try:
            fp = open(filename, "rt")
            reader = csv.DictReader(open(filename, "rt"))
            EXPECTED_FIELDS_NUMBER = 10
            [result.append(row) for row in reader if len(row) == EXPECTED_FIELDS_NUMBER]
        finally:
            fp.close();
            import os, glob
            filesToDelete = glob.glob(filename)
            for fileToDelete in filesToDelete:
                try:
                    os.remove(fileToDelete)
                except Exception:
                    raise 
            
        return result
        
