import json

# Specify the filename for the JSON file
json_filename = 'gt_data.txt'

# Open the JSON file for reading
with open(json_filename, 'r') as json_file:
    # Load the JSON data from the file
    dictionary_data = json.load(json_file)

# Now, 'dictionary_data' contains the content of the JSON file as a Python dictionary
print(dictionary_data)
