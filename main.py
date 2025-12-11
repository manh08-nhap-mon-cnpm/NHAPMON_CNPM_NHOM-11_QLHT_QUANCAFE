# -*- coding: utf-8 -*-
import os
os.system('chcp 65001 >nul')   # ← Dòng này fix lỗi tiếng Việt trên CMD
from colorama import init
init(autoreset=True)
# ... phần còn lại của code
# main.py
from src.data.database import db, init_data, get_next_id
from src.tables.list_tables import list_tables
from src.tables.create_table import create_table
from src.tables.update_table_status import update_table_status

from src.menu.list_items import list_items

from src.orders.add_item_to_bill import add_item_to_bill
from src.orders.update_quantity import update_quantity
from src.orders.remove_item_from_bill import remove_item_from_bill
from src.orders.view_bill import view_bill

from src.payment.calc_total import calc_total
from src.payment.apply_discount import apply_discount
from src.payment.print_bill import print_bill

import os
from datetime import datetime

# === Đăng nhập giả lập ===
current_user = None

def login():
    global current_user
    print("="*50)
    print("           ĐĂNG NHẬP HỆ THỐNG")
    print("="*50)
    username = input("Tên đăng nhập (admin): ") or "admin"
    password = input("Mật khẩu (123456): ") or "123456"
    
    user = next((u for u in db["users"] if u["username"] == username and u["password"] == password), None)
    if user:
        current_user = user
        print(f"\nChào mừng {user['role'].upper()} - {username}!")
        return True
    else:
        print("Sai tài khoản hoặc mật khẩu!")
        return False

# === Tạo hóa đơn mới khi khách ngồi bàn ===
def create_bill_for_table(table_id):
    bill_id = get_next_id("orders") + 1000  # để bill_id đẹp: 1001, 1002...
    db["orders"][bill_id] = {
        "table_id": table_id,
        "items": [],
        "status": "đang phục vụ",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "discount": 0
    }
    # Cập nhật trạng thái bàn
    update_table_status(table_id, "đang dùng")
    print(f"Đã mở bàn {table_id} → Hóa đơn mới: #{bill_id}")
    return bill_id

# === MENU CHÍNH ===
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*60)
        print("           NHÀ HÀNG NGON - PHIÊN BẢN PYTHON")
        print("="*60)
        print(f"Người dùng: {current_user['role'].upper()} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print("="*60)
        print("1. Quản lý bàn")
        print("2. Gọi món / Xem hóa đơn")
        print("3. Thanh toán")
        print("4. Quản trị (danh mục, món, nhân viên...)")
        print("5. Doanh thu")
        print("0. Đăng xuất")
        print("="*60)
        choice = input("Chọn chức năng: ")

        if choice == "1":
            table_menu()
        elif choice == "2":
            order_menu()
        elif choice == "3":
            payment_menu()
        elif choice == "4":
            admin_menu()
        elif choice == "5":
            revenue_menu()
        elif choice == "0":
            print("Tạm biệt!")
            break

# === MENU BÀN ===
def table_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("QUẢN LÝ BÀN")
        list_tables()
        print("\n1. Mở bàn mới (tạo hóa đơn)")
        print("2. Chuyển trạng thái bàn")
        print("0. Quay lại")
        c = input("\nChọn: ")
        if c == "1":
            list_tables()
            try:
                tid = int(input("\nNhập ID bàn muốn mở: "))
                table = next((t for t in db["tables"] if t["id"] == tid), None)
                if table and table["status"] == "trống":
                    create_bill_for_table(tid)
                else:
                    print("Bàn không tồn tại hoặc đang sử dụng!")
            except:
                print("ID không hợp lệ!")
            input("Nhấn Enter để tiếp tục...")
        elif c == "2":
            tid = int(input("Nhập ID bàn: "))
            status = input("Trạng thái mới (trống/đang dùng/đã đặt/dọn dẹp): ")
            update_table_status(tid, status)
            input("Đã cập nhật! Enter để tiếp...")
        elif c == "0":
            break

# === MENU GỌI MÓN ===
def order_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("GỌI MÓN & XEM HÓA ĐƠN")
        print("Hóa đơn đang mở:")
        active_bills = [b for b in db["orders"].values() if b["status"] == "đang phục vụ"]
        for bill in active_bills[:10]:  # chỉ hiện 10 cái đầu
            print(f"   • Bill #{list(db['orders'].keys())[list(db['orders'].values()).index(bill)]} - Bàn {bill['table_id']}")
        print("\n1. Chọn hóa đơn để gọi món")
        print("2. Xem tất cả món ăn")
        print("0. Quay lại")
        c = input("\nChọn: ")
        if c == "1":
            try:
                bill_id = int(input("Nhập mã hóa đơn: "))
                if bill_id in db["orders"]:
                    call_dish_menu(bill_id)
                else:
                    print("Không tìm thấy hóa đơn!")
            except:
                print("Sai mã!")
            input("Enter để tiếp...")
        elif c == "2":
            list_items()
            input("Enter để tiếp...")
        elif c == "0":
            break

def call_dish_menu(bill_id):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        view_bill(bill_id)
        print("\n1. Thêm món")
        print("2. Sửa số lượng")
        print("3. Xóa món")
        print("0. Quay lại")
        c = input("\nChọn: ")
        if c == "1":
            list_items()
            try:
                item_id = int(input("Nhập ID món: "))
                qty = int(input("Số lượng: ") or "1")
                add_item_to_bill(bill_id, item_id, qty)
            except:
                print("Lỗi nhập!")
        elif c == "2":
            item_id = int(input("ID món cần sửa: "))
            qty = int(input("Số lượng mới: "))
            update_quantity(bill_id, item_id, qty)
        elif c == "3":
            item_id = int(input("ID món cần xóa: "))
            remove_item_from_bill(bill_id, item_id)
        elif c == "0":
            break
        input("Enter để tiếp...")

# === MENU THANH TOÁN ===
def payment_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("THANH TOÁN")
    for bill_id, bill in db["orders"].items():
        if bill["status"] == "đang phục vụ":
            print(f"   • Bill #{bill_id} - Bàn {bill['table_id']}")
    try:
        bill_id = int(input("\nNhập mã hóa đơn cần thanh toán: "))
        if bill_id in db["orders"] and db["orders"][bill_id]["status"] == "đang phục vụ":
            view_bill(bill_id)
            discount = input("Giảm giá % (để trống nếu không): ")
            if discount:
                apply_discount(bill_id, int(discount))
            print_bill(bill_id)
            db["orders"][bill_id]["status"] = "đã thanh toán"
            # Cập nhật trạng thái bàn về trống
            table_id = db["orders"][bill_id]["table_id"]
            update_table_status(table_id, "trống")
            print(f"\nHOÁ ĐƠN #{bill_id} ĐÃ THANH TOÁN THÀNH CÔNG!")
        else:
            print("Hóa đơn không tồn tại hoặc đã thanh toán!")
    except:
        print("Lỗi!")
    input("\nNhấn Enter để về menu chính...")

# Các menu còn lại (admin, revenue) mình làm ngắn gọn
def admin_menu():
    print("Chức năng quản trị đang phát triển...")
    input("Enter...")

def revenue_menu():
    print("Doanh thu hôm nay: 0đ (sắp có)")
    input("Enter...")

# === CHẠY CHƯƠNG TRÌNH ===
if __name__ == "__main__":
    db.clear()
    db.update(init_data())  # Khởi tạo dữ liệu mẫu
    
    if login():
        main_menu()
