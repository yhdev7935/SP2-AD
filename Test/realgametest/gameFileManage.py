from requests import get, put
import datetime

# it's not related recent test server

def save(mapName, mapID, playerID, mapList):
    playerCount = 0
    starCount = 0

    for currentList in mapList:
        if 'p' in currentList:
            playerCount += 1
        elif 's' in currentList:
            starCount += 1

    if playerCount != 1: return
    if starCount == 0: return

    timeUpload = datetime.datetime.now()
    put("http://127.0.0.1:5000/upload", data={'mapName': mapName, 'mapID': mapID, 'playerID': playerID, 'timeUpload': timeUpload, 'mapList': mapList})