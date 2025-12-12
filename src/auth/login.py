def login(username, password):
    """TK01 – Đăng nhập"""
    print(f"Đăng nhập: {username}")
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def login(username, password):
    users = load_db("users")
    if not users:
        # tạo user admin mặc định
        u = {"id": 1, "username": "admin", "password": "123456", "role": "admin"}
        users.append(u)
        save_db("users", users)
    user = next((u for u in users if u.get("username") == username and u.get("password") == password), None)
    if user:
        print(f"✅ Đăng nhập thành công: {username}")
        return user
    print("❌ Sai username/password")
    return None
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def change_password(user_id, old_password, new_password):
    users = load_db("users")
    for u in users:
        if int(u.get("id",0)) == int(user_id) and u.get("password") == old_password:
            u["password"] = new_password
            save_db("users", users)
            print("✅ Đổi mật khẩu thành công")
            return
    print("❌ Thông tin không hợp lệ")
# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def assign_role(user_id, role):
    users = load_db("users")
    for u in users:
        if int(u.get("id",0)) == int(user_id):
            u["role"] = str(role)
            save_db("users", users)
            print("✅ Đã phân quyền")
            return
    print("❌ Không tìm thấy user")


  
