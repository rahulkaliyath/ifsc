import json

def load_json(PATH):
    file_json = json.loads(open(PATH).read())
    return file_json