# Read the data with json format
import json

def import_json(file_fullname):
    with open(file_fullname) as data_file:    
        data = json.load(data_file)
    return(data)
