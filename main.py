# -*- coding: utf-8 -*-
import os
import sys
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Fix tiếng Việt trên Windows
os.system('chcp 65001 >nul')

# Import tất cả module (nếu thiếu sẽ vẫn chạy nhờ dummy)
def dummy(*args, **kwargs):
    print("⚠️  Chức năng đang phát triển...")

# --- TABLES ---
try:
    from src.tables.list_tables import list_tables
    from src.tables.create_table import create_table
    from src.tables.update_table import update_table
    from src.tables.delete_table import delete_table
    from src.tables.update_table_status import update_table_status
except:
    list_tables = create_table = update_table = delete_table = update_table_status = dummy

# --- MENU & CATEGORIES ---
try:
    from src.categories.list_categories import list_categories
    from src.menu.list_items import list_items
    from src.menu.add_item import add_item
except:
    list_categories = list_items = add_item = dummy

# --- ORDERS ---
try:
    from src.orders.add_item_to_bill import add_item_to_bill
    from src.orders.view_bill import view_bill
except:
    add_item_to_bill = view_bill = dummy

# --- PAYMENT ---
try:
    from src.payment.calc_total import calc_total
    from src.payment.create_payment import create_payment
    from src.payment.print_bill import print_bill
except:
    calc_total = create_payment = print_bill = dummy

# --- REVENUE ---
try:
    from src.revenue.daily_revenue import daily_revenue
except:
    daily_revenue = dummy

# --- AUTH ---
try:
    from src.auth.login import login
    from src.auth.change_password import change_password
except:
    login = change_password = dummy

# Biến toàn cục kiểm tra đăng nhập
current_user = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_chinh():
    global current_user
    while True:
        clear_screen()
        print(f"{Back.BLACK}{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}           BREW MASTER - QUẢN LÝ QUÁN CAFE NHÓM 11")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   1. Quản lý bàn               6. Quản lý nguyên liệu")
        print(f"{Fore.WHITE}   2. Quản lý danh mục & món    7. Nhập hàng")
        print(f"{Fore.WHITE}   3. Gọi món / Hóa đơn         8. Quản lý nhân viên")
        print(f"{Fore.WHITE}   4. Thanh toán                9. Báo cáo doanh thu")
        print(f"{Fore.WHITE}   5. Tài khoản & phân quyền    0. Thoát")
        if current_user:
            print(f"{Fore.GREEN}   → Đã đăng nhập: {current_user}")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")

        ch = input(f"{Fore.CYAN}   ➤ Chọn chức năng (0-9): {Fore.WHITE}").strip()

        if ch == "1":
            list_tables(); input("\nNhấn Enter để tiếp tục...")
        elif ch == "2":
            list_categories(); input("\nNhấn Enter...")
            list_items(); input("\nNhấn Enter...")
        elif ch == "3":
            view_bill(1); input("\nNhấn Enter...")
        elif ch == "4":
            calc_total(1)
            create_payment(1, 150000)
            print_bill(1); input("\nNhấn Enter...")
        elif ch == "5":
            if not current_user:
                login("admin", "123456")
            else:
                print("Đã đăng nhập rồi!")
            input("\nNhấn Enter...")
        elif ch == "9":
            daily_revenue("2025-12-11"); input("\nNhấn Enter...")
        elif ch == "0":
            print(f"{Fore.MAGENTA}   Hẹn gặp lại NHÓM 11! ☕ Cảm ơn đã sử dụng BREW MASTER!")
            break
        else:
            print(f"{Fore.RED}   Sai rồi đại ca ơi! Chọn lại đi...")
            input("   Nhấn Enter...")

# === KHỞI ĐỘNG ===
if __name__ == "__main__":
    clear_screen()
    print(f"{Fore.GREEN}   Đang khởi động hệ thống quản lý quán cafe NHÓM 11...")
    print(f"{Fore.YELLOW}   Nhấn Enter để vào menu chính...")
    input()
    menu_chinh()
