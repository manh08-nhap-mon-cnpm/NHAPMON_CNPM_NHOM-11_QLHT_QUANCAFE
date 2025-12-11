# database/db.py
import sqlite3
import os

DB_NAME = "database/cafe.db"

def get_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    with open("database/schema.sql", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Khởi tạo database thành công!")

if __name__ == "__main__":
    init_db()
