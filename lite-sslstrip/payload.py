"""
Example of a payload module, implements one function payload(response) which delivers a response
Imagination is the only limit.
"""

import requests

def payload(oldResponse):
    # create new request message
    newResponse = requests.models.Response()

    # set parameters
    newResponse.status_code = 200
    newResponse.headers = r.headers
    newResponse.url = oldResponse.url
    newResponse.history = r.history
    newResponse.encoding = r.encoding
    newResponse.reason = r.reason
    newResponse.elapsed = r.elapsed
    newResponse.request = r.request

    return newResponse