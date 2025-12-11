# -*- coding: utf-8 -*-
from src.core.database import load_db

def bill_detail(bill_id):
    bills = load_db("bills")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("Không tìm thấy bill")
        return
    print(bill)
