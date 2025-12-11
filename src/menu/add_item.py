# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id

def add_item_to_bill(bill_id, item_id, quantity):
    bills = load_db("bills")
    menu = load_db("menu")
    item = next((it for it in menu if int(it["id"]) == int(item_id)), None)
    if item is None:
        print("❌ Món không tồn tại")
        return
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if bill is None:
        bill = {"id": int(bill_id), "items": [], "status": "unpaid"}
        bills.append(bill)
    line = next((l for l in bill["items"] if int(l["item_id"]) == int(item_id)), None)
    if line:
        line["quantity"] += int(quantity)
    else:
        bill["items"].append({
            "item_id": int(item_id),
            "name": item["name"],
            "price": int(item["price"]),
            "quantity": int(quantity)
        })
    save_db("bills", bills)
    print(f"✅ Đã thêm món vào bill {bill_id}")
