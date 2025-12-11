# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def delete_category(category_id):
    cats = load_db("categories")
    new_list = [c for c in cats if int(c["id"]) != int(category_id)]
    if len(new_list) == len(cats):
        print("❌ Không tìm thấy danh mục")
        return
    save_db("categories", new_list)
    print("🗑️ Đã xóa danh mục")
