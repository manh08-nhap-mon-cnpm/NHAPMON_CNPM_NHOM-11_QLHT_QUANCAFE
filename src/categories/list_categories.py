# -*- coding: utf-8 -*-
from src.core.database import load_db

def list_categories():
    cats = load_db("categories")
    if not cats:
        print("⚠️ Chưa có danh mục.")
        return
    print("\n=== DANH MỤC ===")
    for c in cats:
        print(f"ID {c['id']} | {c['name']}")
