# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def add_category(name):
    cats = load_db("categories")
    cid = next_id("categories")
    cats.append({"id": cid, "name": str(name)})
    save_db("categories", cats)
    print(f"✅ Đã thêm danh mục {name} (ID {cid})")
