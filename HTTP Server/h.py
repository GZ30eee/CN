import http.server
import socketserver

# Define the handler for the HTTP requests
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"  # Serve the index.html file on root path
        return super().do_GET()

# Set up the HTTP server
def run_server():
    port = 8080
    handler = MyHttpRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running on http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
