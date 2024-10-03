import json

def load_json(filepath):
    """Loads JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(filepath, data):
    """Saves JSON data to a file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
