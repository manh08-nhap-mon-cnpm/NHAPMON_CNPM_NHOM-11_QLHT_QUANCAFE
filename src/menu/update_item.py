# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def delete_item(item_id):
    items = load_db("menu")
    new_list = [it for it in items if int(it["id"]) != int(item_id)]
    if len(new_list) == len(items):
        print("❌ Không tìm thấy món")
        return
    save_db("menu", new_list)
    print(f"🗑️ Đã xóa món {item_id}")

