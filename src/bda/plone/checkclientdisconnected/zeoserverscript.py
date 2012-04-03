import urllib2
import subprocess


class CheckClientDisconnected:  
    def __init__(self, pathtoinstance, url):
        self.pathtoinstance = pathtoinstance
        self.url = url
        
    def __call__(self):
        status = self.status()  
        if status == 0:
            self.restart()
        return status
               
    def status(self):
        try:
            urllib2.urlopen(self.url)
            return 1
            
        except urllib2.HTTPError, e:
            return 0
        
        except urllib2.URLError, e:
            return -1

    def restart(self):
        subprocess.Popen([self.pathtoinstance, "restart"])


