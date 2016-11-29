import json, os

def load():
    return load_json(os.path.expanduser('~') + '/.spass/data')

def save(data):
    save_json(data, os.path.expanduser('~') + '/.spass/data')

def save_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def load_json(filename):
    f = open(filename)
    data = json.loads(f.read())
    f.close()
    return data
