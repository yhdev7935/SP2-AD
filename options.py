import os

# GAME OPTIONS

GAME_SIZE = [500, 500]
GAME_TITLE = "Finding Star"
SIZE = 20

blockList = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    's': 's',
    'p': 'p',
}


# DO NOT EDIT

CLIENT_ID_KEY = "CLIENT_ID"

def getVersion():
    VERSION_PATH = "../VERSION"
    if os.path.exists(VERSION_PATH):
        f = open(VERSION_PATH, "r")
        return f.readlines()[0]

VERSION = getVersion()

SERVER_DISCONNECTED = "Not Connected"

DATA_SERVER_IP = "127.0.0.1:5000"