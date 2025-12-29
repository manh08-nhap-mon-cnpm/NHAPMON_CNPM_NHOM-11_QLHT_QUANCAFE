import http.server
import socketserver
import webbrowser
import os
import sys

# Cấu hình Port
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Xóa các ký tự có dấu để tránh lỗi Unicode trên Terminal Windows
print("-" * 50)
print(f"STARBUCKS HUB SYSTEM IS STARTING...")
print(f"Server local: http://localhost:{PORT}")
print(f"Trang chu: http://localhost:{PORT}/index.html")
print("-" * 50)

# Tự động mở trình duyệt (Cốc Cốc/Chrome sẽ tự bật)
url = f"http://localhost:{PORT}/index.html"
webbrowser.open(url)

# Khởi tạo Server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        print("He thong dang san sang. Nhan Ctrl+C de dung server.")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer da dung.")
        sys.exit(0)