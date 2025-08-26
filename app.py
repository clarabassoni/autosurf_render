import time
import json
import requests
from flask import Flask

app = Flask(__name__)

# Headers per simulare un browser reale
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/"
}

# Carica configurazione
with open("config.json") as f:
    CONFIG = json.load(f)

URLS = CONFIG.get("urls", ["https://httpbin.org/get"])
INTERVAL = CONFIG.get("interval_seconds", 120)

def keep_alive_loop():
    while True:
        for url in URLS:
            try:
                print(f"🌐 Invia richiesta a {url} simulando un browser...")
                response = requests.get(url, headers=HEADERS, timeout=20)
                print(f"✅ {response.status_code} - {response.text.strip()[:100]}")
            except Exception as e:
                print("❌ Errore:", e)
        print(f"⏳ Aspetto {INTERVAL} secondi...\n")
        time.sleep(INTERVAL)

@app.route('/')
def home():
    return "🌍 Autosurf bot attivo su Render!"

if __name__ == "__main__":
    import threading
    t = threading.Thread(target=keep_alive_loop)
    t.daemon = True
    t.start()
    app.run(host="0.0.0.0", port=10000)
