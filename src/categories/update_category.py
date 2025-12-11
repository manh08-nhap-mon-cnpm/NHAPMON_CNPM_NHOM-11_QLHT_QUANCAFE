# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_category(category_id, name):
    cats = load_db("categories")
    for c in cats:
        if int(c["id"]) == int(category_id):
            c["name"] = str(name)
            save_db("categories", cats)
            print("✅ Đã cập nhật danh mục")
            return
    print("❌ Không tìm thấy danh mục")
