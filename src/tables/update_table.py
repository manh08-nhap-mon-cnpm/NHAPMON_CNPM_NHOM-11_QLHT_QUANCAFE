# src/tables/create_table.py
from src.core.database import load_db, save_db, next_id

def create_table(name, seats):
    tables = load_db("tables")
    new_id = next_id("tables")
    table = {
        "id": new_id,
        "name": str(name),
        "seats": int(seats),
        "status": "Trống"
    }
    tables.append(table)
    save_db("tables", tables)
    print(f"✅ Tạo bàn thành công: ID {new_id} | {name} ({seats} ghế)")
