#!/usr/bin/env python3

import http.server
import socketserver
from sys import argv


class Handler(http.server.SimpleHTTPRequestHandler):
    """
    Extend the base request handler to allow us to mess with how it outputs request data.
    """

    def do_GET(self):
        """Override normal GET method."""
        print(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    PORT = int(argv[1])

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print('Serving HTTP on port {}...'.format(PORT))
    httpd.serve_forever()
