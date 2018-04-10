import requests

# example of payload class

def payload(oldRequest):
    # create new request message
    newRequest = requests.models.Response()

    # set parameters
    newRequest.status_code = 200
    newRequest.headers = r.headers
    newRequest.url = oldRequest.url
    newRequest.history = r.history
    newRequest.encoding = r.encoding
    newRequest.reason = r.reason
    newRequest.elapsed = r.elapsed
    newRequest.request = r.request

    return newRequest