from flask import Flask
import threading
import time
import random
import os
import psycopg2
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


metrics.info("app_info", "Flask backend application", version="1.0.0")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

def test_db_connection():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            print("[DB] PostgreSQL connection OK", flush=True)
        except Exception as e:
            print(f"[DB ERROR] {e}", flush=True)
        time.sleep(5)

def generate_logs():
    while True:
        print(f"[BACKEND LOG] value={random.randint(100, 999)}", flush=True)
        time.sleep(1)

def generate_traffic():
    while True:
        try:
            requests.get("http://localhost:5000/")
        except Exception:
            pass
        time.sleep(1)
        
threading.Thread(target=generate_traffic, daemon=True).start()
threading.Thread(target=generate_logs, daemon=True).start()
threading.Thread(target=test_db_connection, daemon=True).start()

@app.route("/")
def index():
    return "Flask backend with PostgreSQL is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
