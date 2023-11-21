import pickle
import json
import numpy as np

# Load the Pickle file
pkl_filename = 'gt_data.pkl'
with open(pkl_filename, 'rb') as pkl_file:
    data = pickle.load(pkl_file)

# Save the data to a text file using numpy serialization
text_filename = 'gt_data.txt'
with open(text_filename, 'w') as text_file:
    np.save(text_file, data)
