# src/tables/delete_table.py
from src.core.database import load_db, save_db

def delete_table(table_id):
    tables = load_db("tables")
    new_list = [t for t in tables if t["id"] != int(table_id)]
    if len(new_list) == len(tables):
        print("❌ Không tìm thấy bàn.")
        return
    save_db("tables", new_list)
    print(f"🗑️ Đã xóa bàn {table_id}")
