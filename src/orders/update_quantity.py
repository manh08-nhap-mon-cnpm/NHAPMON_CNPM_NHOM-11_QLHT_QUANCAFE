# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def update_quantity(bill_id, item_id, quantity):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("❌ Bill không tồn tại")
        return
    for l in bill.get("items", []):
        if int(l["item_id"]) == int(item_id):
            l["quantity"] = int(quantity)
            save_db("bills", bills)
            print("✅ Cập nhật số lượng thành công")
            return
    print("❌ Món không có trong bill")
