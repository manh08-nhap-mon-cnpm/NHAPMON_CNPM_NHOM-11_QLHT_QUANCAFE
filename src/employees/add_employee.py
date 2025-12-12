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
# -*- coding: utf-8 -*-
from src.core.database import load_db

def list_employees():
    emps = load_db("employees")
    if not emps:
        print("Chưa có nhân viên")
        return
    for e in emps:
        print(f"ID {e['id']} | {e['name']} | {e['role']} | {e['phone']}")
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_employee(employee_id, name=None, role=None, phone=None):
    emps = load_db("employees")
    for e in emps:
        if int(e["id"]) == int(employee_id):
            if name is not None: e["name"] = str(name)
            if role is not None: e["role"] = str(role)
            if phone is not None: e["phone"] = str(phone)
            save_db("employees", emps)
            print("✅ Cập nhật nhân viên")
            return
    print("❌ Không tìm thấy nhân viên")
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def delete_employee(employee_id):
    emps = load_db("employees")
    new_list = [e for e in emps if int(e["id"]) != int(employee_id)]
    save_db("employees", new_list)
    print("🗑️ Đã xóa nhân viên (nếu tồn tại)")

