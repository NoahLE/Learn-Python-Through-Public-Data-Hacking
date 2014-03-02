#!/usr/bin/env python
# bussim.py
#
# Simulated access to CTA website for the "Learn Python through Public Data Hacking"
# tutorial.  Run this script if you have no internet access or connectivity
# is very poor.

from datetime import datetime
import os
import gzip
import re
import time

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer

dirname = os.path.join(os.path.dirname(__file__),'data','buses')
basetime = datetime.today()
files = sorted([name for name in os.listdir(dirname)
                if name.endswith('.xml.gz')])

class BusRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        elapsed = datetime.today() - basetime
        minutes = (elapsed.seconds // 60)
        filename = files[minutes]
        fullname = os.path.join(dirname, filename)
        f = gzip.open(fullname, 'rb')
        data = f.read()
        f.close()
        data = re.sub(br'<time>(.*?)</time>',
                          lambda m: b'<time>' + time.ctime().encode('ascii') + b'</time>', data)
        self.send_response(200, 'OK')
        self.send_header('content-type', 'application/xml')
        self.end_headers()
        self.wfile.write(data)

from functools import partial
serv = HTTPServer(('', 8800), BusRequestHandler)
print('''
Simulated bus-system API server running at http://localhost:8800.
In your code, change all URLs from http://ctabustracker.com/
to http://localhost:8800/.   Note: this server only knows about
a single bus route (#22) as described in the tutorial.
''')
serv.serve_forever()
