import http.server
import socketserver
import os

# PORT = int(os.environ["PORT"])
PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("serving at port", PORT)
    http.serve_forever()
