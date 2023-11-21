import pickle
import json

# Load the Pickle file
pkl_filename = 'gt_data.pkl'
with open(pkl_filename, 'rb') as pkl_file:
    data = pickle.load(pkl_file)


print(data)
