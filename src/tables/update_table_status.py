# src/tables/update_table_status.py
from src.core.database import load_db, save_db

def update_table_status(table_id, status):
    tables = load_db("tables")
    for t in tables:
        if t["id"] == int(table_id):
            t["status"] = str(status)
            save_db("tables", tables)
            print(f"🔄 Bàn {table_id} -> {status}")
            return
    print("❌ Không tìm thấy bàn")
