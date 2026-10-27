import sqlite3
import pandas as pd

DB_PATH = "data/tracker.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            date_applied TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_application(company, role, status, date_applied, notes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO applications (company, role, status, date_applied, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (company, role, status, date_applied, notes))
    conn.commit()
    conn.close()

def get_applications():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM applications", conn)
    conn.close()
    return df