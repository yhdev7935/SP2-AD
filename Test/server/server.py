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
        return todos[command] # {'playerId': playerID, 'timeUpload': timeUpload, 'mapData': mapData}

    def put(self, command):
        global todos, recentMapID, playerMapID
        puted = request.form['data'].split(' ')
        
        if command == 'upload': # upload playerID timeUpload mapData
            mapID, playerID, timeUpload, mapData = puted[0], puted[1], puted[2], puted[3]
            todos[mapID] = {'playerID': playerID, 'timeUpload': timeUpload, 'mapData': mapData}
        
            recentMapID.append(mapID)
            recentMapID = recentMapID[-500:]
        
            if playerID not in playerMapID:
                playerMapID[playerID] = list()
            playerMapID[playerID].append(mapID)
            
            writeDB()
        
        elif command == 'edit': # edit mapID
            mapID = puted[0]
            return todos[mapID]
            
        elif command == 'myMap': # myMap playerID
            playerID = puted[0]
            return playerMapID[playerID] #playerMapID = {playerID:[MapID...]}
            
        elif command == 'recentMap': # recentMap
            return recentMapID

api.add_resource(TodoSimple, '/<string:command>')

if __name__ == '__main__':
    readDB()
    app.run(debug=True)
