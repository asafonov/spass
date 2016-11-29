import json, os

def load():
    f = open(os.path.expanduser('~') + '/.spass/data')
    data = json.loads(f.read())
    f.close()
    return data

def save(data):
    with open(os.path.expanduser('~') + '/.spass/data', 'w') as outfile:
        json.dump(data, outfile)
