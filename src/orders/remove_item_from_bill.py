# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db

def remove_item_from_bill(bill_id, item_id):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("❌ Bill không tồn tại")
        return
    new_items = [l for l in bill.get("items", []) if int(l["item_id"]) != int(item_id)]
    bill["items"] = new_items
    save_db("bills", bills)
    print(f"✅ Đã xóa món {item_id} khỏi bill {bill_id}")
