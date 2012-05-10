import argparse
from api import CheckMultiClient



parser = argparse.ArgumentParser(description="this script will check and, restart \
zeo-clients configured in the clientlist")

parser.add_argument('--quiet', '-q', action="store_true", default=False,
                   help='suppresses every output of the script')

parser.add_argument('--status', '-s', action="store_true", default=False,
                   help='prints the status of the zeo-client')

parser.add_argument('configfile', nargs=1,
                   help='path to configuration file')


def run():
    ns = parser.parse_args()
    
    client = CheckMultiClient(ns.configfile[0],ns.quiet)
    client()

