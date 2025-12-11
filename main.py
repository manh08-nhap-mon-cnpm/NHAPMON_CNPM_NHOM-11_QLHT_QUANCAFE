# -*- coding: utf-8 -*-
# main.py
import sys
# Thiết lập mã hóa cho I/O nếu cần (chỉ cần trong môi trường terminal cũ)
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

# ====================================================================
# 1. IMPORTS
# ********************************************************************
# LƯU Ý: Nếu import báo lỗi, bạn cần tạo các file chức năng TẠM THỜI
# (chỉ cần hàm def và print) trong các thư mục tương ứng để Python
# có thể tìm thấy chúng.
# ********************************************************************

# 1) QUẢN LÝ BÀN - tables
try:
    from src.tables.create_table import create_table
    from src.tables.list_tables import list_tables
    # ... import các hàm còn lại: update_table, delete_table, update_table_status
except ImportError:
    pass # Bỏ qua lỗi import nếu các file chưa được tạo

# 2) QUẢN LÝ MÓN - menu
try:
    from src.menu.add_item import add_item
    from src.menu.list_items import list_items
    # ... import các hàm còn lại
except ImportError:
    pass

# ... (Tiếp tục import tất cả các hàm từ các module khác) ...
# ====================================================================
# 2. MENU CON (SUB-MENUS)
# ====================================================================

# 1) MENU QUẢN LÝ BÀN
def table_management_menu():
    while True:
        print("\n===== 1. QUẢN LÝ BÀN =====")
        print("1. TB01 – Tạo bàn mới")
        print("4. TB04 – Xem danh sách bàn")
        # ... (thêm các chức năng khác 2, 3, 5)
        print("0. Quay lại Menu Chính")
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            name = input("Tên Bàn: ")
            seats = int(input("Số Ghế: "))
            # Gọi hàm chức năng thực tế
            print(f"DEBUG: Gọi create_table({name}, {seats})")
            # create_table(name, seats) 
        elif choice == '4':
            print("DEBUG: Gọi list_tables()")
            # list_tables()
        elif choice == '0': break
        else: print("Lựa chọn không hợp lệ.")
        if choice != '0': input("\nNhấn Enter để tiếp tục...")

# 2) MENU QUẢN LÝ MÓN
def menu_management_menu():
    while True:
        print("\n===== 2. QUẢN LÝ MÓN =====")
        print("1. MN01 – Thêm món")
        print("4. MN04 – Xem danh sách món")
        # ... (thêm các chức năng khác 2, 3)
        print("0. Quay lại Menu Chính")
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            name = input("Tên Món: ")
            price = int(input("Giá: "))
            category_id = int(input("ID Danh mục: "))
            print(f"DEBUG: Gọi add_item({name}, {price}, {category_id})")
            # add_item(name, price, category_id)
        elif choice == '4':
            print("DEBUG: Gọi list_items()")
            # list_items()
        elif choice == '0': break
        else: print("Lựa chọn không hợp lệ.")
        if choice != '0': input("\nNhấn Enter để tiếp tục...")

# 3) MENU DANH MỤC
def categories_management_menu():
    print("\n--- Menu Danh mục đang được xây dựng... ---")
    # Tương tự như trên, bạn cần xây dựng menu con này

# 4) MENU GỌI MÓN / HÓA ĐƠN
def orders_menu():
    print("\n--- Menu Gọi món / Hóa đơn đang được xây dựng... ---")

# 5) MENU THANH TOÁN
def payment_menu():
    print("\n--- Menu Thanh toán đang được xây dựng... ---")

# 6) MENU DOANH THU
def revenue_menu():
    print("\n--- Menu Doanh thu đang được xây dựng... ---")

# 7) MENU NGUYÊN LIỆU
def ingredients_menu():
    print("\n--- Menu Nguyên liệu đang được xây dựng... ---")

# 8) MENU NHẬP HÀNG
def import_menu():
    print("\n--- Menu Nhập hàng đang được xây dựng... ---")

# 9) MENU NHÂN VIÊN
def employees_menu():
    print("\n--- Menu Nhân viên đang được xây dựng... ---")

# 10) MENU TÀI KHOẢN (AUTH)
def auth_menu():
    print("\n--- Menu Tài khoản (Auth) đang được xây dựng... ---")

# ====================================================================
# 3. HÀM MENU CHÍNH (MAIN FUNCTION)
# ====================================================================

def main():
    """Hàm chạy chính, hiển thị Menu Chính."""
    while True:
        print("\n=================================")
        print("====== HỆ THỐNG QUẢN LÝ QUÁN CÀ PHÊ ======")
        print("=================================")
        print("1. QUẢN LÝ BÀN")
        print("2. QUẢN LÝ MÓN")
        print("3. DANH MỤC")
        print("4. GỌI MÓN / HÓA ĐƠN")
        print("5. THANH TOÁN")
        print("6. DOANH THU")
        print("7. NGUYÊN LIỆU")
        print("8. NHẬP HÀNG")
        print("9. NHÂN VIÊN")
        print("10. TÀI KHOẢN (AUTH)")
        print("0. THOÁT CHƯƠNG TRÌNH")
        print("=================================")
        
        choice = input("Chọn chức năng (0-10): ").strip()

        if choice == '1': table_management_menu()
        elif choice == '2': menu_management_menu()
        elif choice == '3': categories_management_menu()
        elif choice == '4': orders_menu()
        elif choice == '5': payment_menu()
        elif choice == '6': revenue_menu()
        elif choice == '7': ingredients_menu()
        elif choice == '8': import_menu()
        elif choice == '9': employees_menu()
        elif choice == '10': auth_menu()
        elif choice == '0':
            print("Đang thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            
        if choice != '0':
            input("\nNhấn Enter để quay lại Menu Chính...")

# ====================================================================
# 4. CHẠY CHƯƠNG TRÌNH
# ====================================================================

if __name__ == "__main__":
    main()
