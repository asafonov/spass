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
    data[a['account']] = spass.crypt.encrypt(generated, password + a['account'])
    spass.storage.save(data)
    return generated

def get(a):
    check_params(a, ['account'])
    data = load_data()
    if a['account'] not in data:
        raise ValueError("account doesn't exist")
    password = a['password'] if 'password' in a else ''
    return spass.crypt.decrypt(data[a['account']], password + a['account'])

def set(a):
    check_params(a, ['account'])
    data = load_data()
    password = a['password'] if 'password' in a else ''
    data[a['account']] = spass.crypt.encrypt(a['set_password'], password + a['account'])
    spass.storage.save(data)
    return a['set_password']

def delete(a):
    check_params(a, ['account'])
    data = load_data()
    if a['account'] not in data:
        raise ValueError("account doesn't exist")
    del data[a['account']]
    spass.storage.save(data)
    return True

def load_unencrypted():
    data = load_data()
    out = {}

    for k in data:
        out[k] = spass.crypt.decrypt(data[k], k)

    return out

def dump_export(a):
    check_params(a, ['file'])
    data = load_data()
    key = False
    if 'key' in a:
        key = a['key']
    out = {}
    password = a['password'] if 'password' in a else ''
    for k in data:
        item = spass.crypt.decrypt(data[k], password + k)
        if key:
            out[k] = spass.crypt.key_encrypt(item, spass.crypt.hash(key + k))
        else:
            out[k] = item
    spass.storage.save_json(out, a['file'])
    return True

def dump_import(a):
    check_params(a, ['file'])
    data = load_data()
    key = False
    if 'key' in a:
        key = a['key']
    new_data = spass.storage.load_json(a['file'])
    password = a['password'] if 'password' in a else ''
    for k in new_data:
        if key:
            item = spass.crypt.key_decrypt(new_data[k], spass.crypt.hash(key + k))
        else:
            item = new_data[k]
        data[k] = spass.crypt.encrypt(item, password + k)
    spass.storage.save(data)
    return True

def get_list(a):
    ret = []
    data = load_data()
    for k in data:
        ret.append(k)
    return ret
