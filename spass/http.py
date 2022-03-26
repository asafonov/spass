from spass import spass, crypt, storage
import urllib.parse
import json
from http.server import BaseHTTPRequestHandler
import os

data = spass.load_data()

class HTTPHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status = 200, headers = {}):
        self.send_response(status)

        for i in headers:
            self.send_header(i, headers[i])

        self.end_headers();

    def do_GET (self):
        response = ''

        if self.path == '/':
            response = self.main_page()
        elif self.path[0:5] == '/get/':
            response = self.get(self.path[5:])
        elif self.path[0:5] == '/del/':
            response = self.dele(self.path[5:])
        elif self.path == '/data/':
            response = self.as_json()
        else:
            self._set_headers(200, {"Access-Control-Allow-Origin": "*"})
            home = os.path.realpath(__file__).replace('http.py', '')
            filename = home + self.path[1:]
            f = open(filename, 'rb')
            response = f.read()
            f.close()
            self.wfile.write(response)
            return

        self.wfile.write(response.encode('utf-8'))

    def do_OPTIONS (self):
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "*"})

    def do_POST (self):
        print('POST request received')
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = post_data.decode('utf-8')
        len(data) > 0 and json.dumps(spass.import_data(json.loads(data), False, ''))
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*"})

    def as_json (self):
        print('Data request received')
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*"})
        return json.dumps(spass.load_unencrypted())

    def get (self, account):
        account = urllib.parse.unquote(account)
        print('Getting ' + account)

        if account not in data:
            self._set_headers(404)
            return ''

        self._set_headers(200)
        return crypt.decrypt(data[account], account)

    def dele (self, account):
        account = urllib.parse.unquote(account)
        print('Deleting ' + account)

        if account not in data:
            self._set_headers(404)
            return ''

        del data[account]
        storage.save(data)
        self._set_headers(200)
        return ''

    def main_page (self):
        print('Displaying main page')
        self._set_headers(200, {"Content-Type": "text/html; charset=UTF-8"})
        head = """<html><head>
            <style>
                * {
                    font-family: PoiretOne-Regular;
                    padding: 0;
                    margin: 0;
                    border: 0;
                }
                .background {
                    background: url(images/01.jpg);
                    background-size: 100% 100%;
                    width: 100%;
                    height: 100%;
                    position: fixed;
                    z-index: -1;
                }
                td {
                    font-size: 36pt;
                    font-weight: bold;
                    color: red;
                }
                td {
                    padding: 12px;
                    border-bottom: 1px solid #cccccc;
                    margin: 0px;
                }
                h1 {
                    font-size: 52pt;
                    text-align: center;
                    padding-bottom: 3%;
                    color: red;
                }
                a {
                    cursor: pointer;
                }
            </style>
            <script>
                function get(url, callback) {
                    var req = new XMLHttpRequest();
                    if (req) {
                        req.onreadystatechange = function() {response(callback, req)};
                        req.open("GET", url, true);
                        req.send({});
                    }
                }

                function response(callback, req) {
                    if (req.readyState == 4) {
                        if (req.status == 200) {
                            callback(req.responseText);
                        }
                    }
                }

                function show(button, account) {
                    get('/get/' + account, function(password) {
                        button.parentNode.parentNode.parentNode.getElementsByTagName('td')[1].innerHTML = password.replace('<', '&lt;').replace('>', '&gt;');
                    });
                }

                function del(button, account) {
                    if (confirm("Are you sure you want to delete " + account)) {
                        get('/del/' + account, function() {
                            button.parentNode.parentNode.parentNode.style.display = 'none';
                        });
                    }
                }
            </script>
        </head>"""
        body = "<body><div class='background'></div><h1>Spass Manager UI</h1><table width='100%' cellpadding='0' cellspacing='0'>"
        for i in data:
            body += "<tr><td>" + i + "</td><td width='100%'> *** </td><td><nobr><a class='green' onclick='show(this, \"" + i + "\")'>👀</a><a onclick='del(this, \"" + i + "\")' class='red'>🚫</a></nobr></td></tr>"

        body += "</table></body></html>"

        return head + body
