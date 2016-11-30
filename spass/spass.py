import spass.storage, spass.password, spass.crypt

def check_params(params, required):
    for i in range(len(required)):
        if required[i] not in params:
            raise ValueError("Please specify " + required[i])

def load_data():
    try:
        data = spass.storage.load()
    except:
        data = {}
    return data

def update(a):
    check_params(a, ['account'])
    data = load_data()
    password = spass.password.generate(a)
    data[a['account']] = spass.crypt.encrypt(password)
    spass.storage.save(data)
    return password

def get(a):
    check_params(a, ['account'])
    data = load_data()
    if a['account'] not in data:
        raise ValueError("account doesn't exist")
    return spass.crypt.encrypt(data[a['account']])

def set(a):
    check_params(a, ['account', 'password'])
    data = load_data()
    data[a['account']] = spass.crypt.encrypt(a['password'])
    spass.storage.save(data)
    return a['password']
    
def delete(a):
    check_params(a, ['account'])
    data = load_data()
    if a['account'] not in data:
        raise ValueError("account doesn't exist")
    del data[a['account']]
    spass.storage.save(data)
    return True

def dump_export(a):
    check_params(a, ['file'])
    data = load_data()
    password = False
    if 'password' in a:
        password = a['password']
    out = {}
    for k in data:
        item = spass.crypt.encrypt(data[k])
        if password:
            out[k] = spass.crypt.key_encrypt(item, password)
        else:
            out[k] = item
    spass.storage.save_json(out, a['file'])
    return True

def dump_import(a):
    check_params(a, ['file'])
    data = load_data()
    password = False
    if 'password' in a:
        password = a['password']
    new_data = spass.storage.load_json(a['file'])
    for k in new_data:
        if password:
            item = spass.crypt.key_encrypt(new_data[k], password)
        else:
            item = new_data[k]
        data[k] = spass.crypt.encrypt(item)
    spass.storage.save(data)
    return True
