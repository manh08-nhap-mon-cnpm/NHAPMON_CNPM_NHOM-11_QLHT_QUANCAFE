# ===================================
#      MAIN PROGRAM - CAFE MANAGER
# ===================================

# ----- TABLES -----
from src.tables.list_tables import list_tables
from src.tables.create_table import create_table
from src.tables.update_table import update_table
from src.tables.delete_table import delete_table
from src.tables.update_table_status import update_table_status

# ----- MENU -----
from src.menu.add_item import add_item
from src.menu.update_item import update_item
from src.menu.delete_item import delete_item
from src.menu.list_items import list_items

# ----- AUTH -----
from src.auth.login import login
from src.auth.change_password import change_password
from src.auth.assign_role import assign_role


# ---------------- MENU TABLES ----------------
def menu_tables():
    while True:
        print("\n=== QUẢN LÝ BÀN ===")
        print("1. Xem danh sách bàn")
        print("2. Tạo bàn mới")
        print("3. Cập nhật thông tin bàn")
        print("4. Xóa bàn")
        print("5. Cập nhật trạng thái bàn")
        print("0. Quay lại")
        ch = input("Chọn: ")

        if ch == "1":
            list_tables()

        elif ch == "2":
            name = input("Tên bàn: ")
            seats = input("Số ghế: ")
            create_table(name, seats)

        elif ch == "3":
            tid = input("ID bàn: ")
            name = input("Tên mới (enter bỏ qua): ")
            seats = input("Số ghế mới (enter bỏ qua): ")
            update_table(tid, name or None, seats or None)

        elif ch == "4":
            tid = input("ID bàn cần xóa: ")
            delete_table(tid)

        elif ch == "5":
            tid = input("ID bàn: ")
            status = input("Trạng thái mới: ")
            update_table_status(tid, status)

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn")


# ---------------- MENU MENU (MON) ----------------
def menu_menu():
    while True:
        print("\n=== QUẢN LÝ MÓN ===")
        print("1. Danh sách món")
        print("2. Thêm món")
        print("3. Cập nhật món")
        print("4. Xóa món")
        print("0. Quay lại")
        ch = input("Chọn: ")

        if ch == "1":
            list_items()

        elif ch == "2":
            name = input("Tên món: ")
            price = input("Giá: ")
            category = input("ID danh mục: ")
            add_item(name, price, category)

        elif ch == "3":
            mid = input("ID món: ")
            name = input("Tên mới (enter bỏ qua): ")
            price = input("Giá mới (enter bỏ qua): ")
            cate = input("Danh mục mới (enter bỏ qua): ")
            update_item(mid, name or None, price or None, cate or None)

        elif ch == "4":
            mid = input("ID món cần xóa: ")
            delete_item(mid)

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn")


# ---------------- MENU AUTH ----------------
def menu_auth():
    while True:
        print("\n=== QUẢN LÝ TÀI KHOẢN ===")
        print("1. Đăng nhập")
        print("2. Đổi mật khẩu")
        print("3. Gán quyền")
        print("0. Quay lại")
        ch = input("Chọn: ")

        if ch == "1":
            u = input("Username: ")
            p = input("Password: ")
            login(u, p)

        elif ch == "2":
            uid = input("User ID: ")
            old = input("Mật khẩu cũ: ")
            new = input("Mật khẩu mới: ")
            change_password(uid, old, new)

        elif ch == "3":
            uid = input("User ID: ")
            role = input("Quyền: ")
            assign_role(uid, role)

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn")


# ---------------- MAIN ----------------
def main():
    while True:
        print("\n===== MENU CHÍNH =====")
        print("1. Quản lý bàn")
        print("2. Quản lý món")
        print("3. Tài khoản / phân quyền")
        print("0. Thoát")

        ch = input("Chọn chức năng: ")

        if ch == "1":
            menu_tables()
        elif ch == "2":
            menu_menu()
        elif ch == "3":
            menu_auth()
        elif ch == "0":
            print("Thoát.")
            break
        else:
            print("Sai lựa chọn.")


if __name__ == "__main__":
    main()
