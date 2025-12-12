def list_employees():
    """NV04 – Xem danh sách nhân viên"""
    print("Danh sách nhân viên")
# -*- coding: utf-8 -*-
from src.core.database import load_db

def list_employees():
    emps = load_db("employees")
    if not emps:
        print("Chưa có nhân viên")
        return
    for e in emps:
        print(f"ID {e['id']} | {e['name']} | {e['role']} | {e['phone']}")
