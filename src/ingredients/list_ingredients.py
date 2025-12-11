# -*- coding: utf-8 -*-
from src.core.database import load_db

def list_ingredients():
    items = load_db("ingredients")
    if not items:
        print("Chưa có nguyên liệu")
        return
    for it in items:
        print(f"ID {it['id']} | {it['name']} | {it['quantity']} {it['unit']}")
