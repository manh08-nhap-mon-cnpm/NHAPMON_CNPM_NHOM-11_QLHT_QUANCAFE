# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def add_item(name, price, category_id):
    items = load_db("menu")
    new_id = next_id("menu")
    item = {
        "id": new_id,
        "name": str(name),
        "price": int(price),
        "category_id": int(category_id) if category_id is not None else None
    }
    items.append(item)
    save_db("menu", items)
    print(f"✅ Đã thêm món: {name} (ID {new_id})")
