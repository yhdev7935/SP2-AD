import pickle
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = dict()
recentMapID = list()
playerMapID = dict()

def readDB():
    global todos, recentMapID, playerMapID
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
        
    fH.close()

def writeDB():
    global todos, recentMapID, playerMapID
    fH = open("todos.dat", 'wb')
    pickle.dump(todos, fH)
    
    fH = open("recentMapID.dat", 'wb')
    pickle.dump(recentMapID, fH)
    
    fH = open("playerMapID.dat", 'wb')
    pickle.dump(playerMapID, fH)

    fH.close()

class TodoSimple(Resource):
    
    def get(self, command):
        mapID = command
        mapDict = todos[mapID]

        playerID = mapDict['playerID']
        TimeUpload = mapDict['TimeUpload']
        mapName = mapDict['mapName']
        mapData = mapDict['mapData']

        return "mapID: %s\n" \
               "playerID: %s\n" \
               "TimeUpload: %s\n" \
               "mapName: %s\n" \
               "mapData: %s" \
               % (mapID, playerID, TimeUpload, mapName, mapData)

    def put(self, command):
        global todos, recentMapID, playerMapID
        
        if command == 'upload':
            mapID = request.form['mapID']
            playerID = request.form['playerID']
            TimeUpload = request.form['TimeUpload']
            mapName = request.form['mapName']
            mapData = request.form['mapData']

            todos[mapID] = {'playerID': playerID, 'TimeUpload': TimeUpload, 'mapData': mapData, 'mapName': mapName}
        
            recentMapID.append(mapID)
            recentMapID = recentMapID[-500:]
        
            if playerID not in playerMapID:
                playerMapID[playerID] = list()
            playerMapID[playerID].append(mapID)
            
            writeDB()
            
        elif command == 'myMap': # myMap playerID
            playerID = request.form['playerID']
            return playerMapID[playerID] #playerMapID = {playerID:[MapID...]}
            
        elif command == 'recentMap': # recentMap
            return recentMapID

api.add_resource(TodoSimple, '/<string:command>')

if __name__ == '__main__':
    readDB()
    app.run(debug=True)
