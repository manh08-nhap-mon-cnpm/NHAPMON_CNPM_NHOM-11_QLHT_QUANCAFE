# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def delete_import_form(form_id):
    forms = load_db("imports")
    new_list = [f for f in forms if int(f["id"]) != int(form_id)]
    save_db("imports", new_list)
    print("🗑️ Đã xóa phiếu nhập (nếu tồn tại)")
