"""Project 2 entry point; legacy panel preserved as lab19_app.py."""
from http.server import ThreadingHTTPServer
from webapp import Handler

if __name__ == "__main__":
    print("Open http://127.0.0.1:8502 ; Ctrl+C stops", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8502), Handler).serve_forever()
