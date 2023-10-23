import json, requests
from enum import Enum
from lolclient.request import createUrl


#####################################
##                                 ##
##      LOBBY and MATCHMAKING      ##
##                                 ##
#####################################

class Lobby(Enum):
    BLIND = 430
    DRAFT = 400
    RANKED_SOLO = 420
    RANKED_FLEX = 440
    ARAM = 450
    
    TFT_NORMAL = 1090
    TFT_RANKED = 1100
    TFT_DOUBLE = 1160
    TFT_HYPER = 1130
    

def createLobby(reqInfo: dict, lobbyId: Lobby):
    """
    Send a POST request to create a lobby. If already in a lobby, leave and create one.
    
    For the `lobbyId` parameter, refer to the enum class `Lobby`.
    
    Examples:
        `Lobby.BLIND`
        `Lobby.DRAFT`
        `Lobby.RANKED_SOLO`...
    """
    url = createUrl(reqInfo['url'], '/lol-lobby/v2/lobby')
    queue = {"queueId":lobbyId.value}
    requests.post(url, json=queue, headers=reqInfo['header'], verify=False)
    
    
def createLobbyCustom(reqInfo: dict, teamSize: int):
    """
    Send a POST request to create a custom lobby.
    
    Define size of the teams with `teamSize`.
    """
    url = createUrl(reqInfo['url'], '/lol-lobby/v2/lobby')
    if teamSize > 5 or teamSize < 1:
        teamSize = 5
    queue = {
        "customGameLobby": {
            "configuration": {
            "gameMode": "CLASSIC", "gameMutator": "", "gameServerRegion": "", "mapId": 11, "mutators": {"id": 1}, "spectatorPolicy": "AllAllowed", "teamSize": teamSize
            },
            "lobbyName": "Name",
            "lobbyPassword": None
        },
        "isCustom": True
    }
    requests.post(url, json=queue, headers=reqInfo['header'], verify=False)


def getLobbyInfo(reqInfo: dict) -> dict:
    """
    Get some lobby info
    """
    url = createUrl(reqInfo['url'], '/lol-lobby/v2/lobby')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    return json_data


def startMatchmaking(reqInfo: dict):
    """
    Send a POST request to start the matchmaking from a lobby.
    """
    url = createUrl(reqInfo['url'], '/lol-lobby/v2/lobby/matchmaking/search')
    requests.post(url, headers=reqInfo['header'], verify=False)


def matchmakingAccept(reqInfo: dict):
    """
    Send a POST request to accept a match
    """
    url = createUrl(reqInfo['url'], '/lol-matchmaking/v1/ready-check/accept')
    requests.post(url, headers=reqInfo['header'], verify=False)
    
    
def matchmakingDecline(reqInfo: dict):
    """
    Send a POST request to decline a match
    """
    url = createUrl(reqInfo['url'], '/lol-matchmaking/v1/ready-check/decline')
    requests.post(url, headers=reqInfo['header'], verify=False)
    
    
def getGameMode(reqInfo: dict) -> dict:
    """
    Get the current `gamemode`, `category`, `map`, and `phase`. Works both in lobby and champ select.

    Example:
        gamemode:  CLASSIC
        category:  Custom
        map:  Summoner's Rift
        phase:   ChampSelect
        
    Returns `None` if user is not in champ select.
    """
    url = createUrl(reqInfo['url'], '/lol-gameflow/v1/session')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    try:
        result = {
            'gamemode' : json_data['gameData']['queue']['gameMode'],
            'category' : json_data['gameData']['queue']['category'],
            'map' : json_data['map']['gameModeName'],
        }
        return result
    except:
        return None
    
    
def isRanked(reqInfo: dict) -> bool:
    """
    Check if the lobby is ranked.
    
    - Returns `True` or `False`
    """
    url = createUrl(reqInfo['url'], '/lol-gameflow/v1/session')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    try:
        is_ranked = json_data['gameData']['queue']['isRanked']
        return is_ranked
    except:
        return False