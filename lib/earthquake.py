import datetime, time
import json

class Earthquake:
    items = []
    def __init__(self, service=''):
        if len(service) <= 0:
            self.__manager = Manager()
        else:
            self.__manager = Manager(service=service)
    def __call__(*args, **kwargs):
        totArgs = len(args) + len(kwargs.keys())
        assert totArgs <= 1, "The constructor accept at most one parameter('service')"
    def refresh(self, format="json"):
        response =  self.__manager.request()
        itemCollection = []
        for elem in response:
            newItem = EarthquakeItem(**elem)
            newItem.setDate(elem['datetime'])
            if(format == "json"): #to be refactored
                itemCollection.append(newItem.__dict__)
            else:
                itemCollection.append(newItem)
        if (format == "json"):
           return json.dumps(itemCollection) 
        return itemCollection

class EarthquakeItem:
    
    def __init__(self, **kwargs):
        self.src = "src" # Source
        self.eqid = -1 # ID
        self.version = -1
        self.itemDatetime = datetime.datetime.now()
        self.lat = 0.0
        self.lon = 0.0
        self.magnitude = 0.0
        self.depth = 0.0 # in Km
        self.nst = 0 # Number of reporting stations
        self.region = ""
        args = [(key, value)for (key, value) in kwargs.items() if type(self.__dict__.get(key)) != type(None)]#filter the args in input.    
        for k, v in args:    
            self.__dict__[k] = v
    
    def setDate(self, dt, expectedFormat="%A, %B %d, %Y %H:%M:%S UTC"):
        if(isinstance(dt, type(''))):
            self.itemDatetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(dt, expectedFormat))).isoformat() 
        elif(isinstance(dt, datatime)):
            self.itemDatetime = dt.isoformat()
class Manager:
    proxyService = None
    parser = None 
    def __init__(self, **kwargs):
        self.__service = "console"     
        self.proxyService = Proxy()
        assert len(kwargs.keys()) <= 1, "The Manager expects maximum one paramenter in its constructor (service)"
        if(len(kwargs.keys()) == 1):
            assert kwargs.get("service"), "Service is the only accepted key in input"
            self.__service = kwargs.get("service")
            if self.__service == "fake":
                self.proxyService = FakeProxy()
                
        self.parser = Parser()
    def request(self):
        response = self.proxyService.makeRequest()
        result = self.parser.parse(response)
        return result

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
            temp = []
            [temp.append(row) for row in reader if len(row) == EXPECTED_FIELDS_NUMBER]
            for row in temp:    
                result.append(dict((k.lower(),v) for k,v in row.iteritems()))            
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
        
