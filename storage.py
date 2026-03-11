import sqlite3
import json
from datetime import datetime

DB = "runs.db"

def save_run(data):

    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        data TEXT
    )
    """)

    conn.execute(
        "INSERT INTO runs (timestamp,data) VALUES (?,?)",
        (datetime.now().isoformat(), json.dumps(data))
    )

    conn.commit()
    conn.close()


def list_runs():

    conn = sqlite3.connect(DB)

    rows = conn.execute(
        "SELECT timestamp,data FROM runs ORDER BY id DESC LIMIT 10"
    ).fetchall()

    conn.close()

    return rows
