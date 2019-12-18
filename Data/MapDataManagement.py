import string, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Internet import *


mapID = ["mapID", 0]
playerID = ["playerID", 1]
TimeUpload = ["TimeUpload", 2]
mapName = ["mapName", 3]


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

def getKeyData(key):
    if getDataServerOnline():
        url = "http://" + DATA_SERVER_IP + "/" + key
        data = put(url).json()
        return data
    return None

def convert_mapID_to_mapData(mapID):
    if getDataServerOnline():
        url = "http://" + DATA_SERVER_IP + "/" + mapID
        data = get(url).json()
        return data
    return None

def getSortedMapList(key):
    if getDataServerOnline():
        return getKeyData(str(key).replace(' ', ''))
    return None

def convert_toModel(map_data):
    # covert model
    model_data = []
    for map in map_data:
        format = getListViewDataFormat(mapID_p=map[mapID[0]],
                                            playerID_p=map[playerID[0]],
                                            TimeUpload_p=map[TimeUpload[0]],
                                            mapName_p=map[mapName[0]]
                                            )
        model_data += [format]
    return QStringListModel(model_data)

if __name__ == "__main__":
    data = getListViewDataFormat("A", "B", "C", "D")
    print(getListViewData(data, mapName))