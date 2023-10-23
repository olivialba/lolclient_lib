import requests, json
from lolclient.request import createUrl


#####################################
##                                 ##
##       CLIENT FUNCTIONS          ##
##                                 ##
#####################################

def getSummonerName(reqInfo: dict) -> str:
    """
    Get your summoner's name.
    
    - Returns a string
    """
    url = createUrl(reqInfo['url'], '/lol-summoner/v1/current-summoner')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    return json_data['displayName']


def getGamePhase(reqInfo: dict) -> str:
    """
    Check where you are: lobby, champ select, game, etc...
    
    Can return `Lobby`, `ChampSelect`, `GameStart`, `InProgress`, `WaitingForStats`
    """
    url = createUrl(reqInfo['url'], '/lol-gameflow/v1/gameflow-phase')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    return json_data


def getChampFromId(id: int) -> dict:
    """
    Get champion from its id or key.
    
    - Returns the `Champion Dictionary` or `None` if champion couldn't be found
    """
    if id != 0:
        game_version = (requests.get("https://ddragon.leagueoflegends.com/api/versions.json")).text
        game_version = json.loads(game_version)[0]
        
        data = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{game_version}/data/en_US/champion.json").text
        champions = json.loads(data)['data']
        
        for champ in champions:
            if str(id) == champions[champ]['key']:
                return champions[champ]
        else:
            return None
    

def getChampStats(reqInfo: dict, championId, position, tier, queue) -> dict:
    """
    Get champion stats.
    
    Parameters:
        - championId = integer32
        - position = string, x ∈ { ALL, UNKNOWN, TOP, JUNGLE, MID, BOTTOM, SUPPORT }
        - tier = string, x ∈ { ALL, UNRANKED, IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND, MASTER, GRANDMASTER, CHALLENGER }
        - queue = string, x ∈ { draft5, rank5flex, rank5solo, blind5, aram, blind3, rank3flex, other }
        
    INFO: use `rank5solo` as others may not always work, blame the API.
    """
    url = createUrl(reqInfo['url'], f'/lol-career-stats/v1/champion-averages/{championId}/{position}/{tier}/{queue}')
    response = requests.get(url, headers=reqInfo['header'], verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
