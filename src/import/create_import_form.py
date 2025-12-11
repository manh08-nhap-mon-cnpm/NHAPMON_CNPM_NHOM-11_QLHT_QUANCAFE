# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def create_import_form(supplier, items):
    forms = load_db("imports")
    fid = next_id("imports")
    form = {"id": fid, "supplier": str(supplier), "items": items}
    forms.append(form)
    save_db("imports", forms)
    print("✅ Đã tạo phiếu nhập")
