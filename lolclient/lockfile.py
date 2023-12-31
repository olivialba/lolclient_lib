import base64, os

#####################################
##                                 ##
##         LOCKFILE INFO           ##
##                                 ##
#####################################

def clientInfo(path: str = 'C:/Riot Games/League of Legends/lockfile') -> dict:
    """
    Get the Lockfile info for requests.
    
    Call readFile() and returns a dictionary with the base `url` and the `header` for making requests.
    
    Returns `None` if file couldn't be found.
    """
    if (os.path.exists(path)):
        return readLockFile(path)
    else:
        return None
    
    
def readLockFile(path: str = 'C:/Riot Games/League of Legends/lockfile') -> dict:
    """
    Return everything from the lockfile. No formatting.
    """
    with open(path, 'r') as lockfile:
        lockfile = lockfile.read()
        data = lockfile.split(':')
        
        auth = 'riot:' + data[3]
        encoded_auth = base64.b64encode(auth.encode('utf-8')).decode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "Authorization": f"Basic {encoded_auth}",
        }
        
        reqInfo = {
            'url': "https://127.0.0.1:" + data[2],
            'header': headers,
            'port': data[2],
            'encoded_auth': encoded_auth
        }
    
        return reqInfo