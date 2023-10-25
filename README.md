# lolclient_lib
Basic package to send and receive requests to the League of Legends client.

## Installation
`pip install lolclient-lib`

## How to use
```
from lolclient import *

reqInfo = clientInfo()
```
`clientInfo()` will return the basic url and authorization header needed to send POST and GET requests.
Always put `reqInfo` as the first parameter for every method.

## Example
```
from lolclient import *

reqInfo = clientInfo()
createLobby(reqInfo, Lobby.DRAFT)
startMatchmaking(reqInfo)
```
Automatically creates a normal draft lobby, and starts the matchmaking.

### More examples:

`name = getSummonerName(reqInfo))` >> Return your summoner name

`createLobbyCustom(reqInfo, 5)` >> Creates a custom lobby of team size 5

`createLobby(reqInfo, Lobby.RANKED_SOLO)` >> Creates a ranked solo lobby