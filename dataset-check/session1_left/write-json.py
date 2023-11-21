import json

# Your dictionary data
dictionary_data = {
    "key": "value",
    "list": [1, 2, 3],
    "nested": {"a": 10, "b": 20}
}

# Specify the filename for the JSON file
json_filename = 'your_file.json'

# Open the JSON file for writing
with open(json_filename, 'w') as json_file:
    # Use json.dump to write the dictionary data to the file
    json.dump(dictionary_data, json_file, indent=2)
