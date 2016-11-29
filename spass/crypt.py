def encrypt(s, key):
    key_len = len(key)
    s_len = len(s)
    ret = ''
    for i in range(s_len):
        ret += chr(ord(s[i]) ^ ord(key[i % key_len]))
    return ret
