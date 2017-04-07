import random

def generate(a, simple = False):
    if 'length' in a:
        length = int(a['length'])
    else:
        length = 16
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if not simple:
        alphabet += "!#?@-*()[]\/+%:;&{},.<>"
    ret = ''
    alphabet_len = len(alphabet)
    for i in range(length):
       next_index = random.randrange(alphabet_len)
       ret += alphabet[next_index]
    return ret
