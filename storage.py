import sqlite3
import json
from datetime import datetime

DB = "runs.db"


def _init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            data      TEXT
        )
    """)
    conn.commit()


def save_run(data):
    """Sauvegarde un run dans la base SQLite."""
    conn = sqlite3.connect(DB)
    _init_db(conn)
    conn.execute(
        "INSERT INTO runs (timestamp, data) VALUES (?, ?)",
        (datetime.now().isoformat(), json.dumps(data))
    )
    conn.commit()
    conn.close()


class Run:
    """Objet représentant un run, accessible par attribut dans les templates Jinja."""
    def __init__(self, row_id, timestamp, data_str):
        self.id = row_id
        self.timestamp = timestamp
        payload = json.loads(data_str) if data_str else {}
        self.payload = payload
        self.passed = payload.get("passed", 0)
        self.failed = payload.get("failed", 0)
        self.error_rate = payload.get("error_rate", 0)
        self.latency_ms_avg = payload.get("latency_ms_avg", 0)
        self.latency_ms_p95 = payload.get("latency_ms_p95", 0)
        self.availability = payload.get("availability", 0)
        self.tests = payload.get("tests", [])


def list_runs():
    """Retourne les 10 derniers runs sous forme d'objets Run."""
    try:
        conn = sqlite3.connect(DB)
        _init_db(conn)
        rows = conn.execute(
            "SELECT id, timestamp, data FROM runs ORDER BY id DESC LIMIT 10"
        ).fetchall()
        conn.close()
        return [Run(r[0], r[1], r[2]) for r in rows]
    except Exception:
        return []


def list_runs_json():
    """Retourne les 10 derniers runs sous forme de dicts (pour /dashboard-json)."""
    try:
        conn = sqlite3.connect(DB)
        _init_db(conn)
        rows = conn.execute(
            "SELECT id, timestamp, data FROM runs ORDER BY id DESC LIMIT 10"
        ).fetchall()
        conn.close()
        result = []
        for r in rows:
            d = json.loads(r[2]) if r[2] else {}
            d["id"] = r[0]
            d["timestamp"] = r[1]
            result.append(d)
        return result
    except Exception:
        return []
