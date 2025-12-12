# -*- coding: utf-8 -*-
from src.core.database import load_db

def calc_total(bill_id):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("⚠️ Bill chưa tồn tại")
        return 0
    total = sum(int(l["price"]) * int(l["quantity"]) for l in bill.get("items", []))
    print(f"Tổng bill {bill_id}: {total} đ")
    return total
