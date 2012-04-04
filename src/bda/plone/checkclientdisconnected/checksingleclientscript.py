import argparse
from api import CheckSingleClient

parser = argparse.ArgumentParser(description='this script will check and, restart a single zeo-client')

parser.add_argument('--quiet', '-q', action="store_true", default=False,
                   help='suppresses every output of the script')

parser.add_argument('--status', '-s', action="store_true", default=False,
                   help='prints the status of the zeo-client')

parser.add_argument('path', nargs=1,
                   help='enter the path to your instance\n'
                        'example: example/bin/instance')

parser.add_argument('address', nargs=1,
                   help='enter the url and the port\n'
                        'example: http://127.0.0.1:8080/site')

def run():
    ns = parser.parse_args()
  
    client = CheckSingleClient(ns.path[0], ns.address[0], ns.quiet)
    
    if ns.status:
        print client.status()
    else:
        client()
