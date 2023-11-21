import pickle
import json
import numpy as np

# Load the Pickle file
pkl_filename = 'gt_data.pkl'
with open(pkl_filename, 'rb') as pkl_file:
    data = pickle.load(pkl_file)

# Convert non-serializable objects to a serializable format
# Example: Convert NumPy arrays to lists
# You may need to customize this part based on the structure of your data
data_serializable = {
    key: value.tolist() if isinstance(value, (np.ndarray, np.generic)) else value
    for key, value in data.items()
}

# Save the data to a text file in JSON format
text_filename = 'gt_data.json'
with open(text_filename, 'w') as text_file:
    json.dump(data_serializable, text_file, indent=2)
