# IMPORTS
import os
import json

# SHOW WHAT PATH CONTAINS
def contains(dirs):
    try:
        path = '/'.join(dirs)
        return os.listdir(path)
    except:
        return False

# PROCESS TEXT INTO YAML FILE
def serialize_yaml(data):
    try:
        eval(data)
        return True
    except:
        return False
    
# LOAD & SERIALIZE JSON FILE
def load_json(path):
    with open(path) as file:
        return json.load(file)