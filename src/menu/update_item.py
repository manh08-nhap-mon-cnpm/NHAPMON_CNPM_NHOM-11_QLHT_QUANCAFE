# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_item(item_id, name=None, price=None, category_id=None):
    items = load_db("menu")
    for it in items:
        if int(it["id"]) == int(item_id):
            if name is not None:
                it["name"] = str(name)
            if price is not None:
                it["price"] = int(price)
            if category_id is not None:
                it["category_id"] = int(category_id)
            save_db("menu", items)
            print(f"✅ Đã cập nhật món {item_id}")
            return
    print("❌ Không tìm thấy món")
def delete_item(item_id):
    items = load_db("menu")
    new_list = [it for it in items if int(it["id"]) != int(item_id)]
    if len(new_list) == len(items):
        print("❌ Không tìm thấy món")
        return
    save_db("menu", new_list)
    print(f"🗑️ Đã xóa món {item_id}")

