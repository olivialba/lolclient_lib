import requests, json, base64, os

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


def readLockFile(path) -> dict:
    """
    Read Lockfile info.
    
    Returns a dictionary with the base `url` and the `header` for making requests
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
        
        url = "https://127.0.0.1:" + data[2]
        header = headers
        
        reqInfo = {
            'url': url,
            'header': headers
        }
    
        return reqInfo


def newUrl(url, endpoint):
    """
    Creates a new url with an `endpoint` using the base url.
    """
    return url + endpoint


def getSummonerName(reqInfo: dict) -> str:
    """
    Get your summoner's name.
    
    - Returns a string
    """
    url = newUrl(reqInfo['url'], '/lol-summoner/v1/current-summoner')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    return json_data['displayName']


def getGamePhase(reqInfo: dict) -> str:
    """
    Check where you are: lobby, champ select, game, etc...
    
    Can return `Lobby`, `ChampSelect`, `GameStart`, `InProgress`, `WaitingForStats`
    """
    url = newUrl(reqInfo['url'], '/lol-gameflow/v1/gameflow-phase')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    return json_data


def getChampSelected(reqInfo: dict) -> dict:
    """
    Get champion selected while in selection.
    
    - Returns the `Champion Dictionary` or `None` if you haven't selected a champion
    """
    url = newUrl(reqInfo['url'], '/lol-champ-select/v1/session/my-selection')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    try:
        champId = json_data['championId']
        if champId == 0:
            return None
        else:
            return getChampFromId(champId)
    except:
        return None


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


def getGameMode(reqInfo: dict) -> dict:
    """
    Get the `gamemode`, `category`, `map`, and `phase`  from champ select.

    Example:
        gamemode:  CLASSIC
        category:  Custom
        map:  Summoner's Rift
        phase:   ChampSelect
        
    Returns `None` if user is not in champ select.
    """
    url = newUrl(reqInfo['url'], '/lol-gameflow/v1/session')
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
    url = newUrl(reqInfo['url'], '/lol-gameflow/v1/session')
    json_data = json.loads((requests.get(url, headers=reqInfo['header'], verify=False)).text)
    try:
        is_ranked = json_data['gameData']['queue']['isRanked']
        return is_ranked
    except:
        return False
    

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
    url = newUrl(reqInfo['url'], f'/lol-career-stats/v1/champion-averages/{championId}/{position}/{tier}/{queue}')
    response = requests.get(url, headers=reqInfo['header'], verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None