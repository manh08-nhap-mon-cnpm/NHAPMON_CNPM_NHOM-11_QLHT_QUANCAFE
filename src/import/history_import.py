# -*- coding: utf-8 -*-
from src.core.database import load_db

def history_import():
    forms = load_db("imports")
    if not forms:
        print("Chưa có phiếu nhập")
        return
    for f in forms:
        print(f"ID {f['id']} | Supplier: {f.get('supplier')} | items: {len(f.get('items', []))}")

