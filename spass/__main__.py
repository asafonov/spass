import os, sys, getopt, importlib

def main():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "", ["password=", "length=", "account=", "update", "generate", "get"])
    func = ''
    func_argv = {}
    module = ''
    for o, a in opts:
        if o == '--generate':
            func = 'generate'
            module = 'spass.password'
        if o == '--update':
            func = 'update'
            module = 'spass.spass'
        if o == '--get':
            func = 'get'
            module = 'spass.spass'
        if o == '--password':
            func_argv['password'] = a
        if o == '--length':
            func_argv['length'] = a
        if o == '--account':
            func_argv['account'] = a
    print(getattr(importlib.import_module(module), func)(func_argv))

if __name__ == "__main__":
    main()
