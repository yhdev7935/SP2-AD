import pickle

file = open('test.dat', "rb")

list = pickle.load(file)

print(list)