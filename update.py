# update.py

import sqlite3
from datetime import datetime

DB_NAME = "crypto.db"

def initDB():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            coin TEXT,
            price_usd REAL
        )
    """)
    conn.commit()
    conn.close()

def DB_save(prices):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for entry in prices:
        cur.execute("INSERT INTO prices (timestamp, coin, price_usd) VALUES (?, ?, ?)", entry)
    conn.commit()
    conn.close()
