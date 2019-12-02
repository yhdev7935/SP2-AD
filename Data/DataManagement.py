import pickle, os, string, random

class DataManagement:

    def __init__(self, file):
        self.filepath = "../Data/" + file

        # if file doesn't exist
        if os.path.exists(self.filepath) == False:
            print("Creating Files... %s" % self.filepath)
            temp = open(self.filepath, "wb")
            temp.close()

    def genKey(self, _len=20):
        ret = ""
        string_pool = string.ascii_letters + string.digits
        for i in range(_len):
            ret += random.choice(string_pool)
        return ret

    def readFile(self):
        readfile = open(self.filepath, "rb")
        try:
            data = pickle.load(readfile)
        except EOFError:
            data = dict()
        return data

    def get(self, key):
        data = self.readFile()
        if key in data:
            ret = data[key]
        else:
            ret = None
        return ret

    def set(self, key, value):
        data = self.readFile()

        # Write Data
        data[key] = value

        writefile = open(self.filepath, "wb")
        pickle.dump(data, writefile)
        writefile.close()

    def delete(self):
        os.remove(self.filepath)

mapID = ["mapID", 0]
playerID = ["playerID", 1]
TimeUpload = ["TimeUpload", 2]
mapName = ["mapName", 3]
mapData = ["mapData", 4]

def getListViewDataFormat(mapID, playerID, TimeUpload, mapName, mapData):
    return "mapID: %s\n" \
           "playerID: %s\n" \
           "TimeUpload: %s\n" \
           "mapName: %s\n" \
           "mapData: %s"\
           % (mapID, playerID, TimeUpload, mapName, mapData)

def getListViewData(data, dataEnum) -> string:
    data = data.split('\n')[dataEnum[1]] # select line
    data = data.split(':')[1][1:]
    return data

if __name__ == "__main__":
    data = getListViewDataFormat("A", "B", "C", "D", "E")
    print(getListViewData(data, mapData))



