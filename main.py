from datetime import datetime
from pathlib import Path

import webview


class API:
    def uhrzeit(self):
        return datetime.now().strftime("%H:%M:%S")


if __name__ == "__main__":
    seite = Path(__file__).resolve().parent / "www" / "index.html"
    webview.create_window("Ionic + Python", str(seite), js_api=API())
    webview.start(http_server=True)
