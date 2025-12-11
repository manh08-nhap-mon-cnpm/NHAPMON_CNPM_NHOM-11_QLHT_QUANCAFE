from src.tables.list_tables import list_tables
from src.tables.create_table import create_table
from src.tables.update_table import update_table
from src.tables.delete_table import delete_table

from src.menu.list_items import list_menu
from src.menu.create_item import create_item
from src.menu.update_item import update_item
from src.menu.delete_item import delete_item

from src.categories.list_categories import list_categories
from src.categories.create_category import create_category
from src.categories.update_category import update_category
from src.categories.delete_category import delete_category

from src.orders.create_order import create_order
from src.orders.update_quantity import update_quantity
from src.orders.delete_item import delete_order_item
from src.orders.view_bill import view_bill

from src.payment.total_bill import get_total_bill
from src.payment.apply_discount import apply_discount
from src.payment.create_payment import create_payment
from src.payment.print_bill import print_bill

from src.revenue.daily_revenue import daily_revenue
from src.revenue.monthly_revenue import monthly_revenue
from src.revenue.bill_detail import bill_detail

from src.ingredients.list_ingredient import list_ingredients
from src.ingredients.create_ingredient import create_ingredient
from src.ingredients.update_ingredient import update_ingredient
from src.ingredients.delete_ingredient import delete_ingredient

from src.import.list_history import list_import_history
from src.import.create_import import create_import
from src.import.update_import import update_import
from src.import.delete_import import delete_import

from src.employees.list_employee import list_employees
from src.employees.create_employee import create_employee
from src.employees.update_employee import update_employee
from src.employees.delete_employee import delete_employee

from src.auth.login import login
from src.auth.change_password import change_password
from src.auth.assign_role import assign_role


def main():
    while True:
        print("\n===== QUẢN LÝ QUÁN CAFE =====")
        print("1. Quản lý bàn")
        print("2. Quản lý món")
        print("3. Quản lý danh mục")
        print("4. Gọi món & Hóa đơn")
        print("5. Thanh toán")
        print("6. Doanh thu")
        print("7. Nguyên liệu & Nhập hàng")
        print("8. Nhân viên")
        print("9. Tài khoản")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        # BÀN
        if choice == "1":
            while True:
                print("\n--- QUẢN LÝ BÀN ---")
                print("1. Xem danh sách bàn")
                print("2. Thêm bàn")
                print("3. Cập nhật bàn")
                print("4. Xóa bàn")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": list_tables()
                elif ch == "2": create_table()
                elif ch == "3": update_table()
                elif ch == "4": delete_table()
                elif ch == "0": break

        # MENU
        elif choice == "2":
            while True:
                print("\n--- QUẢN LÝ MÓN ---")
                print("1. Xem menu")
                print("2. Thêm món")
                print("3. Cập nhật món")
                print("4. Xóa món")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": list_menu()
                elif ch == "2": create_item()
                elif ch == "3": update_item()
                elif ch == "4": delete_item()
                elif ch == "0": break

        # DANH MỤC
        elif choice == "3":
            while True:
                print("\n--- QUẢN LÝ DANH MỤC ---")
                print("1. Xem danh mục")
                print("2. Thêm danh mục")
                print("3. Cập nhật danh mục")
                print("4. Xóa danh mục")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": list_categories()
                elif ch == "2": create_category()
                elif ch == "3": update_category()
                elif ch == "4": delete_category()
                elif ch == "0": break

        # ORDER
        elif choice == "4":
            while True:
                print("\n--- GỌI MÓN & HÓA ĐƠN ---")
                print("1. Tạo order")
                print("2. Cập nhật số lượng")
                print("3. Xóa món khỏi order")
                print("4. Xem hóa đơn hiện tại")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": create_order()
                elif ch == "2": update_quantity()
                elif ch == "3": delete_order_item()
                elif ch == "4": view_bill()
                elif ch == "0": break

        # PAYMENT
        elif choice == "5":
            while True:
                print("\n--- THANH TOÁN ---")
                print("1. Tính tổng hóa đơn")
                print("2. Áp dụng giảm giá")
                print("3. Tạo hóa đơn thanh toán")
                print("4. In hóa đơn")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": get_total_bill()
                elif ch == "2": apply_discount()
                elif ch == "3": create_payment()
                elif ch == "4": print_bill()
                elif ch == "0": break

        # REVENUE
        elif choice == "6":
            while True:
                print("\n--- DOANH THU ---")
                print("1. Doanh thu ngày")
                print("2. Doanh thu tháng")
                print("3. Chi tiết hóa đơn")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": daily_revenue()
                elif ch == "2": monthly_revenue()
                elif ch == "3": bill_detail()
                elif ch == "0": break

        # NGUYÊN LIỆU & NHẬP HÀNG
        elif choice == "7":
            while True:
                print("\n--- NGUYÊN LIỆU & NHẬP HÀNG ---")
                print("1. Xem nguyên liệu")
                print("2. Thêm nguyên liệu")
                print("3. Cập nhật nguyên liệu")
                print("4. Xóa nguyên liệu")
                print("5. Lịch sử nhập hàng")
                print("6. Tạo phiếu nhập")
                print("7. Cập nhật phiếu nhập")
                print("8. Xóa phiếu nhập")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": list_ingredients()
                elif ch == "2": create_ingredient()
                elif ch == "3": update_ingredient()
                elif ch == "4": delete_ingredient()
                elif ch == "5": list_import_history()
                elif ch == "6": create_import()
                elif ch == "7": update_import()
                elif ch == "8": delete_import()
                elif ch == "0": break

        # EMPLOYEE
        elif choice == "8":
            while True:
                print("\n--- NHÂN VIÊN ---")
                print("1. Xem nhân viên")
                print("2. Thêm nhân viên")
                print("3. Cập nhật nhân viên")
                print("4. Xóa nhân viên")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": list_employees()
                elif ch == "2": create_employee()
                elif ch == "3": update_employee()
                elif ch == "4": delete_employee()
                elif ch == "0": break

        # AUTH
        elif choice == "9":
            while True:
                print("\n--- TÀI KHOẢN ---")
                print("1. Đăng nhập")
                print("2. Đổi mật khẩu")
                print("3. Phân quyền")
                print("0. Quay lại")

                ch = input("Chọn: ")

                if ch == "1": login()
                elif ch == "2": change_password()
                elif ch == "3": assign_role()
                elif ch == "0": break

        elif choice == "0":
            print("Thoát hệ thống.")
            break


if __name__ == "__main__":
    main()

