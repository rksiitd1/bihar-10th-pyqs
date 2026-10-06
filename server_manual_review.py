"""
Local Server & Sync Bridge for Bihar 10th PYQ Manual Classifier.
- Serves the UI directly on http://localhost:8000
- Auto-opens browser
- Provides /api/save endpoint that continuously saves classifications directly into manual_classifications.json in this directory without download dialogs
- Provides /api/apply endpoint that immediately applies decisions to {subject}_data_jevified/ and rebuilds pro directories with 1 click!
"""

import http.server
import socketserver
import json
import os
import sys
import webbrowser
import subprocess

PORT = 8000
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


class ReviewHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body.decode('utf-8'))
                with open('manual_classifications.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok', 'saved_count': len(data.get('classifications', []))}).encode('utf-8'))
                print(f"💾 Auto-saved {len(data.get('classifications', []))} classifications to manual_classifications.json")
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))

        elif self.path == '/api/apply':
            try:
                res = subprocess.run([sys.executable, 'apply_manual_classifications.py'], capture_output=True, text=True)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok', 'output': res.stdout}).encode('utf-8'))
                print("🔄 Auto-applied classifications to production data!")
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Ensure manual_review_data.json exists
    if not os.path.exists('manual_review_data.json'):
        print("Exporting manual_review_data.json...")
        subprocess.run([sys.executable, 'export_for_review.py'])

    handler = ReviewHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://localhost:{PORT}/manual_review.html"
        print("="*60)
        print(f"🚀 Manual Review Server running at: {url}")
        print("⚡ Auto-saves continuously to manual_classifications.json")
        print("⚡ 1-click 'Apply to Dataset' directly from UI")
        print("="*60)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == '__main__':
    main()
