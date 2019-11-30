import pickle

file = open('test.dat', "wb")

list = [1, 2, 3]
list2 = [4, 5, 6]

pickle.dump(list, file)
#pickle.dump(list2, file)

file.close()
