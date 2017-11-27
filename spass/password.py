import random

simple_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = simple_alphabet + "!#?@-*()[]\/+%:;&{},.<>_"

def generate(a, simple = False):
    if 'length' in a:
        length = int(a['length'])
    else:
        length = 16
    alpha = alphabet
    if simple:
        alpha = simple_alphabet
        
    ret = ''
    alphabet_len = len(alpha)
    for i in range(length):
       next_index = random.randrange(alphabet_len)
       ret += alpha[next_index]
    return ret
