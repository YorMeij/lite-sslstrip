## Execution of an SSL-strip
## first sets up a CherryPy Server to handle Alice requests
## Communicates with Bob through XXX package

import cherrypy
import random
import string

## Example of usage: a random string generator see: http://docs.cherrypy.org/en/latest/tutorials.html#tutorial-3-my-urls-have-parameters

# Class object to provide functionality for CherryPy server
@cherrypy.expose    # <-- decorator, you can ignore this
class StringGenerator(object):
    # function names map to the page that they generate
    # this will map to /index and will show the string "Hello world!"
    def index(self):
        return "Hello world!"

    # this will map to /generate
    # function arguments:
        # self: which is this class so you can call this function later on
        # anything else will be accessble use a http-parameter, in this case /generate?length=some_number
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

## TODO: relay the incoming connection from Alice to Bob
    def relay(self):
        return ""

# starting the server
if __name__ == '__main__':
    # this command binds cherrypy to all interfaces of this machine, hence it is findable on the network
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # this command actually starts the server
    cherrypy.quickstart(StringGenerator())