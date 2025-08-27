import time
import requests
import threading
from flask import Flask

app = Flask(__name__)

# 🌍 Lista siti da visitare (puoi aggiungerne quanti vuoi)
URLS = [
    "https://httpbin.org/get",
    "https://example.com",
    "https://jsonplaceholder.typicode.com/todos/1"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/"
}

def autosurf_loop(interval_seconds=120):
    """Ciclo infinito che visita i siti"""
    while True:
        for url in URLS:
            try:
                print(f"🌍 Visito {url} ...")
                response = requests.get(url, headers=HEADERS, timeout=15)
                print(f"✅ {url} → {response.status_code} | {response.text.strip()[:100]}")
            except Exception as e:
                print(f"❌ Errore con {url}: {e}")
        print(f"⏳ Aspetto {interval_seconds} secondi...\n")
        time.sleep(interval_seconds)

@app.route("/")
def home():
    return "🚀 Autosurf bot attivo su Render!"

def start_background_thread():
    """Avvia il thread che gira in loop"""
    t = threading.Thread(target=autosurf_loop, daemon=True)
    t.start()

if __name__ == "__main__":
    start_background_thread()
    app.run(host="0.0.0.0", port=10000)


