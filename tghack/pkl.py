import pickle

f = open('model.pkl', 'rb')
data = pickle.load(f)

print(data)

f.close()