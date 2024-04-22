import http.server
import socketserver

# Initialize the calorie count
current_calories = 0

# Define the handler to serve the HTML page
class CalorieCounterHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global current_calories
        if self.path == '/':
            # Serve the index.html page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index2.html', 'r') as f:
                html_content = f.read()
            self.wfile.write(html_content.encode())
        else:
            # Handle other requests (e.g., CSS, images, etc.)
            super().do_GET()

    def do_POST(self):
        global current_calories
        if self.path == '/add':
            # Increment the calorie count
            current_calories += 10  # You can adjust this value as needed
        elif self.path == '/reset':
            # Reset the calorie count
            current_calories = 0
        # Redirect back to the main page
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

# Set up the server
PORT = 8000
with socketserver.TCPServer(("", PORT), CalorieCounterHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
