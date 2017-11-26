import spass.device, hashlib
from spass.password import alphabet

def encrypt(s, password = ''):
    key = get_key(password)
    return key_encrypt(s, key)

def key_encrypt(s, key, sign = 1):
    key_len = len(key)
    s_len = len(s)
    a_len = len(alphabet)
    ret = ''
    for i in range(s_len):
        position = alphabet.find(s[i]) + sign * alphabet.find(key[i % key_len])
        if position >= a_len:
            position = position - a_len
        if position < 0:
            position = position + a_len
        ret += alphabet[position]
    return ret
    
def key_decrypt(s, key):
    return key_encrypt(s, key, -1)
    
def decrypt(s, password = ''):
    key = get_key(password)
    return key_decrypt(s, key)

def get_key(password = ''):
    key = password + str(spass.device.get_device_id()) + spass.device.get_username()
    return hashlib.sha256(key.encode()).hexdigest()

def hash(s):
    return hashlib.sha256(s.encode()).hexdigest()
