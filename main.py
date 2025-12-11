# -*- coding: utf-8 -*-
# main.py
# CODE ĐÃ ĐƯỢC TỐI ƯU HÓA ĐỂ CHẠY TRONG TERMINAL VỚI TIẾNG VIỆT VÀ COLORAMA

import os
import sys
from colorama import init, Fore, Back, Style
import time

# ====================================================================
# KHẮC PHỤC LỖI MÃ HÓA CHO TERMINAL VÀ COLORAMA
# ====================================================================
init(autoreset=True)

# Khắc phục lỗi cp1252 bằng cách buộc sử dụng UTF-8 cho I/O (Cách mạnh nhất)
if sys.stdout.encoding != 'utf-8':
    try:
        # Nếu đang chạy trên Windows và chưa có UTF-8
        if os.name == 'nt':
            # 1. Thử dùng lệnh chcp (cho CMD/PowerShell)
            os.system('chcp 65001 > nul')
            
            # 2. Khắc phục lỗi stdout/stdin (cách này hoạt động tốt nhất)
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    except Exception:
        pass


# ====================================================================
# DUMMY FUNCTION VÀ IMPORTS
# ====================================================================

def dummy(*args, **kwargs):
    """Hàm giả lập khi module chưa được triển khai."""
    print(f"{Fore.RED}⚠️ Chức năng đang phát triển... ({Style.RESET_ALL}Thiếu module)")

def enter_to_continue():
    """Hàm tiện ích chờ người dùng nhấn Enter."""
    input(f"{Fore.CYAN}\nNhấn Enter để tiếp tục...{Style.RESET_ALL}")

# --- IMPORT MODULES ---
# Để code chạy mượt mà ngay cả khi thiếu file, chúng ta gán hàm dummy
# nếu import thất bại, sử dụng các hàm bạn đã định nghĩa.

# 1) QUẢN LÝ BÀN
try:
    from src.tables.list_tables import list_tables
    from src.tables.create_table import create_table
    from src.tables.update_table import update_table
    from src.tables.delete_table import delete_table
    from src.tables.update_table_status import update_table_status
except ImportError:
    list_tables = create_table = update_table = delete_table = update_table_status = dummy

# 2) QUẢN LÝ MÓN (Menu) & DANH MỤC (Categories)
try:
    from src.categories.list_categories import list_categories
    from src.menu.list_items import list_items
    from src.menu.add_item import add_item
    # Cần thêm các hàm còn lại: update_item, delete_item, add_category...
except ImportError:
    list_categories = list_items = add_item = dummy

# 3) GỌI MÓN / HÓA ĐƠN
try:
    from src.orders.add_item_to_bill import add_item_to_bill
    from src.orders.view_bill import view_bill
except ImportError:
    add_item_to_bill = view_bill = dummy

# 4) THANH TOÁN
try:
    from src.payment.calc_total import calc_total
    from src.payment.create_payment import create_payment
    from src.payment.print_bill import print_bill
except ImportError:
    calc_total = create_payment = print_bill = dummy

# 5) BÁO CÁO DOANH THU
try:
    from src.revenue.daily_revenue import daily_revenue
except ImportError:
    daily_revenue = dummy

# 6) TÀI KHOẢN (Auth)
try:
    from src.auth.login import login
    from src.auth.change_password import change_password
except ImportError:
    login = change_password = dummy
    
# Thêm các module còn lại tương tự (Nguyên liệu, Nhập hàng, Nhân viên...)
# ...

# ====================================================================
# BIẾN TOÀN CỤC & TIỆN ÍCH
# ====================================================================

current_user = None

