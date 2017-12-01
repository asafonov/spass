import json, os
import spass.crypt

def get_working_dir():
    return os.path.expanduser('~') + '/.spass/'

def load():
    return load_json(get_working_dir() + 'data')

def save(data):
    save_json(data, get_working_dir() + 'data')

def save_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def load_json(filename):
    f = open(filename)
    data = json.loads(f.read())
    f.close()
    return data
    
def save_password(argv):
    params = get_params()
    params['--password'] = spass.crypt.encrypt(argv['password'])
    save_json(params, get_params_filename())

def get_params_filename():
    return get_working_dir() + 'params'

def get_params():
    if os.path.exists(get_params_filename()):
        data = load_json(get_params_filename())
        if '--password' in data:
            data['--password'] = spass.crypt.decrypt(data['--password'])
        return data
    return {}
