import pickle


with open('gt_data.pkl', 'rb') as f:
    data = pickle.load(f)
    print (data)
