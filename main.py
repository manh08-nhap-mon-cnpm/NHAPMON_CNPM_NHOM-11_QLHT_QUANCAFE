# =======================
#  IMPORT CÁC CHỨC NĂNG 
# =======================

# Quản lý bàn
from src.tables.create_table import create_table
from src.tables.update_table import update_table
from src.tables.delete_table import delete_table
from src.tables.list_tables import list_tables
from src.tables.update_table_status import update_table_status

# Quản lý món
from src.menu.add_item import add_item
from src.menu.update_item import update_item
from src.menu.delete_item import delete_item
from src.menu.list_items import list_items

# Danh mục
from src.categories.add_category import add_category
from src.categories.update_category import update_category
from src.categories.delete_category import delete_category
from src.categories.list_categories import list_categories

# Gọi món / hóa đơn
from src.orders.add_item_to_bill import add_item_to_bill
from src.orders.update_quantity import update_quantity
from src.orders.remove_item_from_bill import remove_item_from_bill
from src.orders.view_bill import view_bill

# Thanh toán
from src.payment.calc_total import calc_total
from src.payment.apply_discount import apply_discount
from src.payment.create_payment import create_payment
from src.payment.print_bill import print_bill

# Doanh thu
from src.revenue.daily_revenue import daily_revenue
from src.revenue.monthly_revenue import monthly_revenue
from src.revenue.bill_detail import bill_detail

# Nguyên liệu
from src.ingredients.add_ingredient import add_ingredient
from src.ingredients.update_ingredient import update_ingredient
from src.ingredients.delete_ingredient import delete_ingredient
from src.ingredients.list_ingredients import list_ingredients

# Nhập hàng
from src.imports.create_import_form import create_import_form
from src.imports.update_import_form import update_import_form
from src.imports.delete_import_form import delete_import_form
from src.imports.history_import import history_import

# Nhân viên
from src.employees.add_employee import add_employee
from src.employees.update_employee import update_employee
from src.employees.delete_employee import delete_employee
from src.employees.list_employees import list_employees

# Tài khoản
from src.auth.login import login
from src.auth.change_password import change_password
from src.auth.assign_role import assign_role


# =======================
#     MENU CHÍNH
# =======================
def main():
    while True:
        print("\n===== QUẢN LÝ QUÁN CAFE =====")
        print("1. Quản lý bàn")
        print("2. Quản lý món")
        print("3. Danh mục")
        print("4. Gọi món / Hóa đơn")
        print("5. Thanh toán")
        print("6. Doanh thu")
        print("7. Nguyên liệu")
        print("8. Nhập hàng")
        print("9. Nhân viên")
        print("10. Tài khoản")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            menu_tables()
        elif choice == "2":
            menu_menu()
        elif choice == "3":
            menu_categories()
        elif choice == "4":
            menu_orders()
        elif choice == "5":
            menu_payment()
        elif choice == "6":
            menu_revenue()
        elif choice == "7":
            menu_ingredients()
        elif choice == "8":
            menu_imports()
        elif choice == "9":
            menu_employees()
        elif choice == "10":
            menu_auth()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Sai lựa chọn.")


# =======================
#     SUB-MENU
# =======================

def menu_tables():
    print("\n--- QUẢN LÝ BÀN ---")
    print("1. Tạo bàn")
    print("2. Cập nhật bàn")
    print("3. Xóa bàn")
    print("4. Xem danh sách bàn")
    print("5. Cập nhật trạng thái")
    c = input("Chọn: ")
    if c == "1":
        create_table(input("Tên: "), input("Ghế: "))
    elif c == "2":
        update_table(input("ID: "), input("Tên mới: "), input("Ghế mới: "))
    elif c == "3":
        delete_table(input("ID: "))
    elif c == "4":
        list_tables()
    elif c == "5":
        update_table_status(input("ID: "), input("Trạng thái: "))


def menu_menu():
    print("\n--- QUẢN LÝ MÓN ---")
    print("1. Thêm món")
    print("2. Cập nhật món")
    print("3. Xóa món")
    print("4. Xem danh sách món")
    c = input("Chọn: ")
    if c == "1":
        add_item(input("Tên: "), input("Giá: "), input("Danh mục: "))
    elif c == "2":
        update_item(input("ID: "), input("Tên mới: "), input("Giá mới: "), input("Danh mục mới: "))
    elif c == "3":
        delete_item(input("ID: "))
    elif c == "4":
        list_items()


