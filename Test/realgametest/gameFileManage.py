from requests import get, put
import datetime

# it's not related recent test server

def save(mapID, playerID, mapData, mapName):
    playerCount = 0
    starCount = 0

    for currentList in mapData:
        for block in currentList:
            if block == 'p':
                playerCount += 1
            elif block == 's':
                starCount += 1

    print(playerCount, starCount)

    if playerCount != 1: return
    if starCount == 0: return

    TimeUpload = datetime.datetime.now()
    put("http://127.0.0.1:5000/upload", data={'mapID': mapID, 'playerID': playerID, 'TimeUpload': str(TimeUpload), 'mapData': mapData, 'mapName': mapName})