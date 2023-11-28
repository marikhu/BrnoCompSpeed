import pickle
import json

# Load the Pickle file
pkl_filename = 'gt_data_3_cars.pkl'
with open(pkl_filename, 'rb') as pkl_file:
    data = pickle.load(pkl_file)


print(data)
