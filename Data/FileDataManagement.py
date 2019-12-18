import pickle, os, string, random


class DataManagement:

    def __init__(self, file):
        self.filepath = "../Data/" + file

        # if file doesn't exist
        if os.path.exists(self.filepath) == False:
            print("Creating Files... %s" % self.filepath)
            temp = open(self.filepath, "wb")
            temp.close()

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
