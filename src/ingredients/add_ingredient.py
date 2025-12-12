# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def add_ingredient(name, quantity, unit):
    items = load_db("ingredients")
    iid = next_id("ingredients")
    items.append({"id": iid, "name": str(name), "quantity": float(quantity), "unit": str(unit)})
    save_db("ingredients", items)
    print("✅ Thêm nguyên liệu thành công")
