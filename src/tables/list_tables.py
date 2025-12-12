# src/tables/update_table.py
from src.core.database import load_db, save_db

def update_table(table_id, name=None, seats=None):
    tables = load_db("tables")
    for t in tables:
        if t["id"] == int(table_id):
            if name is not None:
                t["name"] = str(name)
            if seats is not None:
                t["seats"] = int(seats)
            save_db("tables", tables)
            print(f"✅ Đã cập nhật bàn {table_id}")
            return
    print("❌ Không tìm thấy bàn")
