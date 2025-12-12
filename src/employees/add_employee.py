def add_employee(name, role, phone):
    """NV01 – Thêm nhân viên"""
    print(f"Thêm nhân viên {name}")
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def add_employee(name, role, phone):
    emps = load_db("employees")
    eid = next_id("employees")
    emps.append({"id": eid, "name": str(name), "role": str(role), "phone": str(phone)})
    save_db("employees", emps)
    print("✅ Thêm nhân viên thành công")
