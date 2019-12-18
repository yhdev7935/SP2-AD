import pickle
import datetime
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = dict()
recentMapID = list()
playerMapID = dict()
mapIDList = list()

def readDB():
    global todos, recentMapID, playerMapID, mapIDList
    try:
        fH = open("todos.dat", 'rb')
        todos = pickle.load(fH)
    except FileNotFoundError as e:
        todos = dict()
        
    try:
        fH = open("recentMapID.dat", 'rb')
        recentMapID = pickle.load(fH)
    except FileNotFoundError as e:
        recentMapID = list()
        
    try:
        fH = open("playerMapID.dat", 'rb')
        playerMapID = pickle.load(fH)
    except FileNotFoundError as e:
        playerMapID = dict()

    try:
        fH = open("mapIDList.dat", 'rb')
        mapIDList = pickle.load(fH)
    except FileNotFoundError as e:
        mapIDList = list()

def writeDB():
    global todos, recentMapID, playerMapID, mapIDList
    fH = open("todos.dat", 'wb')
    pickle.dump(todos, fH)
    
    fH = open("recentMapID.dat", 'wb')
    pickle.dump(recentMapID, fH)
    
    fH = open("playerMapID.dat", 'wb')
    pickle.dump(playerMapID, fH)

    fH = open("mapIDList.dat", 'wb')
    pickle.dump(mapIDList, fH)

class TodoSimple(Resource):
    
    def get(self, command):
        # ex) get(http://127.0.0.1:5000/mapID).json()
        mapID = command
        recentDict = todos[mapID]
        return recentDict['mapData']

    def put(self, command):
        global todos, recentMapID, playerMapID
        
        if command == 'upload':
            # ex) put('http://127.0.0.1:5000/upload', data={'mapID': mapID, 'playerID': playerID, ......}).json()
            mapID = request.form['mapID']
            playerID = request.form['playerID']
            TimeUpload = request.form['TimeUpload']
            mapName = request.form['mapName']
            mapData = request.form['mapData']

            if mapID in mapIDList:
                print(mapID, '가 중복됨')

            todos[mapID] = {'mapID': mapID, 'playerID': playerID, 'TimeUpload': str(datetime.datetime.now()), 'mapData': mapData, 'mapName': mapName}

            mapIDList.append(mapID)
            recentMapID.append(todos[mapID])
            recentMapID = recentMapID[-500:]
        
            if not playerID in playerMapID:
                playerMapID[playerID] = list()
            playerMapID[playerID].append(todos[mapID])
            
            writeDB()
            
        elif command == 'myMap': # myMap playerID
            # ex) put('http://127.0.0.1:5000/myMap', data={'playerID': playerID}).json()
            playerID = request.form['playerID']
            return playerMapID[playerID][::-1] #playerMapID = {playerID:[MapID...]}

        elif command == 'recentMap': # recentMap
            # ex) put('http://127.0.0.1:5000/recentMap').json()
            return recentMapID[::-1]


api.add_resource(TodoSimple, '/<string:command>')

if __name__ == '__main__':
    readDB()
    app.run(debug=True)
