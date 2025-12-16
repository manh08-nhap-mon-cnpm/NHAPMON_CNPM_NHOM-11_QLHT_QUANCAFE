import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
c = conn.cursor()

# ===== USERS =====
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

# Tạo user mặc định
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', '123456', 'admin')")
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('staff', '123456', 'staff')")

# ===== TABLES =====
c.execute("""
CREATE TABLE IF NOT EXISTS tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    status TEXT
)
""")

for i in range(1, 6):
    c.execute("INSERT OR IGNORE INTO tables (id, name, status) VALUES (?, ?, ?)", (i, f"Bàn {i}", "empty"))

# ===== INVOICES =====
c.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER,
    total REAL,
    created_at TEXT
)
""")

conn.commit()
conn.close()
print("✅ Database 'database.db' da tao xong va san sang su dung!")
