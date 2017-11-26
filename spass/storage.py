import json, os
import spass.crypt

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
    
def get_password_filename():
    return os.path.expanduser('~') + '/.spass/.password'
    
def password():
    filename = get_password_filename()
    if os.path.exists(filename):
        f = open(filename)
        data = f.read()
        f.close()
        return spass.crypt.decrypt(data)
    return False
    
def save_password(argv):
    filename = get_password_filename()
    f = open(filename, 'w')
    f.write(spass.crypt.encrypt(argv['password']))
    f.close()