def menu_categories():
    print("\n--- DANH MỤC ---")
    print("1. Thêm danh mục")
    print("2. Cập nhật")
    print("3. Xóa")
    print("4. Xem danh sách")
    c = input("Chọn: ")
    if c == "1":
        add_category(input("Tên: "))
    elif c == "2":
        update_category(input("ID: "), input("Tên mới: "))
    elif c == "3":
        delete_category(input("ID: "))
    elif c == "4":
        list_categories()


def menu_orders():
    print("\n--- GỌI MÓN / HÓA ĐƠN ---")
    print("1. Thêm món vào bill")
    print("2. Sửa số lượng")
    print("3. Xóa món khỏi bill")
    print("4. Xem bill")
    c = input("Chọn: ")
    if c == "1":
        add_item_to_bill(input("Bill: "), input("Món: "), input("SL: "))
    elif c == "2":
        update_quantity(input("Bill: "), input("Món: "), input("SL mới: "))
    elif c == "3":
        remove_item_from_bill(input("Bill: "), input("Món: "))
    elif c == "4":
        view_bill(input("Bill: "))


def menu_payment():
    print("\n--- THANH TOÁN ---")
    print("1. Tính tổng")
    print("2. Giảm giá")
    print("3. Tạo thanh toán")
    print("4. In bill")
    c = input("Chọn: ")
    if c == "1":
        calc_total(input("Bill: "))
    elif c == "2":
        apply_discount(input("Bill: "), input("Giảm (%): "))
    elif c == "3":
        create_payment(input("Bill: "), input("Khách trả: "))
    elif c == "4":
        print_bill(input("Bill: "))


def menu_revenue():
    print("\n--- DOANH THU ---")
    print("1. Doanh thu ngày")
    print("2. Doanh thu tháng")
    print("3. Chi tiết bill")
    c = input("Chọn: ")
    if c == "1":
        daily_revenue(input("Ngày: "))
    elif c == "2":
        monthly_revenue(input("Tháng: "), input("Năm: "))
    elif c == "3":
        bill_detail(input("Bill: "))


def menu_ingredients():
    print("\n--- NGUYÊN LIỆU ---")
    print("1. Thêm")
    print("2. Cập nhật")
    print("3. Xóa")
    print("4. Danh sách")
    c = input("Chọn: ")
    if c == "1":
        add_ingredient(input("Tên: "), input("SL: "), input("Đơn vị: "))
    elif c == "2":
        update_ingredient(input("ID: "), input("Tên mới: "), input("SL mới: "), input("Đơn vị mới: "))
    elif c == "3":
        delete_ingredient(input("ID: "))
    elif c == "4":
        list_ingredients()


def menu_imports():
    print("\n--- NHẬP HÀNG ---")
    print("1. Tạo phiếu nhập")
    print("2. Cập nhật")
    print("3. Xóa")
    print("4. Lịch sử nhập")
    c = input("Chọn: ")
    if c == "1":
        create_import_form(input("Nhà cung cấp: "), input("Danh sách hàng: "))
    elif c == "2":
        update_import_form(input("ID: "), input("Data: "))
    elif c == "3":
        delete_import_form(input("ID: "))
    elif c == "4":
        history_import()


def menu_employees():
    print("\n--- NHÂN VIÊN ---")
    print("1. Thêm nhân viên")
    print("2. Cập nhật")
    print("3. Xóa")
    print("4. Danh sách")
    c = input("Chọn: ")
    if c == "1":
        add_employee(input("Tên: "), input("Vai trò: "), input("SĐT: "))
    elif c == "2":
        update_employee(input("ID: "), input("Tên mới: "), input("Vai trò mới: "), input("SĐT mới: "))
    elif c == "3":
        delete_employee(input("ID: "))
    elif c == "4":
        list_employees()


def menu_auth():
    print("\n--- TÀI KHOẢN ---")
    print("1. Đăng nhập")
    print("2. Đổi mật khẩu")
    print("3. Phân quyền")
    c = input("Chọn: ")
    if c == "1":
        login(input("Username: "), input("Password: "))
    elif c == "2":
        change_password(input("ID: "), input("Mật khẩu cũ: "), input("Mật khẩu mới: "))
    elif c == "3":
        assign_role(input("User ID: "), input("Quyền: "))


# ========== CHẠY APP ==========
if __name__ == "__main__":
    main()
