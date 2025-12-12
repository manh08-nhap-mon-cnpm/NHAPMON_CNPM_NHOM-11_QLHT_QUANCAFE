# -*- coding: utf-8 -*-
from src.core.database import load_db
from src.payment.calc_total import calc_total

def print_bill(bill_id):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("⚠️ Bill chưa tồn tại")
        return
    print(f"\n=== HÓA ĐƠN {bill_id} ===")
    for l in bill.get("items", []):
        print(f"{l['name']} x{l['quantity']} = {int(l['price']) * int(l['quantity'])} đ")
    total = calc_total(bill_id)
    print(f"--- Tổng: {total} đ")

