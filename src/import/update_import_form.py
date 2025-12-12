# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_import_form(form_id, data):
    forms = load_db("imports")
    for f in forms:
        if int(f["id"]) == int(form_id):
            f.update(data)
            save_db("imports", forms)
            print("✅ Đã cập nhật phiếu nhập")
            return
    print("❌ Không tìm thấy phiếu nhập")
