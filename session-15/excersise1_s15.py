import http.server
import socketserver
import termcolor

PORT = 8006


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        requestline = self.requestline
    # -- printing the request line

        termcolor.cprint(self.requestline, 'green')
        if requestline.startswith("GET /") or requestline.startswith("GET /echo"):

            f = open("form1.html", 'r')
            contents = f.read()
        else:
            f = open("form_ex_error.html", 'r')
            contents = f.read()

        self.send_response(200) # everything is OK (happy server)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
