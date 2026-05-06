import importlib.util
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
BOT_FILE = ROOT / "Rule_Based_chat-bot_AI.py"


def load_bot():
    spec = importlib.util.spec_from_file_location("rule_based_chatbot", BOT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bot = load_bot()


class ChatHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404, "Not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(content_length)
            data = json.loads(body or b"{}")
            message = str(data.get("message", "")).strip()

            if not message:
                self.send_json({"reply": "Please type a message first."}, status=400)
                return

            self.send_json({"reply": bot.get_response(message)})
        except json.JSONDecodeError:
            self.send_json({"reply": "Invalid request format."}, status=400)
        except Exception:
            self.send_json({"reply": "Something went wrong. Please try again."}, status=500)

    def send_json(self, payload, status=200):
        response = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


def run(host="127.0.0.1", port=8000):
    server = ThreadingHTTPServer((host, port), ChatHandler)
    print(f"Chatbot website is running at http://{host}:{port}")
    print("Press Ctrl+C to stop the server.")
    server.serve_forever()


if __name__ == "__main__":
    run()
