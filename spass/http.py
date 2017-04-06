from spass import spass, crypt, storage
import urllib.parse

data = spass.load_data()

def show(req):
    url = req.split(' ')[1]
    if url == '/':
        return main_page()
    elif url[0:5] == '/get/':
        return get(url[5:])
    elif url[0:5] == '/del/':
        return dele(url[5:])
    else:
        return error404()

def get_header(status, params = {}):
    header = "HTTP/1.1 " + status + "\n"
    for i in params:
        header += i + ": " +  params[i] + "\n"
    return header + "\n"

def get(account):
    account = urllib.parse.unquote(account)
    print('Getting ' + account)
    if account not in data:
        return error404()
    return get_header("200 OK") + crypt.encrypt(data[account])

def dele(account):
    print('Deleting ' + account)
    if account not in data:
        return error404()
    del data[account]
    storage.save(data)
    return status_ok()

def error404():
    return get_header("404 Not Found")

def status_ok():
    return get_header("200 OK")

def main_page():
    print('Displaying main page')
    header = get_header("200 OK", {"Content-Type": "text/html; charset=UTF-8"})
    head = """<html><head>
        <style>
            * {
                font-family: monospace;
                background-color: black;
                color: #b0c7d4;
            }
            td{
                font-size: 36pt;
            }
            table {
                margin: 12px;
            }
            td {
                padding: 12px;
                border-bottom: 1px solid #cccccc;
                margin: 0px;
            }
            h1 {
                font-size: 48pt;
                text-align: center;
            },
            a {
                cursor: pointer;
            }
            .green {
                color: #66c066;
            }
            .red {
                color: #c06666;
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
    body = "<body><h1>Spass Manager UI</h1><table width='100%' cellpadding='0' cellspacing='0'>"
    for i in data:
        body += "<tr><td>" + i + "</td><td width='100%'> *** </td><td><nobr><a class='green' onclick='show(this, \"" + i + "\")'>&#128269;</a><a onclick='del(this, \"" + i + "\")' class='red'>&#10060;</a></nobr></td></tr>"

    body += "</table></body></html>"

    return header + head + body
