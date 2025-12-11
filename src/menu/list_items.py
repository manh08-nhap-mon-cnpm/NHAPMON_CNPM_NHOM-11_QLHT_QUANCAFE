# -*- coding: utf-8 -*-
from src.core.database import load_db

def list_items():
    items = load_db("menu")
    if not items:
        print("⚠️ Chưa có món nào.")
        return
    print("\n=== DANH SÁCH MÓN ===")
    for it in items:
        print(f"ID {it['id']} | {it['name']} | {it['price']} đ | Category {it.get('category_id')}")
