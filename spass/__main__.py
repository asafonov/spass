import os, sys, getopt, importlib

def main():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "", ["password=", "length=", "account=", "update", "generate", "get", "set"])
    func = ''
    func_argv = {}
    module = 'spass.spass'
    for o, a in opts:
        if o == '--generate':
            func = 'generate'
            module = 'spass.password'
        if o == '--update':
            func = 'update'
        if o == '--get':
            func = 'get'
        if o == '--set':
            func = 'set'
        if o == '--password':
            func_argv['password'] = a
        if o == '--length':
            func_argv['length'] = a
        if o == '--account':
            func_argv['account'] = a
    print(getattr(importlib.import_module(module), func)(func_argv))

if __name__ == "__main__":
    main()
