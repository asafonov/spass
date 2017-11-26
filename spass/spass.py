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
    simple = False
    if 'simple' in a:
        simple = a['simple']
    generated = spass.password.generate(a, simple)
    password = a['password'] if 'password' in a else ''
    data[a['account']] = spass.crypt.encrypt(generated, password)
    spass.storage.save(data)
    return generated

def get(a):
    check_params(a, ['account'])
    data = load_data()
    if a['account'] not in data:
        raise ValueError("account doesn't exist")
    password = a['password'] if 'password' in a else ''
    return spass.crypt.decrypt(data[a['account']], password)

def set(a):
    check_params(a, ['account', 'password'])
    data = load_data()
    password = a['password'] if 'password' in a else ''
    data[a['account']] = spass.crypt.encrypt(a['password'], password)
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
        item = spass.crypt.decrypt(data[k])
        if password:
            out[k] = spass.crypt.key_encrypt(item, spass.crypt.hash(password + k))
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
            item = spass.crypt.key_decrypt(new_data[k], spass.crypt.hash(password + k))
        else:
            item = new_data[k]
        data[k] = spass.crypt.encrypt(item)
    spass.storage.save(data)
    return True
