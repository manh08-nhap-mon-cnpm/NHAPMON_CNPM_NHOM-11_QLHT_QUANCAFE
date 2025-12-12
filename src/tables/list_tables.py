# src/tables/list_tables.py
from src.core.database import load_db

def list_tables():
    tables = load_db("tables")
    if not tables:
        print("⚠️ Chưa có bàn nào.")
        return
    print("\n=== DANH SÁCH BÀN ===")
    for t in tables:
        print(f"ID {t['id']} | {t['name']} | {t.get('seats','?')} ghế | {t.get('status','?')}")
