"""
OmniCount Pro - Web Application & Local Showcase Server.
Serves the modern interactive web application index.html at http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean formatted logging
        print(f"[OmniCount Web] {self.address_string()} - {format % args}")

def run_server(port=PORT, auto_open=True):
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", port), Handler) as httpd:
        url = f"http://localhost:{port}"
        print("=" * 70)
        print("    👁️ OMNICOUNT PRO — SPATIAL CROWD VISION WEB DASHBOARD")
        print("=" * 70)
        print(f"[*] Serving files from: {DIRECTORY}")
        print(f"[*] Webpage available at: {url}")
        print(f"[*] Author: Anas Aleem (anasaleemofficial@gmail.com)")
        print("[*] Press Ctrl+C in terminal to stop server.")
        print("=" * 70)

        if auto_open:
            try:
                webbrowser.open(url)
            except Exception:
                pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Web server stopped.")
            httpd.server_close()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
