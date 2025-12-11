# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_ingredient(ingredient_id, name=None, quantity=None, unit=None):
    items = load_db("ingredients")
    for it in items:
        if int(it["id"]) == int(ingredient_id):
            if name is not None: it["name"] = str(name)
            if quantity is not None: it["quantity"] = float(quantity)
            if unit is not None: it["unit"] = str(unit)
            save_db("ingredients", items)
            print("✅ Cập nhật thành công")
            return
    print("❌ Không tìm thấy nguyên liệu")
