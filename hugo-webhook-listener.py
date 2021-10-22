import json, hmac, hashlib, os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers.get("Content-Length"))
            orig_signature = self.headers.get("X-Hub-Signature-256")
            body = self.rfile.read(content_length)
            json_body = json.loads(body)
            global secret
            encoded_secret = (secret.strip()).encode()
            signature = hmac.new(encoded_secret, body, hashlib.sha256).hexdigest()
            signature = "sha256=" + signature
            if orig_signature == signature:
                print("signature ok")

                os.chdir("/var/www/otit.fi")
                os.system("git stash -u")
                os.chdir("/var/www/otit.fi")
                os.system("git pull")
                os.chdir("/var/www/otit.fi")
                os.system("hugo")
            else:
                print("signatures do not match")
            print(json_body)
            self.send_response(200)
        else:
            self.send_response(404)

with open("secret", "r") as f:
    secret = f.readline()
    f.close()

httpd = HTTPServer(("127.0.0.1", 55555), MyHandler)
httpd.serve_forever()
