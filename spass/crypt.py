import spass.device, hashlib

def encrypt(s, password = ''):
    key = get_key(password)
    key_len = len(key)
    s_len = len(s)
    ret = ''
    for i in range(s_len):
        ret += chr(ord(s[i]) ^ ord(key[i % key_len]))
    return ret

def get_key(password = ''):
    key = password + str(spass.device.get_device_id()) + spass.device.get_username()
    return hashlib.sha256(key.encode()).hexdigest()
