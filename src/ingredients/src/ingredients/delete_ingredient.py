# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def delete_ingredient(ingredient_id):
    items = load_db("ingredients")
    new_list = [it for it in items if int(it["id"]) != int(ingredient_id)]
    save_db("ingredients", new_list)
    print("🗑️ Đã xóa nguyên liệu (nếu tồn tại)")
