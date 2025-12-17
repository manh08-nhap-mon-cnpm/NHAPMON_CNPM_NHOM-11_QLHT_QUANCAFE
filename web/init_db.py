import sqlite3
from datetime import datetime, timedelta
import random
import hashlib

# 1. Ham ma hoa mat khau (Bat buoc phai co de khop voi app.py)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")

# 2. TAO BANG
c.execute("DROP TABLE IF EXISTS invoice_items")
c.execute("DROP TABLE IF EXISTS invoices")
c.execute("DROP TABLE IF EXISTS tables")
c.execute("DROP TABLE IF EXISTS users")

c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, role TEXT)")
c.execute("CREATE TABLE tables (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, capacity INTEGER, status TEXT DEFAULT 'trong')")
c.execute("CREATE TABLE invoices (id INTEGER PRIMARY KEY AUTOINCREMENT, table_id INTEGER, total REAL, discount REAL DEFAULT 0, status TEXT DEFAULT 'paid', created_at TEXT, FOREIGN KEY(table_id) REFERENCES tables(id))")
c.execute("CREATE TABLE invoice_items (id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_id INTEGER, item_name TEXT, quantity INTEGER, price REAL, FOREIGN KEY(invoice_id) REFERENCES invoices(id))")

# 3. NAP USER (Ma hoa '123456')
pass_hashed = hash_password("123456")
c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", pass_hashed, "admin"))
c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("staff", pass_hashed, "staff"))

# 4. NAP BAN (Giu nguyen 10 ban cua may)
for i in range(1, 11):
    c.execute("INSERT INTO tables (id, name, capacity, status) VALUES (?, ?, ?, 'trong')", (i, f"Ban {i}", random.choice([2, 4, 6])))

# 5. MENU STARBUCKS CHUAN (Giu nguyen list may gui)
menu_items = [
    ("Caffe Latte", 75000), ("Cappuccino", 80000), ("Flat White", 80000),
    ("Caffe Mocha", 85000), ("Caramel Macchiato", 90000), ("Cold Brew", 65000),
    ("Java Chip Frappuccino", 100000), ("Green Tea Cream", 100000),
    ("Mango Passion Fruit", 80000), ("Signature Hot Chocolate", 75000),
    ("Pure Matcha Latte", 80000), ("Pink Drink Strawberry", 80000),
    ("Asian Dolce Latte", 80000), ("Caffe Americano", 60000)
]

# 6. TAO DOANH THU 300 TRIEU (Trong vong 30 ngay)
current_date = datetime.now()
print("Dang tao 300 trieu doanh thu...")

for day in range(30):
    date_obj = current_date - timedelta(days=day)
    date_str = date_obj.strftime("%Y-%m-%d")
    
    daily_sum = 0
    # Moi ngay kiem khoang 9.5tr - 10.5tr
    target = random.randint(9500000, 10500000)

    while daily_sum < target:
        item_name, price = random.choice(menu_items)
        qty = random.randint(1, 2)
        total_bill = price * qty
        
        # Tao gio ngau nhien tu 7h den 21h
        time_str = f"{random.randint(7, 21):02d}:{random.randint(0, 59):02d}:00"
        
        c.execute("INSERT INTO invoices (table_id, total, created_at, status) VALUES (?, ?, ?, 'paid')",
                  (random.randint(1, 10), total_bill, f"{date_str} {time_str}"))
        
        inv_id = c.lastrowid
        c.execute("INSERT INTO invoice_items (invoice_id, item_name, quantity, price) VALUES (?, ?, ?, ?)",
                  (inv_id, item_name, qty, price))
        daily_sum += total_bill

conn.commit()
conn.close()
print("------------------------------------------")
print("THANH CONG! May da co Database 300 trieu va Login duoc bang 123456.")