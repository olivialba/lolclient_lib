import os, requests, json

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


def certSSL():
    '''
    The LCU API uses a self signed certificate. This will return the path of the certificate given by the LCU API.
    Certificate can be found on the LCU API faq page: https://hextechdocs.dev/lcu-api-faq/
    '''
    current_module_directory = os.path.dirname(__file__)
    return os.path.join(current_module_directory, 'riotgames.pem')