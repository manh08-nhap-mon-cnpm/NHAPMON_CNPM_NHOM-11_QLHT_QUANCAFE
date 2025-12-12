# -*- coding: utf-8 -*-
from src.core.database import load_db, save_db, next_id
from src.payment.calc_total import calc_total

def create_payment(bill_id, amount_paid):
    bills = load_db("bills")
    payments = load_db("payments")
    bill = next((b for b in bills if int(b["id"]) == int(bill_id)), None)
    if not bill:
        print("❌ Bill không tồn tại")
        return
    total = calc_total(bill_id)
    pid = next_id("payments")
    payment = {
        "id": pid,
        "bill_id": int(bill_id),
        "amount_paid": int(amount_paid),
        "total": int(total),
        "change": int(amount_paid) - int(total)
    }
    payments.append(payment)
    save_db("payments", payments)
    # mark bill paid
    bill["status"] = "paid"
    save_db("bills", bills)
    print(f"✅ Thanh toán hoàn tất. Tiền thối: {payment['change']} đ")

