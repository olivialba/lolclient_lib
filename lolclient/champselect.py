import json, requests
from lolclient.client import getChampFromId
from lolclient.request import createUrl


#####################################
##                                 ##
##          CHAMP SELECT           ##
##                                 ##
#####################################
    
def getChampSelected(reqInfo: dict) -> dict:
    """
    Get champion selected while in selection.
    
    - Returns the `Champion Dictionary` or `None` if you haven't selected a champion
    """
    url = createUrl(reqInfo['url'], '/lol-champ-select/v1/session/my-selection')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    try:
        champId = json_data['championId']
        if champId == 0:
            return None
        else:
            return getChampFromId(champId)
    except:
        return None