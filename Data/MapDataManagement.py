import string, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Internet import *


mapID = ["mapID", 0]
playerID = ["playerID", 1]
TimeUpload = ["TimeUpload", 2]
mapName = ["mapName", 3]
mapData = ["mapData", 4]


def getListViewDataFormat(mapID_p, playerID_p, TimeUpload_p, mapName_p):
    return "mapID: %s\n" \
           "playerID: %s\n" \
           "TimeUpload: %s\n" \
           "mapName: %s" \
           % (mapID_p, playerID_p, TimeUpload_p, mapName_p)


def getListViewData(data, dataEnum) -> str:
    data = data.split('\n')[dataEnum[1]]  # select line
    data = data.split(':')[1][1:]
    return data

def genKey(_len=20):
    ret = ""
    string_pool = string.ascii_letters + string.digits
    for i in range(_len):
        ret += random.choice(string_pool)
    return ret

def getKeyData(key, player_id = None):
    if getDataServerOnline():
        url = "http://" + DATA_SERVER_IP + "/" + key
        if player_id == None:
            data = put(url).json()
        else:
            data = put(url, data={playerID[0]: player_id}).json()
        return data
    return None

def convert_mapID_to_mapData(mapID):
    if getDataServerOnline():
        url = "http://" + DATA_SERVER_IP + "/" + mapID
        data = get(url).json()
        return data
    return None

def upload(upload_data):
    if getDataServerOnline():
        url = "http://" + DATA_SERVER_IP + "/upload"
        put(url, data=upload_data)

def getSortedMapList(key, player_id = None):
    if getDataServerOnline():
        return getKeyData(str(key).replace(' ', ''), player_id)
    return None

def convert_toModel(map_data):
    # covert model
    model_data = []
    for map in map_data:
        format = convert_MaptoString(map)
        model_data += [format]
    return QStringListModel(model_data)


def convert_MaptoString(map):
    return getListViewDataFormat(mapID_p=map[mapID[0]],
                                   playerID_p=map[playerID[0]],
                                   TimeUpload_p=map[TimeUpload[0]],
                                   mapName_p=map[mapName[0]]
                                   )

if __name__ == "__main__":
    data = getListViewDataFormat("A", "B", "C", "D")
    print(getListViewData(data, mapName))