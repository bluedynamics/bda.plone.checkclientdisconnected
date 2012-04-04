import urllib2
import subprocess
from ConfigParser import ConfigParser

class CheckSingleClient:      
    def __init__(self, path, address, quiet=False):
        self.path = path
        self.address = address
        self.quiet = quiet
       
    def __call__(self):
        status = self.status()  
        if status == 0:
            self.restart()
        return status
               
    def status(self):
        try:
            urllib2.urlopen(self.address)
            return 1
            
        except urllib2.HTTPError, e:
            return 0
        
        except urllib2.URLError, e:
            return -1
        
    def restart(self):
        if self.quiet:             
            childprocess = subprocess.Popen([self.path, "restart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         
        else:      
            childprocess = subprocess.Popen([self.path, "restart"])
        childprocess.wait()
          
class CheckMultiClient(object):
    def __init__(self, configfile, quiet=False):
        self.config = ConfigParser()
        self.config.read(configfile)
        self.quiet = quiet
        
    def __call__(self):    
        for path, address in self.config.items("zeo-clients"):
            client = CheckSingleClient(path, address, self.quiet)
            client()

            
                        

             
        