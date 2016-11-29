import spass.storage, spass.password, spass.crypt

def update(a):
    if 'account' not in a:
        raise ValueError("please specify account for update")

    try:
        data = spass.storage.load()
    except:
        data = {}

    password = spass.password.generate(a)
    data[a['account']] = spass.crypt.encrypt(password)
    spass.storage.save(data)
    return password

def get(a):
    if 'account' not in a:
        raise ValueError("please specify account for get")

    try:
        data = spass.storage.load()
    except:
        data = {}

    if a['account'] not in data:
        raise ValueError("account doesn't exist")

    return spass.crypt.encrypt(data[a['account']])
