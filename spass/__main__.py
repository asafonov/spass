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

def daemon():
    import socket

    HOST, PORT = '', 9092

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print('Serving HTTP on port ' + str(PORT) + ' ...')
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        req_s = request.decode('utf-8').split("\n")

        http_response = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
<head></head>
<body>
<h1>Hello world<h1>
</body>
</html>
"""
        client_connection.sendall(http_response.encode("utf-8"))
        client_connection.close()

if __name__ == "__main__":
    main()
