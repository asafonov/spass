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
    
