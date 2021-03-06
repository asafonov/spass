import os, sys, getopt, importlib, spass.storage

def main():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "", ["set-password=", "password=", "length=", "file=", "update=", "get=", "set=", "delete=", "key=", "export", "import", "generate", "daemon", "simple", "print", "prompt", "set-password-prompt", "version", "list"])
    func = ''
    func_argv = {}
    default_params = spass.storage.get_params()
    module = 'spass.spass'
    xclip = sys.platform == 'linux'
    pbcopy = sys.platform == 'darwin'
    opts = list(default_params.items()) + opts
    for o, a in opts:
        if o == '--set-password':
            xclip = False
            module = 'spass.storage'
            func = 'save_password'
            func_argv['password'] = a
        if o == '--set-password-prompt':
            xclip = False
            module = 'spass.storage'
            func = 'save_password'
            func_argv['password'] = input('Please enter your password: ')
        if o == '--print':
            xclip = False
            pbcopy = False
        if o == '--prompt':
            func_argv['password'] = input('Please enter your password: ')
        if o == '--generate':
            func = 'generate'
            module = 'spass.password'
        if o == '--update':
            func = 'update'
            func_argv['account'] = a
        if o == '--simple':
            func_argv['simple'] = True
        if o == '--get':
            func = 'get'
            func_argv['account'] = a
        if o == '--delete':
            func = 'delete'
            func_argv['account'] = a
        if o == '--set':
            func = 'set'
            func_argv['account'] = a
            func_argv['set_password'] = args[0]
        if o == '--list':
            func = 'get_list'
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
        if o == '--key':
            func_argv['key'] = a
        if o == '--version':
            from spass.version import version
            print('SPass Smart Password Manager. Version: ' + version)
            return True
        if o == '--daemon':
            daemon()
            return True
    res = getattr(importlib.import_module(module), func)(func_argv)
    if xclip and isinstance(res, str):
        os.system('echo "' + res.replace('"', '\"') + '" | xclip -selection clipboard')
    elif pbcopy and isinstance(res, str):
        os.system('echo "' + res.replace('"', '\"') + '" | pbcopy')
    else:
        print(res)

def daemon():
    from http.server import HTTPServer
    from spass.http import HTTPHandler

    server_address = ('', 9092)
    httpd = HTTPServer(server_address, HTTPHandler)

    try:
        print('Serving HTTP on port ' + str(server_address[1]) + ' ...')
        httpd.serve_forever()
    except Exception:
        pass

    httpd.server_close()

if __name__ == "__main__":
    main()
