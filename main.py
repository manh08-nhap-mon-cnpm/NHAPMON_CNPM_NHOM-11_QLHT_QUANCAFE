# -*- coding: utf-8 -*-
# main.py (ĐÃ ĐƯỢC SỬA FULL – LOẠI BỎ KÝ TỰ \u00A0 và FIX UNICODE)

import os
import sys
import io
from colorama import init, Fore, Back, Style
import time

init(autoreset=True)

# ======================== CUSTOM PRINT (AN TOÀN 100%) ========================
def custom_print(*args, **kwargs):
    output = ' '.join(str(a) for a in args)

    # loại ký tự gây lỗi Unicode (NO‑BREAK SPACE)
    output = output.replace("\u00A0", " ")

    # encode/decode an toàn
    safe_output = output.encode('utf-8', 'replace').decode('utf-8')

    try:
        print(safe_output, **kwargs)
    except Exception:
        sys.stdout.write(safe_output + (kwargs.get('end', '\n')))

# ======================== ÉP TERMINAL SANG UTF-8 ========================
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        if os.name == 'nt':
            os.system('chcp 65001 > nul')
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    except:
        pass

# ======================== HÀM TIỆN ÍCH ========================
def dummy(*args, **kwargs):
    custom_print(f"{Fore.RED}⚠️ Chức năng đang phát triển...")

def enter_to_continue():
    input(f"{Fore.CYAN}\nNhấn Enter để tiếp tục...{Style.RESET_ALL}")

# ======================== IMPORT MODULES ========================
try:
    from src.tables.list_tables import list_tables
    from src.tables.create_table import create_table
    from src.tables.update_table import update_table
    from src.tables.delete_table import delete_table
    from src.tables.update_table_status import update_table_status
except:
    list_tables = create_table = update_table = delete_table = update_table_status = dummy

try:
    from src.categories.list_categories import list_categories
    from src.menu.list_items import list_items
    from src.menu.add_item import add_item
except:
    list_categories = list_items = add_item = dummy

try:
    from src.orders.add_item_to_bill import add_item_to_bill
    from src.orders.view_bill import view_bill
except:
    add_item_to_bill = view_bill = dummy

try:
    from src.payment.calc_total import calc_total
    from src.payment.create_payment import create_payment
    from src.payment.print_bill import print_bill
except:
    calc_total = create_payment = print_bill = dummy

try:
    from src.revenue.daily_revenue import daily_revenue
except:
    daily_revenue = dummy

try:
    from src.auth.login import login
    from src.auth.change_password import change_password
except:
    login = change_password = dummy

# ======================== CHUNG ========================
current_user = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ======================== MENU CON ========================
def table_management_menu():
    while True:
        clear_screen()
        custom_print(f"{Fore.YELLOW}===== 1. QUẢN LÝ BÀN =====")
        custom_print(" 1. TB01 – Tạo bàn mới")
        custom_print(" 2. TB02 – Cập nhật thông tin bàn")
        custom_print(" 3. TB03 – Xóa bàn")
        custom_print(" 4. TB04 – Xem danh sách bàn")
        custom_print(" 5. TB05 – Cập nhật trạng thái bàn")
        custom_print(" 0. Quay lại Menu Chính")

        ch = input(f"{Fore.CYAN}➤ Chọn chức năng (0-5): {Fore.WHITE}").strip()

        if ch == '1':
            name = input("Nhập Tên Bàn: ")
            seats = input("Nhập Số Ghế: ")
            try:
                create_table(name, int(seats))
            except:
                custom_print(f"{Fore.RED}Lỗi: Số ghế phải là số!")
        elif ch == '4':
            list_tables()
        elif ch == '0':
            break
        else:
            custom_print(f"{Fore.RED}Lựa chọn không hợp lệ.")
        enter_to_continue()


def menu_category_management_menu():
    while True:
        clear_screen()
        custom_print(f"{Fore.YELLOW}===== 2. QUẢN LÝ DANH MỤC & MÓN =====")
        custom_print(" 1. Xem danh mục")
        custom_print(" 2. Thêm danh mục")
        custom_print(" 3. Xem món")
        custom_print(" 4. Thêm món")
        custom_print(" 0. Quay lại Menu Chính")

        ch = input(f"Chọn (0-4): ").strip()

        if ch == '1':
            list_categories()
        elif ch == '3':
            list_items()
        elif ch == '4':
            name = input("Tên món: ")
            price = input("Giá: ")
            category = input("Loại danh mục: ")
            try:
                add_item(name, int(price), category)
            except:
                custom_print(f"{Fore.RED}Giá phải là số!")
        elif ch == '0':
            break
        else:
            custom_print("Sai lựa chọn!")
        enter_to_continue()


def order_management_menu():
    clear_screen()
    custom_print("===== 3. HÓA ĐƠN =====")
    view_bill(999)
    enter_to_continue()


def payment_management_menu():
    clear_screen()
    custom_print("===== 4. THANH TOÁN =====")
    calc_total(999)
    create_payment(999, 150000)
    print_bill(999)
    enter_to_continue()


def auth_management_menu():
    global current_user
    clear_screen()
    custom_print("===== 5. TÀI KHOẢN =====")
    if not current_user:
        login("admin", "123456")
        current_user = "admin"
    else:
        custom_print(f"Đã đăng nhập: {current_user}")
        change_password("admin", "old", "new")
    enter_to_continue()


def revenue_management_menu():
    clear_screen()
    custom_print("===== 9. BÁO CÁO DOANH THU =====")
    daily_revenue(time.strftime("%Y-%m-%d"))
    enter_to_continue()

# ======================== MENU CHÍNH ========================
def menu_chinh():
    global current_user
    while True:
        clear_screen()
        custom_print(f"{Fore.YELLOW}{'='*60}")
        custom_print(f"BREW MASTER - QUẢN LÝ QUÁN CAFE NHÓM 11")
        custom_print(f"{Fore.YELLOW}{'='*60}")

        custom_print(" 1. Quản lý bàn            6. Quản lý nguyên liệu")
        custom_print(" 2. Danh mục & món          7. Nhập hàng")
        custom_print(" 3. Gọi món / Hóa đơn       8. Quản lý nhân viên")
        custom_print(" 4. Thanh toán              9. Doanh thu")
        custom_print(" 5. Tài khoản               0. Thoát")

        if current_user:
            custom_print(f"→ Đăng nhập: {current_user}")

        ch = input("Chọn (0-9): ").strip()

        if ch == '1': table_management_menu()
        elif ch == '2': menu_category_management_menu()
        elif ch == '3': order_management_menu()
        elif ch == '4': payment_management_menu()
        elif ch == '5': auth_management_menu()
        elif ch == '9': revenue_management_menu()
        elif ch in ['6','7','8']:
            custom_print("Chức năng chưa xây dựng!")
            enter_to_continue()
        elif ch == '0':
            custom_print("Tạm biệt! ☕")
            break
        else:
            custom_print("Sai lựa chọn!")
            enter_to_continue()

# ======================== KHỞI ĐỘNG ========================
if __name__ == "__main__":
    clear_screen()
    custom_print("Đang khởi động hệ thống...")
    input("Nhấn Enter để tiếp tục...")
    menu_chinh()