def clear_screen():
    """Xóa màn hình Terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ====================================================================
# CÁC MENU CON TƯƠNG TÁC (TẤT CẢ ĐÃ CHUYỂN SANG MENU TƯƠNG TÁC)
# ====================================================================

# 1. QUẢN LÝ BÀN
def table_management_menu():
    while True:
        clear_screen()
        print(f"{Fore.YELLOW}===== 1. QUẢN LÝ BÀN =====")
        print(f"{Fore.WHITE} 1. TB01 – Tạo bàn mới")
        print(f"{Fore.WHITE} 2. TB02 – Cập nhật thông tin bàn")
        print(f"{Fore.WHITE} 3. TB03 – Xóa bàn")
        print(f"{Fore.WHITE} 4. TB04 – Xem danh sách bàn")
        print(f"{Fore.WHITE} 5. TB05 – Cập nhật trạng thái bàn")
        print(f"{Fore.CYAN} 0. Quay lại Menu Chính")
        print(f"{Fore.YELLOW}==========================")
        
        ch = input(f"{Fore.CYAN}➤ Chọn chức năng (0-5): {Fore.WHITE}").strip()

        if ch == '1':
            name = input(f"{Fore.GREEN}Nhập Tên Bàn: {Fore.WHITE}")
            seats = input(f"{Fore.GREEN}Nhập Số Ghế: {Fore.WHITE}")
            try:
                create_table(name, int(seats))
            except ValueError:
                print(f"{Fore.RED}Lỗi: Số ghế phải là số nguyên!")
        elif ch == '4':
            list_tables()
        elif ch == '0': 
            break
        else:
            print(f"{Fore.RED}Lựa chọn không hợp lệ.")
            
        enter_to_continue()


# 2. QUẢN LÝ DANH MỤC & MÓN
def menu_category_management_menu():
    while True:
        clear_screen()
        print(f"{Fore.YELLOW}===== 2. QUẢN LÝ DANH MỤC & MÓN =====")
        print(f"{Fore.WHITE} 1. Danh mục: Xem danh sách")
        print(f"{Fore.WHITE} 2. Danh mục: Thêm mới")
        print(f"{Fore.WHITE} 3. Món: Xem danh sách")
        print(f"{Fore.WHITE} 4. Món: Thêm mới")
        print(f"{Fore.CYAN} 0. Quay lại Menu Chính")
        print(f"{Fore.YELLOW}=====================================")

        ch = input(f"{Fore.CYAN}➤ Chọn chức năng (0-4): {Fore.WHITE}").strip()

        if ch == "1":
            print(f"{Fore.GREEN}--- Danh sách Danh mục ---")
            list_categories()
        elif ch == "3":
            print(f"{Fore.GREEN}--- Danh sách Món ---")
            list_items()
        elif ch == "4":
            print(f"{Fore.GREEN}--- Thêm món mới ---")
            name = input("Tên món: ")
            price = input("Giá: ")
            category = input("Loại danh mục: ")
            try:
                add_item(name, int(price), category)
            except ValueError:
                print(f"{Fore.RED}Lỗi: Giá phải là số nguyên!")
        elif ch == "0":
            break
        else:
            print(f"{Fore.RED}Lựa chọn không hợp lệ.")
            
        enter_to_continue()

# 3. GỌI MÓN / HÓA ĐƠN
def order_management_menu():
    # Tương tự, bạn sẽ triển khai logic cho GOI01-GOI04 tại đây
    clear_screen()
    print(f"{Fore.YELLOW}===== 3. GỌI MÓN / HÓA ĐƠN =====")
    view_bill(999) # Chỉ chạy demo xem bill
    enter_to_continue()

# 4. THANH TOÁN
def payment_management_menu():
    # Triển khai logic cho TT01-TT04 tại đây
    clear_screen()
    print(f"{Fore.YELLOW}===== 4. THANH TOÁN =====")
    calc_total(999)
    create_payment(999, 150000)
    print_bill(999)
    enter_to_continue()
    
# 5. TÀI KHOẢN & PHÂN QUYỀN
def auth_management_menu():
    global current_user
    clear_screen()
    print(f"{Fore.YELLOW}===== 5. TÀI KHOẢN & PHÂN QUYỀN =====")
    if not current_user:
        login("admin", "123456")
        # Giả lập đăng nhập thành công
        current_user = "admin"
    else:
        print(f"{Fore.GREEN}Bạn đang đăng nhập với quyền: {current_user}")
        change_password("admin", "old", "new")
    enter_to_continue()

# 9. BÁO CÁO DOANH THU
def revenue_management_menu():
    clear_screen()
    print(f"{Fore.YELLOW}===== 9. BÁO CÁO DOANH THU =====")
    daily_revenue(time.strftime("%Y-%m-%d"))
    enter_to_continue()


# ====================================================================
# MENU CHÍNH (MAIN FUNCTION)
# ====================================================================

def menu_chinh():
    global current_user
    while True:
        clear_screen()
        print(f"{Back.BLACK}{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}           BREW MASTER - QUẢN LÝ QUÁN CAFE NHÓM 11")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
        
        # In các lựa chọn menu chính
        print(f"{Fore.WHITE}   1. Quản lý bàn               6. Quản lý nguyên liệu")
        print(f"{Fore.WHITE}   2. Quản lý danh mục & món    7. Nhập hàng")
        print(f"{Fore.WHITE}   3. Gọi món / Hóa đơn         8. Quản lý nhân viên")
        print(f"{Fore.WHITE}   4. Thanh toán                9. Báo cáo doanh thu")
        print(f"{Fore.WHITE}   5. Tài khoản & phân quyền    0. Thoát")
        
        if current_user:
            print(f"{Fore.GREEN}   → Đã đăng nhập: {current_user}")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")

        ch = input(f"{Fore.CYAN}   ➤ Chọn chức năng (0-9): {Fore.WHITE}").strip()

        if ch == "1":
            table_management_menu()
        elif ch == "2":
            menu_category_management_menu()
        elif ch == "3":
            order_management_menu()
        elif ch == "4":
            payment_management_menu()
        elif ch == "5":
            auth_management_menu()
        elif ch == "9":
            revenue_management_menu()
        
        # Xử lý các chức năng chưa triển khai (6, 7, 8)
        elif ch in ["6", "7", "8"]:
            print(f"{Fore.RED}Chức năng {ch} đang được xây dựng!")
            enter_to_continue()
        
        elif ch == "0":
            print(f"{Fore.MAGENTA}   Hẹn gặp lại NHÓM 11! ☕ Cảm ơn đã sử dụng BREW MASTER!")
            break
        else:
            print(f"{Fore.RED}   Sai rồi đại ca ơi! Chọn lại đi...")
            enter_to_continue()

# ====================================================================
# KHỞI ĐỘNG
# ====================================================================

if __name__ == "__main__":
    clear_screen()
    print(f"{Fore.GREEN}   Đang khởi động hệ thống quản lý quán cafe NHÓM 11...")
    print(f"{Fore.YELLOW}   Nhấn Enter để vào menu chính...")
    input()
    menu_chinh()
