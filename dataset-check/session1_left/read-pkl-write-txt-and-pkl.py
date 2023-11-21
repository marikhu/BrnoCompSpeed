import pickle
import base64
import json
import os

def ensureDir(d):
    if len(d) > 0:
        if not os.path.exists(d):
            try:
                os.makedirs(d)
            except OSError as e:
                if e.errno != 17: # FILE EXISTS
                    raise e

#####################################

# Open the .pkl file for reading in binary mode
with open('gt_data.pkl', 'rb') as pkl_file:
    # Load the object from the .pkl file
    dictionary_data = pickle.load(pkl_file)

print(dictionary_data)
print(type(dictionary_data))

cacheFile="gt_data_out.pkl"
ensureDir(os.path.dirname(cacheFile))
with open(cacheFile, 'wb') as fid:
    pickle.dump(dictionary_data, fid, pickle.HIGHEST_PROTOCOL)

# Open the text file for writing
text_filename = "gt_data.txt"
with open(text_filename, 'w') as text_file:
    # Iterate through dictionary items and write them to the file
    for key, value in dictionary_data.items():
        text_file.write(key + ": " + str(value) + "\n")


json_filename = 'gt_data.json'

# Open the JSON file for writing
with open(json_filename, 'w') as json_file:
    # Use json.dump to write the dictionary data to the file
    json.dump(dictionary_data, json_file, indent=2)
