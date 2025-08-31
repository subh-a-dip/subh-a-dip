#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🐍 Snake Game Server Starting...")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"🎮 Play Snake Game at: http://localhost:{PORT}/snake-game.html")
        print(f"🛑 Press Ctrl+C to stop the server")
        
        # Auto-open the game in browser
        webbrowser.open(f'http://localhost:{PORT}/snake-game.html')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped!")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()