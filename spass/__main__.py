import os, sys, getopt, importlib

def main():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "", ["password=", "length=", "file=", "update=", "get=", "set=", "delete=", "export", "import", "generate"])
    func = ''
    func_argv = {}
    module = 'spass.spass'
    for o, a in opts:
        if o == '--generate':
            func = 'generate'
            module = 'spass.password'
        if o == '--update':
            func = 'update'
            func_argv['account'] = a
        if o == '--get':
            func = 'get'
            func_argv['account'] = a
        if o == '--delete':
            func = 'delete'
            func_argv['account'] = a
        if o == '--set':
            func = 'set'
            func_argv['account'] = a
        if o == '--export':
            func = 'dump_export'
        if o == '--import':
            func = 'dump_import'
        if o == '--password':
            func_argv['password'] = a
        if o == '--length':
            func_argv['length'] = a
        if o == '--file':
            func_argv['file'] = a
    print(getattr(importlib.import_module(module), func)(func_argv))

if __name__ == "__main__":
    main()
