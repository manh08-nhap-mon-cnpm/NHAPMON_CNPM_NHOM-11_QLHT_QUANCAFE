# -*- coding: utf-8 -*-
from src.core.database import load_db

def view_bill(bill_id):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("⚠️ Bill chưa tồn tại")
        return
    print(f"\n=== HÓA ĐƠN {bill_id} ===")
    total = 0
    for l in bill.get("items", []):
        line_total = int(l["price"]) * int(l["quantity"])
        total += line_total
        print(f"{l['name']} x{l['quantity']} = {line_total} đ")
    print(f"--- Tổng: {total} đ")
