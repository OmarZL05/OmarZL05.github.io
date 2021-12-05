import http.server

import socketserver

PORT = 8000                               

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.0.110", PORT), Handler) as httpd:
    print(f"Servidor iniciado en el puerto: {PORT}")
    httpd.serve_forever()