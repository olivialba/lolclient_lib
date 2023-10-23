import requests, json

#####################################
##                                 ##
##            REQUEST              ##
##                                 ##
#####################################

def createUrl(url, endpoint) -> str:
    """
    Creates a new url with an `endpoint` using the base url of the client.
    """
    return url + endpoint


def getRequest(reqInfo: dict, endpoint: str):
    """
    Send a get request at a `endpoint`.
    
    - Returns a request object. 200 for successful requests.
    """    
    url = createUrl(reqInfo['url'], endpoint)
    return requests.get(url, headers=reqInfo['header'], verify=False)


def getRequestJson(reqInfo: dict, endpoint: str):
    """
    Send a get request at a `endpoint` and return the request in the form of a json
    
    - Returns a json text, usually a dictionary
    """    
    return json.loads((getRequest(reqInfo, endpoint)).text)