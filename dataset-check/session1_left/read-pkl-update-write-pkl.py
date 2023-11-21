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

for key in dictionary_data.keys():
    print(key)
  
# Get the list of 'carId' values in key 'cars'
key_to_update = 'cars'
car_ids = [car['carId'] for car in dictionary_data.get(key_to_update, [])]
print(car_ids)

# Update the list of dictionaries for the specified key
condition = lambda car: car.get('carId', 0) > 100
if key_to_update in dictionary_data and isinstance(dictionary_data[key_to_update], list):
    dictionary_data[key_to_update] = [car for car in dictionary_data[key_to_update] if not condition(car)]

# Save to pkl file
outFile="gt_data_out.pkl"
ensureDir(os.path.dirname(outFile))
with open(outFile, 'wb') as fid:
    pickle.dump(dictionary_data, fid, pickle.HIGHEST_PROTOCOL)





